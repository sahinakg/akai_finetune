"""
AKAI Dataset Generator
======================
Türk hukuk modeli için fine-tuning dataseti oluşturma aracı.

Özellikler:
- GPT-4o ile yarı-otomatik instruction pair üretimi
- Manuel çift ekleme
- JSONL formatına dönüştürme
- Kalite validasyonu
- Kategori bazlı istatistik

Kurulum:
    pip install openai tqdm colorama

Kullanım:
    1. Otomatik üretim:   python akai_dataset_generator.py --mode generate
    2. Manuel ekleme:     python akai_dataset_generator.py --mode manual
    3. Validasyon:        python akai_dataset_generator.py --mode validate
    4. İstatistik:        python akai_dataset_generator.py --mode stats
    5. Dışa aktarım:      python akai_dataset_generator.py --mode export
"""

import sys
import json
import os
import re
import hashlib
import argparse

# Windows konsolu (cp1254 vb.) emoji/Türkçe karakterlerde çökmesin diye
# standart çıktıyı UTF-8'e ayarla; desteklenmiyorsa hataları görmezden gel.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
from pathlib import Path
from datetime import datetime
from typing import Optional

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️  openai paketi bulunamadı. Otomatik üretim için: pip install openai")

try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False

# ─────────────────────────────────────────────
# YAPILANDIRMA
# ─────────────────────────────────────────────

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")   # Ortam değişkeninden al

SYSTEM_PROMPT = (
    "Sen AKAI'sin — Türk hukukçular için geliştirilmiş yapay zeka asistanı. "
    "Kanunları, içtihatları ve hukuki kavramları doğru, anlaşılır ve kaynaklı biçimde açıklarsın. "
    "Hukuki tavsiye vermezsin; bilgi ve analiz sunarsın."
)

DATA_DIR = Path("akai_data")
RAW_DIR = DATA_DIR / "raw"          # Ham kaynak metinler
PAIRS_FILE = DATA_DIR / "pairs.jsonl"   # Tüm çiftler
EXPORT_FILE = DATA_DIR / "dataset_export.jsonl"  # Fine-tune için hazır

# Hedef çift sayıları
CATEGORY_TARGETS = {
    "kanun_maddesi": 200,
    "hukuki_kavram": 150,
    "dilekce_uretimi": 200,
    "karar_ozeti": 200,
    "ret_sinir": 150,
    "cok_turlu_diyalog": 200,
    "belge_analizi": 150,
    "dilekce_wizard": 150,
}

CATEGORY_LABELS = {
    "kanun_maddesi": "Kanun Maddesi Açıklama",
    "hukuki_kavram": "Hukuki Kavram Tanımı",
    "dilekce_uretimi": "Dilekçe Üretimi",
    "karar_ozeti": "Karar Özeti / Analizi",
    "ret_sinir": "Ret / Sınır Örnekleri",
    "cok_turlu_diyalog": "Çok Turlu Diyalog",
    "belge_analizi": "Belge Analizi",
    "dilekce_wizard": "Dilekçe Wizard Akışı",
}

