"""
Kaggle Turkish Law Dataset → AKAI format dönüştürücü

Kullanım:
    1. Kaggle'dan indirilen CSV'yi proje klasörüne koy
    2. python kaggle_import.py --file <dosya_adı.csv> --preview
    3. Beğenirsen: python kaggle_import.py --file <dosya_adı.csv> --apply
"""

import json
import re
import argparse
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("pandas gerekli: pip install pandas")
    sys.exit(1)

# ── Ayarlar ────────────────────────────────────────────────────────────────
KANUN_TARGET   = 75   # kanun_maddesi hedef toplam
KAVRAM_TARGET  = 75   # hukuki_kavram hedef toplam
KANUN_CURRENT  = 30   # mevcut kanun_maddesi sayısı
KAVRAM_CURRENT = 20   # mevcut hukuki_kavram sayısı
MIN_SCORE      = 7    # minimum kalite skoru
MIN_ANSWER_LEN = 100  # minimum cevap uzunluğu (karakter)
MAX_ANSWER_LEN = 2000 # maksimum cevap uzunluğu

# Validator ile birebir aynı anahtar kelimeler (akai_dataset_generator.py LAW_REF_KEYWORDS)
LAW_REF_KEYWORDS = ["m.", "madde", "Kanun", "TBK", "TMK", "HMK", "İİK", "TCK", "TTK", "4857", "6502"]


def has_law_ref(text: str) -> bool:
    return any(k in text for k in LAW_REF_KEYWORDS)
# ───────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT_KANUN = (
    "Sen AKAI'sın — Türk hukuku konusunda uzmanlaşmış bir yapay zeka asistanısın. "
    "Kanun maddelerini açık, katmanlı ve kaynaklı biçimde açıklarsın."
)

SYSTEM_PROMPT_KAVRAM = (
    "Sen AKAI'sın — Türk hukuku konusunda uzmanlaşmış bir yapay zeka asistanısın. "
    "Hukuki kavramları tanımlar, unsurlarını ve pratik sonuçlarını açıklarsın."
)

# Kanun maddesi tespiti için anahtar kelimeler
KANUN_KEYWORDS = [
    r'\bm\.\s*\d+', r'\bmadde\s+\d+', r'\bfıkra\b', r'\bbent\b',
    r'\bkanun\b', r'\btck\b', r'\btmk\b', r'\bhmk\b', r'\btbk\b',
    r'\biyk\b', r'\bikk\b', r'\bkmk\b', r'\bktk\b',
    r'\banayasa\b', r'\byönetmelik\b', r'\btüzük\b',
]

# Kavram tespiti için anahtar kelimeler
KAVRAM_KEYWORDS = [
    r'\bnedir\b', r'\bne demek\b', r'\btanım\b', r'\bkavram\b',
    r'\bilke\b', r'\bprensip\b', r'\bteori\b', r'\bdoktr[iı]n\b',
    r'\bfark\b', r'\baras[iı]ndaki\b', r'\bunsur\b', r'\bşart\b',
    r'\bsayılır\b', r'\bsayılma\b',
]


def classify(soru: str, cevap: str) -> str | None:
    """Satırı kanun_maddesi veya hukuki_kavram olarak sınıflandır."""
    soru_lower = soru.lower()
    cevap_lower = cevap.lower()

    kanun_score = sum(
        1 for kw in KANUN_KEYWORDS
        if re.search(kw, soru_lower) or re.search(kw, cevap_lower)
    )
    kavram_score = sum(
        1 for kw in KAVRAM_KEYWORDS
        if re.search(kw, soru_lower)
    )

    if kanun_score >= 2:
        return "kanun_maddesi"
    if kavram_score >= 2:
        return "hukuki_kavram"
    if kanun_score == 1 and kavram_score == 0:
        return "kanun_maddesi"
    if kavram_score == 1 and kanun_score == 0:
        return "hukuki_kavram"
    return None


def clean_text(text: str) -> str:
    """Metni temizle."""
    text = str(text).strip()
    text = re.sub(r'\s+', ' ', text)
    return text


def to_messages(soru: str, cevap: str, category: str) -> dict:
    """AKAI messages formatına dönüştür."""
    system = SYSTEM_PROMPT_KANUN if category == "kanun_maddesi" else SYSTEM_PROMPT_KAVRAM
    return {
        "messages": [
            {"role": "system",  "content": system},
            {"role": "user",    "content": soru},
            {"role": "assistant","content": cevap},
        ]
    }


