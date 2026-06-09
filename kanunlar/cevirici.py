import fitz
import json
import os
import re

pdf_klasoru = os.path.dirname(os.path.abspath(__file__))
cikti_dosyasi = "hukuk_dataset.jsonl"

def donustur():
    dataset = []
    dosyalar = [f for f in os.listdir(pdf_klasoru) if f.endswith('.pdf')]
    
    # regex: "Madde [Sayı]" ile başlayan ve bir sonraki "Madde [Sayı]"ya kadar her şeyi alan desen
    # Bu desen fıkraları (1), (2) ve bentleri a), b) asla bölmez, bütün tutar.
    madde_bulucu = re.compile(r'(Madde\s+\d+[\s\S]*?)(?=Madde\s+\d+|$)', re.IGNORECASE)

    for dosya_adi in dosyalar:
        kanun_adi = dosya_adi.replace(".pdf", "").replace("_", " ")
        yol = os.path.join(pdf_klasoru, dosya_adi)
        
        doc = fitz.open(yol)
        print(f"İşleniyor: {kanun_adi}")
        
        # Tüm PDF metnini birleştiriyoruz ki sayfa geçişlerindeki maddeler bölünmesin
        full_text = ""
        for sayfa in doc:
            full_text += sayfa.get_text()

        # Gereksiz sayfa numaralarını ve alt bilgileri temizlemek için basit bir temizlik
        # (PDF yapısına göre gerekirse eklenebilir)
        
        bulunan_maddeler = madde_bulucu.findall(full_text)
        
        for m in bulunan_maddeler:
            # Temizlik: Fazla boşlukları ve satır sonlarını düzenle
            temiz_metin = re.sub(r'\s+', ' ', m).strip()
            
            # FİLTRE: Eğer metin çok kısaysa (Tablodur) alma
            if len(temiz_metin) < 150: 
                continue
                
            # Madde numarasını tespit et (Örn: Madde 101)
            no_match = re.search(r'Madde\s+\d+', temiz_metin)
            madde_no = no_match.group(0) if no_match else "İlgili Madde"

            entry = {
                "instruction": f"{kanun_adi} {madde_no} içeriği ve fıkraları nelerdir?",
                "input": "",
                "output": f"{kanun_adi} {temiz_metin}"
            }
            dataset.append(entry)

    with open(os.path.join(pdf_klasoru, cikti_dosyasi), "w", encoding="utf-8") as f:
        for item in dataset:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    
    print(f"Bitti! {len(dataset)} adet kompleks madde başarıyla işlendi.")

if __name__ == "__main__":
    donustur()