# Her kategori için GPT-4o'ya verilecek üretim talimatları
GENERATION_PROMPTS = {
    "kanun_maddesi": """
Türk hukuku alanında bir fine-tuning dataseti oluşturuyorum.
Aşağıdaki kanun maddesi için 5 adet soru-cevap çifti üret.

Kanun metni:
{source_text}

Kurallar:
- Her çiftte "user" soruyu, "assistant" cevabı içersin
- Cevaplar avukat üslubunda, kaynaklı (madde numarası, Yargıtay dairesi) olsun
- Farklı soru tipleri kullan: "nedir?", "ne zaman?", "nasıl işler?", "farkı ne?"
- JSON listesi olarak döndür: [{{"user": "...", "assistant": "..."}}, ...]
""",

    "hukuki_kavram": """
Türk hukuku fine-tuning dataseti için hukuki kavram açıklama çiftleri üret.

Konu: {source_text}

5 adet soru-cevap çifti üret:
- Kavramın tanımı, unsurları, diğer kavramlarla farkı
- Avukat üslubu, madde referansları
- JSON: [{{"user": "...", "assistant": "..."}}, ...]
""",

    "dilekce_uretimi": """
Türk hukuku fine-tuning dataseti için dilekçe üretim çifti üret.

Dava tipi: {source_text}

3 adet farklı senaryo için dilekçe taslağı üret.
Her birinde:
- "user": Dava bilgilerini içeren talimat
- "assistant": HMK uyumlu dilekçe taslağı (yer tutucular köşeli parantezle)
- JSON: [{{"user": "...", "assistant": "..."}}, ...]
""",

    "ret_sinir": """
Türk hukuk asistanı için ret/sınır örnekleri üret.

Konu: {source_text}

5 adet çift üret. Her birinde:
- "user": Asistanın yanıtlamaması gereken soru (tavsiye, alan dışı, riskli)
- "assistant": Nazik ret + bilgi notu + yönlendirme
- Ret asla kuru "yapamam" ile bitmemeli
- JSON: [{{"user": "...", "assistant": "..."}}, ...]
""",

    "karar_ozeti": """
Türk hukuku fine-tuning dataseti için mahkeme kararı özeti çiftleri üret.

Karar konusu / metni: {source_text}

3 adet soru-cevap çifti üret. Her birinde:
- "user": Bir Yargıtay/yerel mahkeme kararının özetlenmesini isteyen talimat (gerçekçi, kısa karar metni içerebilir)
- "assistant": Yapılandırılmış özet — Mahkeme, Esas/Karar, Uyuşmazlık konusu, Yerel mahkeme kararı, Yargıtay değerlendirmesi (maddeler), Sonuç (onama/bozma) ve Emsal niteliği başlıklarıyla
- Avukat üslubu, doğru daire ve madde referansları
- JSON: [{{"user": "...", "assistant": "..."}}, ...]
""",

    "belge_analizi": """
Türk hukuku fine-tuning dataseti için belge/sözleşme analizi çiftleri üret.

Belge türü / konu: {source_text}

3 adet soru-cevap çifti üret. Her birinde:
- "user": Bir sözleşme/belge metnini (kısa, gerçekçi alıntı) verip sorunlu maddelerin analizini isteyen talimat
- "assistant": Madde madde hukuki analiz — her sorunlu hüküm için ilgili kanun maddesi (TBK/TMK vb.) ve risk açıklaması, sonunda somut öneri
- Avukat üslubu, kaynaklı
- JSON: [{{"user": "...", "assistant": "..."}}, ...]
""",

    "cok_turlu_diyalog": """
Türk hukuku fine-tuning dataseti için ÇOK TURLU diyalog örnekleri üret.

Konu: {source_text}

2 adet diyalog üret. Her diyalog:
- En az 3 tur içermeli (3 user + 3 assistant), sırayla user/assistant
- Konu tutarlı kalmalı ama sorular doğal şekilde derinleşmeli
- Son cevaplar önceki konuşmaya açıkça atıfta bulunmalı ("Önceki soruda...", "Bahsettiğimiz gibi...")
- Avukat üslubu, madde referansları
- JSON formatı (dialog anahtarı zorunlu):
  [{{"dialog": [{{"role": "user", "content": "..."}}, {{"role": "assistant", "content": "..."}}, {{"role": "user", "content": "..."}}, {{"role": "assistant", "content": "..."}}, ...]}}, ...]
""",

    "dilekce_wizard": """
Türk hukuku fine-tuning dataseti için DİLEKÇE WIZARD akışı örnekleri üret.

Dava tipi: {source_text}

2 adet diyalog üret. Her diyalog şu akışı izlemeli:
- 1. tur user: Eksik bilgiyle dilekçe talebi (örn. "Boşanma dilekçesi yaz.")
- 1. tur assistant: Eksik bilgileri TEK seferde, numaralı liste hâlinde sorar (tek tek soru sormaz)
- 2. tur user: İstenen bilgileri verir
- 2. tur assistant: HMK uyumlu, eksiksiz dilekçe taslağı üretir (yer tutucular köşeli parantezle)
- Model eksik bilgiyle dilekçe ÜRETMEMELİ
- JSON formatı (dialog anahtarı zorunlu):
  [{{"dialog": [{{"role": "user", "content": "..."}}, {{"role": "assistant", "content": "..."}}, {{"role": "user", "content": "..."}}, {{"role": "assistant", "content": "..."}}]}}, ...]
""",
}