def to_import_format(soru: str, cevap: str, category: str) -> dict:
    """Seed import formatına dönüştür."""
    return {
        "category": category,
        "source": "kaggle_turkish_law",
        "user": soru,
        "assistant": cevap,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Kaggle CSV dosya adı")
    parser.add_argument("--preview", action="store_true", help="Sadece önizle, kaydetme")
    parser.add_argument("--apply",   action="store_true", help="Import JSON dosyaları oluştur")
    args = parser.parse_args()

    csv_path = Path(args.file)
    if not csv_path.exists():
        print(f"Dosya bulunamadı: {csv_path}")
        sys.exit(1)

    print(f"CSV yükleniyor: {csv_path}")
    df = pd.read_csv(csv_path, encoding="utf-8")
    print(f"Toplam satır: {len(df)}")
    print(f"Kolonlar: {list(df.columns)}\n")

    # Kolon isimlerini normalize et
    col_map = {}
    for col in df.columns:
        c = col.lower().strip()
        if c in ("soru", "question"):
            col_map["soru"] = col
        elif c in ("cevap", "answer"):
            col_map["cevap"] = col
        elif c in ("score", "skor", "puan"):
            col_map["score"] = col

    if "soru" not in col_map or "cevap" not in col_map:
        print(f"Kolon eşlemesi başarısız. Bulunan kolonlar: {list(df.columns)}")
        sys.exit(1)

    # Filtrele
    df["_soru"] = df[col_map["soru"]].apply(clean_text)
    df["_cevap"] = df[col_map["cevap"]].apply(clean_text)

    # Skor filtresi
    if "score" in col_map:
        df["_score"] = pd.to_numeric(df[col_map["score"]], errors="coerce").fillna(0)
        df = df[df["_score"] >= MIN_SCORE]
        print(f"Skor >= {MIN_SCORE} filtresi sonrası: {len(df)} satır")

    # Uzunluk filtresi
    df = df[df["_cevap"].str.len().between(MIN_ANSWER_LEN, MAX_ANSWER_LEN)]
    df = df[df["_soru"].str.len() >= 20]
    print(f"Uzunluk filtresi sonrası: {len(df)} satır")

    # Sınıflandır
    df["_category"] = df.apply(
        lambda r: classify(r["_soru"], r["_cevap"]), axis=1
    )
    df = df[df["_category"].notna()]
    print(f"Sınıflandırılabilir: {len(df)} satır\n")

    kanun_need  = KANUN_TARGET  - KANUN_CURRENT
    kavram_need = KAVRAM_TARGET - KAVRAM_CURRENT

    # kanun_maddesi: validator ile aynı kural — cevabın LAW_REF_KEYWORDS içermesi zorunlu
    kanun_pool = df[df["_category"] == "kanun_maddesi"]
    kanun_pool = kanun_pool[kanun_pool["_cevap"].apply(has_law_ref)]
    kanun_df = kanun_pool.drop_duplicates("_soru").head(kanun_need)

    # hukuki_kavram: aynı kural
    kavram_pool = df[df["_category"] == "hukuki_kavram"]
    kavram_pool = kavram_pool[kavram_pool["_cevap"].apply(has_law_ref)]
    kavram_df = kavram_pool.drop_duplicates("_soru").head(kavram_need)

    print(f"Seçilen kanun_maddesi : {len(kanun_df)}/{kanun_need} (hedef +{kanun_need})")
    print(f"Seçilen hukuki_kavram : {len(kavram_df)}/{kavram_need} (hedef +{kavram_need})\n")

    # Önizleme
    print("=== KANUN_MADDESİ — İlk 3 örnek ===")
    for _, row in kanun_df.head(3).iterrows():
        print(f"S: {row['_soru'][:120]}")
        print(f"C: {row['_cevap'][:200]}")
        print()

    print("=== HUKUKİ_KAVRAM — İlk 3 örnek ===")
    for _, row in kavram_df.head(3).iterrows():
        print(f"S: {row['_soru'][:120]}")
        print(f"C: {row['_cevap'][:200]}")
        print()

    if args.apply:
        # Import JSON dosyaları oluştur
        kanun_records = [
            to_import_format(r["_soru"], r["_cevap"], "kanun_maddesi")
            for _, r in kanun_df.iterrows()
        ]
        kavram_records = [
            to_import_format(r["_soru"], r["_cevap"], "hukuki_kavram")
            for _, r in kavram_df.iterrows()
        ]

        kanun_out = Path("seeds/kaggle_kanun_maddesi.json")
        kavram_out = Path("seeds/kaggle_hukuki_kavram.json")

        kanun_out.write_text(
            json.dumps(kanun_records, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        kavram_out.write_text(
            json.dumps(kavram_records, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        print(f"Kaydedildi: {kanun_out} ({len(kanun_records)} çift)")
        print(f"Kaydedildi: {kavram_out} ({len(kavram_records)} çift)")
        print()
        print("Şimdi şunu çalıştır:")
        print(f"  python akai_dataset_generator.py --mode import --file {kanun_out}")
        print(f"  python akai_dataset_generator.py --mode import --file {kavram_out}")
        print("  python akai_dataset_generator.py --mode validate")
        print("  python akai_dataset_generator.py --mode export")
    else:
        print("Önizleme modu — kaydetmek için --apply ekle")


if __name__ == "__main__":
    main()
