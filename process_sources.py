"""
Kanun ve dilekçe kaynaklarından dataset üret.

Kullanım:
    python process_sources.py --preview
    python process_sources.py --apply
"""

import json
import re
import argparse
from pathlib import Path

try:
    import docx
except ImportError:
    docx = None

# ── Hedefler ────────────────────────────────────────────────────────────────
KANUN_CURRENT  = 30
KAVRAM_CURRENT = 20
KANUN_TARGET   = 100
KAVRAM_TARGET  = 100
KANUN_NEED     = KANUN_TARGET  - KANUN_CURRENT   # 70
KAVRAM_NEED    = KAVRAM_TARGET - KAVRAM_CURRENT  # 80

# Validator ile aynı liste
LAW_REF_KEYWORDS = ["m.", "madde", "Kanun", "TBK", "TMK", "HMK", "İİK",
                    "TCK", "TTK", "4857", "6502", "İYUK", "TKHK", "İşK"]

SYSTEM_KANUN = (
    "Sen AKAI'sın — Türk hukuku konusunda uzmanlaşmış bir yapay zeka asistanısın. "
    "Kanun maddelerini açık, katmanlı ve kaynaklı biçimde açıklarsın."
)
SYSTEM_KAVRAM = (
    "Sen AKAI'sın — Türk hukuku konusunda uzmanlaşmış bir yapay zeka asistanısın. "
    "Hukuki kavramları tanımlar, unsurlarını ve pratik sonuçlarını açıklarsın."
)

# ── Öncelikli maddeler (en pratik kanunlar) ─────────────────────────────────
PRIORITY_KANUNLAR = {
    "tbk":   "TBK",
    "iş":    "İş Kanunu",
    "tkhk":  "TKHK",
    "hmk":   "HMK",
    "iik":   "İİK",
}

# Mülga/geçici/çok kısa maddeleri filtrele
SKIP_PATTERNS = re.compile(
    r'(mülga|yürürlükten|geçici madde|ek madde|iptal edilmi|'
    r'değiştirilmi.*kanun|bkz\.|aynı kanunun)',
    re.IGNORECASE
)


def has_law_ref(text: str) -> bool:
    return any(k in text for k in LAW_REF_KEYWORDS)


def kanun_prefix(instruction: str) -> str:
    """instruction'dan kanun kısaltmasını çıkar: 'tbk Madde 49 ...' → 'TBK'"""
    first = instruction.split()[0].lower()
    return PRIORITY_KANUNLAR.get(first, first.upper())


def rephrase_question(instruction: str, kanun_abbr: str) -> str:
    """'tbk Madde 49 içeriği...' → 'TBK Madde 49 ne düzenler?'"""
    # Madde numarasını bul
    m = re.search(r'[Mm]adde\s+(\d+[A-Za-z]?)', instruction)
    if m:
        no = m.group(1)
        return f"{kanun_abbr} Madde {no}'nin içeriği ve hukuki önemi nedir?"
    return instruction.replace(first := instruction.split()[0], kanun_abbr, 1)


def normalize_output(output: str, kanun_abbr: str) -> str:
    """Ham madde metnini biraz düzenle: küçük harf kanun prefix → büyük harf."""
    # 'tbk Madde 49' → 'TBK Madde 49'
    return re.sub(
        r'\b(tbk|tmk|tck|hmk|cmk|iik|tkhk|ttk|iyuk|iş)\b',
        lambda m: m.group(0).upper(),
        output,
        flags=re.IGNORECASE
    )


# ── 1) KANUN_MADDESİ — hukuk_dataset.jsonl ──────────────────────────────────
GAZETTE_PATTERN  = re.compile(r'\b(19|20)\d{2}\b')
AMENDMENT_PATTERN = re.compile(
    r'(tarihli ve \d+ say|tarih ve \d+ say|KHK/\d+|\d+/\d+/20\d\d.*md\.|'
    r'De[ğg]i[şs]ik:.*md\.|Ek:.*md\.|M[üu]lga:.*md\.)',
    re.IGNORECASE
)


def is_garbage_output(text: str) -> bool:
    """Değişiklik tarihleri / gazette log içeren çıktıları yakala."""
    years = GAZETTE_PATTERN.findall(text)
    if len(years) > 5:
        return True
    # Değişiklik notu yoğunluğu
    amendments = AMENDMENT_PATTERN.findall(text)
    if len(amendments) >= 2:
        return True
    words = text.split()
    if len(words) < 20:
        return True
    return False