# Çok turlu çıktı üreten kategoriler (dialog formatı)
MULTI_TURN_CATEGORIES = {"cok_turlu_diyalog", "dilekce_wizard"}

# Kanun/madde referansı beklenmeyen kategoriler (validasyonda muaf)
NO_LAW_REF_CATEGORIES = {"ret_sinir", "dilekce_wizard"}

# ─────────────────────────────────────────────
# YARDIMCI FONKSİYONLAR
# ─────────────────────────────────────────────

def cprint(text: str, color: str = "white"):
    if COLOR:
        colors = {
            "green": Fore.GREEN,
            "red": Fore.RED,
            "yellow": Fore.YELLOW,
            "cyan": Fore.CYAN,
            "white": "",
        }
        print(f"{colors.get(color, '')}{text}")
    else:
        print(text)


def ensure_dirs():
    DATA_DIR.mkdir(exist_ok=True)
    RAW_DIR.mkdir(exist_ok=True)
    cprint(f"📁 Dizinler hazır: {DATA_DIR}", "green")


def load_pairs() -> list[dict]:
    if not PAIRS_FILE.exists():
        return []
    pairs = []
    with open(PAIRS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                pairs.append(json.loads(line))
    return pairs


def save_pair(pair: dict):
    """Tek bir çifti dosyaya ekle."""
    with open(PAIRS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(pair, ensure_ascii=False) + "\n")


def pair_signature(entry: dict) -> str:
    """Çiftin içerik imzası — tekilleştirme için (rol + normalize edilmiş metin)."""
    parts = []
    for m in entry.get("messages", []):
        if m.get("role") in ("user", "assistant"):
            normalized = " ".join(m.get("content", "").split()).lower()
            parts.append(f"{m['role']}:{normalized}")
    raw = "||".join(parts)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def load_signatures() -> set:
    """Mevcut tüm çiftlerin imzalarını döndür."""
    return {pair_signature(p) for p in load_pairs()}


def save_pair_if_new(entry: dict, seen: set) -> bool:
    """Çift yeni ise kaydet ve True döndür; kopya ise atla ve False döndür."""
    sig = pair_signature(entry)
    if sig in seen:
        return False
    save_pair(entry)
    seen.add(sig)
    return True


def detect_category(stem: str) -> Optional[str]:
    """Dosya adı kökünden kategori belirle.

    Kategori anahtarları alt çizgi içerdiği için (örn. 'kanun_maddesi'),
    bilinen kategorilerden en uzun önekle eşleşeni seçer.
    Örnek: 'kanun_maddesi_tbk49' → 'kanun_maddesi'.
    """
    matches = [cat for cat in CATEGORY_TARGETS if stem == cat or stem.startswith(cat + "_")]
    if not matches:
        return None
    return max(matches, key=len)


def build_entry(category: str, messages: list[dict], source: str = "manual") -> dict:
    """Standart format oluştur."""
    return {
        "id": f"{category}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
        "category": category,
        "source": source,
        "created_at": datetime.now().isoformat(),
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            *messages,
        ],
    }


# ─────────────────────────────────────────────
# OTOMATİK ÜRETİM (GPT-4o)
# ─────────────────────────────────────────────

def generate_pairs_from_text(category: str, source_text: str, client) -> list[dict]:
    """Kaynak metinden GPT-4o ile instruction pair üret."""
    if category not in GENERATION_PROMPTS:
        cprint(f"⚠️  '{category}' için üretim şablonu yok.", "yellow")
        return []

    prompt = GENERATION_PROMPTS[category].format(source_text=source_text[:3000])

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Türk hukuku fine-tuning dataseti üreticisisin. Sadece JSON döndür."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=3000,
        )
        raw = response.choices[0].message.content.strip()

        # JSON bloğunu çıkar
        json_match = re.search(r'\[.*\]', raw, re.DOTALL)
        if not json_match:
            cprint("⚠️  JSON bulunamadı, atlanıyor.", "yellow")
            return []

        pairs_raw = json.loads(json_match.group())
        entries = []
        for p in pairs_raw:
            messages = None
            if category in MULTI_TURN_CATEGORIES and isinstance(p.get("dialog"), list):
                # Çok turlu: dialog dizisini doğrula ve al
                turns = [
                    {"role": m["role"], "content": m["content"]}
                    for m in p["dialog"]
                    if isinstance(m, dict) and m.get("role") in ("user", "assistant") and m.get("content")
                ]
                if len(turns) >= 2:
                    messages = turns
            elif "user" in p and "assistant" in p:
                # Tekli soru-cevap
                messages = [
                    {"role": "user", "content": p["user"]},
                    {"role": "assistant", "content": p["assistant"]},
                ]

            if messages:
                entry = build_entry(
                    category=category,
                    messages=messages,
                    source="gpt4o_generated",
                )
                entries.append(entry)
        return entries

    except json.JSONDecodeError as e:
        cprint(f"❌ JSON parse hatası: {e}", "red")
        return []
    except Exception as e:
        cprint(f"❌ API hatası: {e}", "red")
        return []


def mode_generate():
    """Ham kaynak dosyalarından otomatik çift üret."""
    if not OPENAI_AVAILABLE:
        cprint("❌ openai paketi gerekli: pip install openai", "red")
        return

    if not OPENAI_API_KEY:
        cprint("❌ OPENAI_API_KEY ortam değişkeni ayarlanmamış.", "red")
        return

    ensure_dirs()
    client = OpenAI(api_key=OPENAI_API_KEY)

    # RAW klasöründeki .txt dosyalarını işle
    raw_files = list(RAW_DIR.glob("*.txt"))
    if not raw_files:
        cprint(f"⚠️  {RAW_DIR} klasöründe .txt dosyası bulunamadı.", "yellow")
        cprint("   Kaynak metinleri şu formatta kaydet: <kategori>_<başlık>.txt", "yellow")
        cprint("   Örnek: kanun_maddesi_tbk49.txt", "yellow")
        return

    seen = load_signatures()
    total_new = 0
    total_dup = 0
    for file_path in raw_files:
        # Dosya adından kategori belirle. Kategori anahtarları alt çizgi
        # içerdiğinden, bilinen en uzun önekle eşleştir.
        category = detect_category(file_path.stem)

        if category is None:
            cprint(f"⚠️  Bilinmeyen kategori, atlanıyor: {file_path.name}", "yellow")
            continue

        cprint(f"\n📄 İşleniyor: {file_path.name} → kategori: {category}", "cyan")
        source_text = file_path.read_text(encoding="utf-8")

        entries = generate_pairs_from_text(category, source_text, client)
        new_count = 0
        dup_count = 0
        for entry in entries:
            if save_pair_if_new(entry, seen):
                new_count += 1
            else:
                dup_count += 1
        total_new += new_count
        total_dup += dup_count
        msg = f"   ✅ {new_count} çift üretildi."
        if dup_count:
            msg += f" ({dup_count} kopya atlandı)"
        cprint(msg, "green")

    summary = f"\n🎉 Toplam {total_new} yeni çift eklendi."
    if total_dup:
        summary += f" {total_dup} kopya atlandı."
    cprint(summary, "green")


# ─────────────────────────────────────────────
# MANUEL EKLEME
# ─────────────────────────────────────────────