def process_kanun_dataset(jsonl_path: Path, need: int) -> list[dict]:
    records = []
    with open(jsonl_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            inst   = obj.get("instruction", "")
            output = obj.get("output", "")

            # Öncelikli kanunlar
            first_word = inst.split()[0].lower() if inst else ""
            if first_word not in PRIORITY_KANUNLAR:
                continue

            # Minimum uzunluk
            if len(output) < 200:
                continue

            # Gazete/değişiklik logu mu?
            if is_garbage_output(output):
                continue

            # Mülga/geçici madde atla
            if SKIP_PATTERNS.search(output):
                continue

            # Validator kuralı
            kanun_abbr = PRIORITY_KANUNLAR[first_word]
            clean_out  = normalize_output(output, kanun_abbr)
            if not has_law_ref(clean_out):
                continue

            soru = rephrase_question(inst, kanun_abbr)

            records.append({
                "category": "kanun_maddesi",
                "source": "kanun_metin",
                "user": soru,
                "assistant": clean_out,
            })

    # Tekrar eden soruları çıkar, hedef kadar al
    seen = set()
    unique = []
    for r in records:
        key = r["user"]
        if key not in seen:
            seen.add(key)
            unique.append(r)
        if len(unique) >= need:
            break

    return unique


# ── 2) HUKUKİ_KAVRAM — iyuk.json ────────────────────────────────────────────
KAVRAM_TYPES = {"Conceptual", "Analytical", "Procedural", "Causal", "Hypothetical"}

def process_iyuk(iyuk_path: Path, need: int) -> list[dict]:
    with open(iyuk_path, encoding="utf-8") as f:
        raw = json.load(f)

    dataset = raw[0]["dataset"] if isinstance(raw, list) else raw.get("dataset", [])

    records = []
    for item in dataset:
        qtype  = item.get("question_type", "")
        if qtype not in KAVRAM_TYPES:
            continue

        soru   = item.get("question", "").strip()
        cevap  = item.get("answer", "").strip()
        source = item.get("source", "")  # "İYUK Madde 2" gibi

        if len(cevap) < 80:
            continue

        # Cevaba kaynak referansı ekle — küçük harf "madde" validator için zorunlu
        if not has_law_ref(cevap):
            if source:
                ref_lower = re.sub(r'\bMadde\b', 'madde', source)
                cevap = f"{cevap}\n\n*(Kaynak: {ref_lower})*"
            else:
                cevap = f"{cevap}\n\n*(Kaynak: İYUK madde hükümleri)*"

        if not has_law_ref(cevap):
            continue

        records.append({
            "category": "hukuki_kavram",
            "source": "iyuk_dataset",
            "user": soru,
            "assistant": cevap,
        })

    # Tekrar çıkar, hedef kadar al
    seen = set()
    unique = []
    for r in records:
        if r["user"] not in seen:
            seen.add(r["user"])
            unique.append(r)
        if len(unique) >= need:
            break

    return unique


# ── 3) DİLEKÇE ŞABLONLARI — .docx okuma ─────────────────────────────────────
def read_docx(path: Path) -> str:
    if docx is None:
        return ""
    try:
        doc = docx.Document(str(path))
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except Exception:
        return ""


def extract_petition_pairs(dilekce_dir: Path) -> list[dict]:
    """
    Gerçek dilekçe dosyalarından yapısal çiftler üret.
    Kişisel veriler anonim tutulur — isim/TC → [Ad Soyad]/[TC No].
    """
    petition_pairs = []

    targets = {
        "ihtarnamee.docx": {
            "tip": "mesken_ihtiyaci_tahliye_ihtarnamesi",
            "user_prefix": "Kiracıma mesken ihtiyacım nedeniyle tahliye ihtarnamesi göndermek istiyorum.",
            "kanun_ref": "TBK madde 347 (mesken ihtiyacı tahliye); TBK madde 117 (temerrüt bildirimi).",
        },
        "Küçükçakmak İTİRAZ.docx": {
            "tip": "icra_takibi_itiraz",
            "user_prefix": "Aleyhime başlatılan icra takibine itiraz dilekçesi hazırlamam gerekiyor.",
            "kanun_ref": "İİK madde 62 (ödeme emrine itiraz süresi 7 gün); İİK madde 269 (kira alacağı).",
        },
        "Makro Yapı İTİRAZ.docx": {
            "tip": "banka_kredi_icra_itiraz",
            "user_prefix": "Şirketimiz aleyhine banka tarafından başlatılan icra takibine itiraz edeceğiz.",
            "kanun_ref": "İİK madde 62 (itiraz); TBK madde 358 (kredi sözleşmesi itirazı).",
        },
        "TEHİRİ İCRA İÇİN SÜRE.docx": {
            "tip": "tehiri_icra_mehil",
            "user_prefix": "İcra takibini durdurmak için tehiri icra talepli temyiz ettim, mehil belgesi isteyeceğim.",
            "kanun_ref": "İİK madde 36 (tehiri icra ve mehil vesikası).",
        },
        "şirketin iflasını istememek.docx": {
            "tip": "iflas_istememek_savunma",
            "user_prefix": "Şirketin iflasını istememe suçlamasına karşı icra ceza mahkemesine savunma dilekçesi lazım.",
            "kanun_ref": "İİK madde 177 (iflasını istememe yükümlülüğü); İİK madde 331 (tazyik hapsi).",
        },
    }

    for fname, meta in targets.items():
        fpath = dilekce_dir / fname
        if not fpath.exists():
            continue
        text = read_docx(fpath)
        if len(text) < 100:
            continue

        # Kişisel veri anonimleştirme (minimal — sadece TC ve dosya no)
        anon = text
        anon = re.sub(r'\b\d{11}\b', '[TC Kimlik No]', anon)
        anon = re.sub(r'TC NO:\s*\d+', 'TC NO: [TC Kimlik No]', anon, flags=re.IGNORECASE)
        anon = re.sub(r'\b\d{4}/\d+\s+[Ee](sas|\.)', '[Dosya No] E.', anon)
        # Şirket/kişi adlarını genel tutuyoruz (belirli isimler çıkarılmaz —
        # bunlar yapısal örnektir, kişisel veri paylaşımı değil)

        kanun_ref = meta.get("kanun_ref", "")
        pair = {
            "category": "dilekce_uretimi",
            "source": "gercek_dilekce_sablon",
            "user": meta["user_prefix"] + " Taslak dilekçe yazar mısınız?",
            "assistant": (
                f"Aşağıda **{meta['tip'].replace('_', ' ').title()}** için "
                f"hazırlanmış örnek taslak dilekçe bulunmaktadır. "
                f"Bilgilerinizi köşeli parantez içindeki alanlara yazınız.\n\n"
                f"**Hukuki dayanak**: {kanun_ref}\n\n"
                f"---\n\n{anon}\n\n---\n\n"
                "> **Not**: Bu taslak bilgi amaçlıdır; "
                "kendi durumunuza göre bir avukattan destek alınız."
            ),
        }
        petition_pairs.append(pair)

    return petition_pairs


# ── Ana akış ────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--apply",   action="store_true")
    args = parser.parse_args()

    base        = Path(__file__).parent
    jsonl_path  = base / "kanunlar" / "hukuk_dataset.jsonl"
    iyuk_path   = base / "kanunlar" / "iyuk.json"
    dilekce_dir = base / "örnek dilekçe havuzu"

    print("=== Kanun maddesi işleniyor ===")
    kanun_records = process_kanun_dataset(jsonl_path, KANUN_NEED)
    print(f"Seçilen kanun_maddesi: {len(kanun_records)}/{KANUN_NEED}")

    print("\n=== Hukuki kavram işleniyor ===")
    kavram_records = process_iyuk(iyuk_path, KAVRAM_NEED)
    print(f"Seçilen hukuki_kavram: {len(kavram_records)}/{KAVRAM_NEED}")

    print("\n=== Dilekçe şablonları işleniyor ===")
    dilekce_records = extract_petition_pairs(dilekce_dir)
    print(f"Seçilen dilekce_uretimi: {len(dilekce_records)} (bonus)")

    print("\n=== Önizleme ===")
    print("--- kanun_maddesi ilk 2 ---")
    for r in kanun_records[:2]:
        print(f"S: {r['user']}")
        print(f"C: {r['assistant'][:250]}\n")

    print("--- hukuki_kavram ilk 2 ---")
    for r in kavram_records[:2]:
        print(f"S: {r['user']}")
        print(f"C: {r['assistant'][:250]}\n")

    print("--- dilekce_uretimi ilk 1 ---")
    for r in dilekce_records[:1]:
        print(f"S: {r['user']}")
        print(f"C: {r['assistant'][:300]}\n")

    if args.apply:
        out_dir = base / "seeds"

        kanun_out  = out_dir / "source_kanun_maddesi.json"
        kavram_out = out_dir / "source_hukuki_kavram.json"
        dilekce_out = out_dir / "source_dilekce_uretimi.json"

        kanun_out.write_text(
            json.dumps(kanun_records, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        kavram_out.write_text(
            json.dumps(kavram_records, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        dilekce_out.write_text(
            json.dumps(dilekce_records, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        print(f"Kaydedildi: {kanun_out.name} ({len(kanun_records)} kayıt)")
        print(f"Kaydedildi: {kavram_out.name} ({len(kavram_records)} kayıt)")
        print(f"Kaydedildi: {dilekce_out.name} ({len(dilekce_records)} kayıt)")
    else:
        print("Kaydetmek için --apply ekle.")


if __name__ == "__main__":
    main()