def mode_manual():
    """Komut satırından manuel çift ekle."""
    ensure_dirs()
    cprint("\n=== Manuel Veri Ekleme ===", "cyan")
    cprint("Çıkmak için 'q' yaz.\n", "white")

    # Kategori seç
    cprint("Kategoriler:", "yellow")
    cat_list = list(CATEGORY_LABELS.items())
    for i, (key, label) in enumerate(cat_list, 1):
        print(f"  {i}. {label}")

    while True:
        cat_input = input("\nKategori numarası: ").strip()
        if cat_input.lower() == "q":
            return
        try:
            idx = int(cat_input) - 1
            if 0 <= idx < len(cat_list):
                category = cat_list[idx][0]
                break
        except ValueError:
            pass
        cprint("Geçersiz seçim.", "red")

    # Çok turlu mu?
    multi = input("Çok turlu diyalog mu? (e/h): ").strip().lower() == "e"

    messages = []
    turn = 1
    while True:
        cprint(f"\n--- Tur {turn} ---", "cyan")
        user_msg = input("Kullanıcı mesajı (bitirmek için boş bırak): ").strip()
        if not user_msg:
            if messages:
                break
            cprint("En az bir tur gerekli.", "red")
            continue

        print("Asistan cevabı (bitirmek için tek satırda 'END' yaz):")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        assistant_msg = "\n".join(lines).strip()

        if not assistant_msg:
            cprint("Cevap boş olamaz.", "red")
            continue

        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
        turn += 1

        if not multi:
            break

        devam = input("\nBir tur daha ekle? (e/h): ").strip().lower()
        if devam != "e":
            break

    entry = build_entry(category=category, messages=messages, source="manual")
    if save_pair_if_new(entry, load_signatures()):
        cprint(f"\n✅ Çift kaydedildi (ID: {entry['id']})", "green")
    else:
        cprint("\n⚠️  Bu çift zaten mevcut (kopya), kaydedilmedi.", "yellow")


# ─────────────────────────────────────────────
# TOPLU JSON EKLEME
# ─────────────────────────────────────────────

def mode_import(json_file: str):
    """
    Hazır JSON dosyasından toplu çift aktar.

    Beklenen format (liste):
    [
      {
        "category": "kanun_maddesi",
        "user": "Soru metni",
        "assistant": "Cevap metni"
      },
      ...
    ]
    """
    ensure_dirs()
    path = Path(json_file)
    if not path.exists():
        cprint(f"❌ Dosya bulunamadı: {json_file}", "red")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        cprint("❌ Dosya bir JSON listesi olmalı.", "red")
        return

    seen = load_signatures()
    count = 0
    dup_count = 0
    for item in data:
        category = item.get("category", "kanun_maddesi")

        # Çok turlu içe aktarımı destekle: "dialog" veya "messages" anahtarı
        dialog = item.get("dialog") or item.get("messages")
        if isinstance(dialog, list):
            messages = [
                {"role": m["role"], "content": m["content"]}
                for m in dialog
                if isinstance(m, dict) and m.get("role") in ("user", "assistant") and m.get("content")
            ]
            if len(messages) < 2:
                continue
        else:
            user_msg = item.get("user", "").strip()
            assistant_msg = item.get("assistant", "").strip()
            if not user_msg or not assistant_msg:
                continue
            messages = [
                {"role": "user", "content": user_msg},
                {"role": "assistant", "content": assistant_msg},
            ]

        entry = build_entry(
            category=category,
            messages=messages,
            source=item.get("source", "imported"),
        )
        if save_pair_if_new(entry, seen):
            count += 1
        else:
            dup_count += 1

    msg = f"✅ {count} çift içe aktarıldı."
    if dup_count:
        msg += f" {dup_count} kopya atlandı."
    cprint(msg, "green")


# ─────────────────────────────────────────────
# VALİDASYON
# ─────────────────────────────────────────────

LAW_REF_KEYWORDS = ["m.", "madde", "Kanun", "TBK", "TMK", "HMK", "İİK", "TCK", "TTK", "4857", "6502"]

# Önceki konuşmaya atıf ifadeleri (çok turlu diyalog kalite kriteri)
CONTEXT_REF_PHRASES = ["önceki", "bahsettiğ", "konuştuğ", "yukarıda", "demiştik", "söylediğ", "az önce", "ilk soru"]


def _is_dry_refusal(text: str) -> bool:
    """Cevap kuru bir 'yapamam' ile mi bitiyor (çekim/noktalama toleranslı)."""
    cleaned = text.strip().lower().rstrip(".!… ")
    return cleaned.endswith("yapamam") or cleaned.endswith("yardımcı olamam") or cleaned.endswith("edemem")


def validate_pair(entry: dict) -> list[str]:
    """Bir çiftin kalite sorunlarını kategoriye duyarlı biçimde döndür."""
    issues = []
    category = entry.get("category", "")
    messages = entry.get("messages", [])
    assistant_msgs = [m["content"] for m in messages if m["role"] == "assistant"]
    user_msgs = [m["content"] for m in messages if m["role"] == "user"]

    if not assistant_msgs:
        issues.append("Asistan mesajı yok")
        return issues

    # Mesaj başına kontroller
    for assistant_text in assistant_msgs:
        if len(assistant_text) < 50:
            issues.append("Cevap 50 karakterden kısa")
        if _is_dry_refusal(assistant_text):
            issues.append("Cevap kuru ret ('yapamam' vb.) ile bitiyor")

    # Kanun referansı — sadece beklenen kategorilerde ve en az bir cevapta bulunmalı
    if category not in NO_LAW_REF_CATEGORIES:
        if not any(any(k in m for k in LAW_REF_KEYWORDS) for m in assistant_msgs):
            issues.append("Hiçbir cevap kanun/madde referansı içermiyor")

    # Çok turlu kategori kontrolleri
    if category in MULTI_TURN_CATEGORIES:
        min_turns = 3 if category == "cok_turlu_diyalog" else 2
        if len(assistant_msgs) < min_turns or len(user_msgs) < min_turns:
            issues.append(f"Çok turlu olmalı (en az {min_turns} tur gerekli)")

        # cok_turlu_diyalog: son cevap önceki konuşmaya atıf yapmalı
        if category == "cok_turlu_diyalog" and len(assistant_msgs) >= 2:
            last = assistant_msgs[-1].lower()
            if not any(p in last for p in CONTEXT_REF_PHRASES):
                issues.append("Son cevap önceki konuşmaya atıf yapmıyor")

        # dilekce_wizard: ilk cevap soru sormalı, eksik bilgiyle dilekçe üretmemeli
        if category == "dilekce_wizard" and assistant_msgs:
            if "?" not in assistant_msgs[0]:
                issues.append("Wizard ilk cevabı eksik bilgi sorusu içermiyor")

    # Aynı sorunu tekrar listeleme
    seen = set()
    unique_issues = []
    for i in issues:
        if i not in seen:
            seen.add(i)
            unique_issues.append(i)
    return unique_issues


def mode_validate():
    """Tüm çiftleri doğrula, sorunluları raporla."""
    pairs = load_pairs()
    if not pairs:
        cprint("Henüz veri yok.", "yellow")
        return

    issues_found = 0
    for pair in pairs:
        issues = validate_pair(pair)
        if issues:
            issues_found += 1
            cprint(f"\n⚠️  ID: {pair['id']}", "yellow")
            cprint(f"   Kategori: {pair['category']}", "white")
            for issue in issues:
                cprint(f"   ❌ {issue}", "red")

    if issues_found == 0:
        cprint(f"\n✅ {len(pairs)} çiftin tamamı geçti.", "green")
    else:
        cprint(f"\n📊 {len(pairs)} çiftten {issues_found} tanesi sorunlu.", "yellow")


# ─────────────────────────────────────────────
# İSTATİSTİK
# ─────────────────────────────────────────────

def mode_stats():
    """Kategori bazlı ilerleme istatistikleri."""
    pairs = load_pairs()

    counts = {cat: 0 for cat in CATEGORY_TARGETS}
    sources = {}
    for pair in pairs:
        cat = pair.get("category", "bilinmiyor")
        if cat in counts:
            counts[cat] += 1
        src = pair.get("source", "bilinmiyor")
        sources[src] = sources.get(src, 0) + 1

    cprint("\n=== AKAI Dataset İstatistikleri ===\n", "cyan")
    total = sum(counts.values())
    target_total = sum(CATEGORY_TARGETS.values())

    for cat, label in CATEGORY_LABELS.items():
        current = counts[cat]
        target = CATEGORY_TARGETS[cat]
        pct = (current / target * 100) if target > 0 else 0
        bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
        color = "green" if pct >= 100 else ("yellow" if pct >= 50 else "red")
        cprint(f"{label:<30} [{bar}] {current:>3}/{target} ({pct:.0f}%)", color)

    cprint(f"\nToplam: {total}/{target_total} ({total/target_total*100:.1f}%)", "cyan")

    cprint("\nKaynaklar:", "cyan")
    for src, cnt in sources.items():
        print(f"  {src}: {cnt}")


# ─────────────────────────────────────────────
# DIŞA AKTARIM
# ─────────────────────────────────────────────

def mode_export():
    """
    Fine-tuning için hazır JSONL üret.
    Her satır: {"messages": [...]} — OpenAI & HuggingFace TRL uyumlu.
    """
    pairs = load_pairs()
    if not pairs:
        cprint("Henüz veri yok.", "yellow")
        return

    with open(EXPORT_FILE, "w", encoding="utf-8") as f:
        for pair in pairs:
            export_entry = {"messages": pair["messages"]}
            f.write(json.dumps(export_entry, ensure_ascii=False) + "\n")

    cprint(f"✅ {len(pairs)} çift dışa aktarıldı: {EXPORT_FILE}", "green")
    cprint(f"   Dosya boyutu: {EXPORT_FILE.stat().st_size / 1024:.1f} KB", "white")

    # HuggingFace split önerisi
    val_count = max(1, int(len(pairs) * 0.1))
    train_count = len(pairs) - val_count
    cprint(f"\n   Önerilen split: train={train_count}, validation={val_count}", "cyan")


# ─────────────────────────────────────────────
# ANA PROGRAM
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="AKAI Fine-Tuning Dataset Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modlar:
  generate   Ham .txt dosyalarından GPT-4o ile otomatik üretim
  manual     Komut satırından manuel çift ekle
  import     JSON dosyasından toplu aktar (--file gerekli)
  validate   Tüm çiftleri doğrula
  stats      Kategori bazlı ilerleme göster
  export     Fine-tuning için JSONL çıktısı al

Örnekler:
  python akai_dataset_generator.py --mode stats
  python akai_dataset_generator.py --mode generate
  python akai_dataset_generator.py --mode import --file ornekler.json
  python akai_dataset_generator.py --mode export
        """,
    )
    parser.add_argument(
        "--mode",
        choices=["generate", "manual", "import", "validate", "stats", "export"],
        default="stats",
        help="Çalışma modu (varsayılan: stats)",
    )
    parser.add_argument(
        "--file",
        type=str,
        default="",
        help="import modu için JSON dosyası",
    )
    args = parser.parse_args()

    if args.mode == "generate":
        mode_generate()
    elif args.mode == "manual":
        mode_manual()
    elif args.mode == "import":
        if not args.file:
            cprint("❌ --file parametresi gerekli.", "red")
        else:
            mode_import(args.file)
    elif args.mode == "validate":
        mode_validate()
    elif args.mode == "stats":
        mode_stats()
    elif args.mode == "export":
        mode_export()


if __name__ == "__main__":
    main()
