"""
Seed — Kategori 1: Kanun Maddesi Açıklama
=========================================
Rehbere uygun, avukat üslubunda, kaynaklı soru-cevap çiftleri.
Bu betik düzenlenebilir Python kaynağıdır; çalıştırınca import için
hazır bir JSON dosyası üretir:

    python seeds/seed_kanun_maddesi.py
    python akai_dataset_generator.py --mode import --file seeds/seed_kanun_maddesi.json

Yeni çift eklemek için PAIRS listesine (user, assistant) ikilisi ekle.
"""

import json
from pathlib import Path

CATEGORY = "kanun_maddesi"
SOURCE = "claude_seed"
OUT_FILE = Path(__file__).with_name("seed_kanun_maddesi.json")

# (user, assistant) ikilileri
PAIRS = [
    (
        "TMK madde 2 neyi düzenler?",
        "Türk Medeni Kanunu'nun 2. maddesi, tüm özel hukuk ilişkilerine yön veren "
        "dürüstlük (objektif iyiniyet) kuralını düzenler.\n\n"
        "Madde metni: \"Herkes, haklarını kullanırken ve borçlarını yerine getirirken "
        "dürüstlük kurallarına uymak zorundadır. Bir hakkın açıkça kötüye kullanılmasını "
        "hukuk düzeni korumaz.\"\n\n"
        "**İki temel ilke içerir:**\n"
        "- **Dürüstlük kuralı (md. 2/1):** Tarafların ilişkilerinde orta zekâlı, dürüst bir "
        "kişiden beklenen davranışı göstermesini gerektirir.\n"
        "- **Hakkın kötüye kullanılması yasağı (md. 2/2):** Bir hak biçimsel olarak var olsa "
        "bile, açıkça kötüye kullanılıyorsa hukuken korunmaz.\n\n"
        "Bu madde hâkim tarafından re'sen dikkate alınır ve sözleşmeyle bertaraf edilemez. "
        "Yargıtay, özellikle kira, iş ve aile hukukunda bu maddeyi sıkça uygulamaktadır.",
    ),
    (
        "İspat yükü kime aittir, hangi maddede düzenlenir?",
        "İspat yükünün dağılımı Türk Medeni Kanunu'nun 6. maddesinde düzenlenir.\n\n"
        "Madde metni: \"Kanunda aksine bir hüküm bulunmadıkça, taraflardan her biri, hakkını "
        "dayandırdığı olguların varlığını ispatla yükümlüdür.\"\n\n"
        "**Temel kural:** Bir olguyu iddia eden değil, o olgudan kendi lehine hak çıkaran taraf "
        "ispatla yükümlüdür. Örneğin alacaklı alacağın doğduğunu, borçlu ise borcun ödendiğini "
        "(ifa) ispatlamak zorundadır.\n\n"
        "**İstisnalar:** Kanunda yer alan karinelerle ispat yükü yer değiştirebilir. Örneğin "
        "TBK m.112 uyarınca borçlu, borca aykırılıkta kusursuzluğunu kendisi ispatlar. "
        "Usul hukuku boyutu HMK m.190'da ayrıca düzenlenmiştir.",
    ),
    (
        "TMK 166 boşanma sebebini açıklar mısın?",
        "Türk Medeni Kanunu'nun 166. maddesi, uygulamada en sık dayanılan boşanma sebebi olan "
        "\"evlilik birliğinin temelinden sarsılması\"nı (şiddetli geçimsizlik) düzenler.\n\n"
        "Madde metni (1. fıkra): \"Evlilik birliği, ortak hayatı sürdürmeleri kendilerinden "
        "beklenmeyecek derecede temelinden sarsılmış olursa, eşlerden her biri boşanma davası "
        "açabilir.\"\n\n"
        "**Önemli noktalar:**\n"
        "- Bu genel ve nispi bir boşanma sebebidir; hâkim ortak hayatın çekilmez hâle gelip "
        "gelmediğini somut olaya göre takdir eder.\n"
        "- Md. 166/2: Davacının kusuru daha ağırsa, davalı boşanmaya itiraz edebilir; ancak "
        "bu itiraz hakkın kötüye kullanılması niteliğindeyse ve evlilik birliğinin devamında "
        "korunmaya değer bir yarar kalmamışsa hâkim yine de boşanmaya karar verebilir.\n"
        "- Md. 166/3 anlaşmalı boşanmayı düzenler: En az 1 yıl süren evlilikte, eşlerin birlikte "
        "başvurması veya birinin davasını diğerinin kabul etmesi ve hâkimin tarafları bizzat "
        "dinlemesi gerekir.\n\n"
        "Yargıtay 2. Hukuk Dairesi uygulamasında, kusur dağılımı tazminat ve nafaka taleplerini "
        "doğrudan etkiler.",
    ),
    (
        "Yoksulluk nafakası nedir, dayanağı hangi maddedir?",
        "Yoksulluk nafakası, Türk Medeni Kanunu'nun 175. maddesinde düzenlenir.\n\n"
        "Madde metni: \"Boşanma yüzünden yoksulluğa düşecek taraf, kusuru daha ağır olmamak "
        "koşuluyla geçimi için diğer taraftan malî gücü oranında süresiz olarak nafaka "
        "isteyebilir. Nafaka yükümlüsünün kusuru aranmaz.\"\n\n"
        "**Şartları:**\n"
        "- Boşanma nedeniyle **yoksulluğa düşmek**,\n"
        "- Talep eden eşin kusurunun diğerinden **daha ağır olmaması**,\n"
        "- Nafaka yükümlüsünün kusuru aranmaz; mali gücüyle orantılı belirlenir.\n\n"
        "**İştirak nafakasından farkı:** Yoksulluk nafakası eş lehinedir; iştirak nafakası "
        "(TMK m.182) ise müşterek çocuğun bakım giderleri içindir. Yoksulluk nafakası kural "
        "olarak süresizdir, ancak nafaka alanın yeniden evlenmesi veya yoksulluğun ortadan "
        "kalkması hâlinde kaldırılabilir (TMK m.176).",
    ),
    (
        "TBK madde 112 borca aykırılıkta sorumluluğu nasıl düzenler?",
        "Türk Borçlar Kanunu'nun 112. maddesi, borcun ifa edilmemesinden doğan sorumluluğun "
        "genel hükmüdür.\n\n"
        "Madde metni: \"Borç hiç veya gereği gibi ifa edilmezse borçlu, kendisine hiçbir kusurun "
        "yüklenemeyeceğini ispat etmedikçe, alacaklının bundan doğan zararını gidermekle "
        "yükümlüdür.\"\n\n"
        "**Öne çıkan unsurlar:**\n"
        "- **Kusur karinesi:** Borca aykırılık hâlinde borçlunun kusurlu olduğu varsayılır; "
        "kusursuzluğunu **borçlu** ispatlamak zorundadır (ispat yükü borçludadır).\n"
        "- Sorumluluk hem hiç ifa etmemeyi hem de eksik/ayıplı ifayı kapsar.\n"
        "- Tazminat, alacaklının uğradığı **müspet zararı** (ifadan beklenen yarar) karşılar.\n\n"
        "Bu madde, haksız fiil sorumluluğunu düzenleyen TBK m.49'dan farklı olarak, taraflar "
        "arasında önceden var olan bir borç ilişkisini (sözleşme) gerektirir.",
    ),
    (
        "Borçlu temerrüdü ne zaman oluşur? TBK 117.",
        "Borçlu temerrüdü, Türk Borçlar Kanunu'nun 117. maddesinde düzenlenir.\n\n"
        "Madde metni (1. fıkra): \"Muaccel bir borcun borçlusu, alacaklının ihtarıyla temerrüde "
        "düşer.\"\n\n"
        "**Temerrüdün şartları:**\n"
        "- Borç **muaccel** (vadesi gelmiş) olmalı,\n"
        "- Kural olarak alacaklının **ihtarı** gerekir.\n\n"
        "**İhtarın gerekmediği hâller (md. 117/2):**\n"
        "- İfa gününün taraflarca birlikte belirlenmiş olması (kesin vade),\n"
        "- Borcun, belirlenmiş bir sürenin geçmesiyle muaccel olacağının kararlaştırılması.\n\n"
        "**Sonuçları:** Temerrüde düşen borçlu, gecikme faizi (TBK m.120) ve kusursuz olduğunu "
        "ispatlayamadığı sürece gecikmeden doğan zararı öder; para borçlarında ayrıca aşkın "
        "zarar (TBK m.122) talep edilebilir.",
    ),
    (
        "Türk Borçlar Kanunu'nda genel zamanaşımı süresi kaç yıldır?",
        "Genel zamanaşımı süresi, Türk Borçlar Kanunu'nun 146. maddesinde düzenlenir.\n\n"
        "Madde metni: \"Kanunda aksine bir hüküm bulunmadıkça, her alacak on yıllık zamanaşımına "
        "tabidir.\"\n\n"
        "**Açıklama:** On yıllık süre genel/tamamlayıcı niteliktedir; yalnızca özel bir süre "
        "öngörülmeyen alacaklara uygulanır.\n\n"
        "**Sık karşılaşılan özel süreler:**\n"
        "- Kira bedeli, faiz ve dönemsel edimler: **5 yıl** (TBK m.147),\n"
        "- Haksız fiilden doğan tazminat: zararın ve failin öğrenilmesinden itibaren **2 yıl**, "
        "her hâlde fiil tarihinden itibaren **10 yıl** (TBK m.72).\n\n"
        "Zamanaşımı hâkim tarafından re'sen dikkate alınmaz; borçlunun defi olarak ileri sürmesi "
        "gerekir (TBK m.161).",
    ),
    (
        "Kira sözleşmesinin tanımı kanunda nasıl yapılmış?",
        "Kira sözleşmesi, Türk Borçlar Kanunu'nun 299. maddesinde tanımlanır.\n\n"
        "Madde metni: \"Kira sözleşmesi, kiraya verenin bir şeyin kullanılmasını veya kullanmayla "
        "birlikte ondan yararlanılmasını kiracıya bırakmayı, kiracının da buna karşılık "
        "kararlaştırılan kira bedelini ödemeyi üstlendiği sözleşmedir.\"\n\n"
        "**Unsurları:**\n"
        "- Bir şeyin kullanımının/ondan yararlanmanın devri,\n"
        "- Belirli bir kira bedeli,\n"
        "- Tarafların karşılıklı ve birbirine uygun iradesi.\n\n"
        "Kira bir **kullandırma** sözleşmesidir; mülkiyet kiracıya geçmez. Konut ve çatılı "
        "işyeri kiraları için TBK m.339 ve devamında kiracıyı koruyan özel hükümler (tahliye "
        "sebeplerinin sınırlılığı, kira artış sınırı vb.) öngörülmüştür.",
    ),
    (
        "Dava dilekçesinde bulunması zorunlu unsurlar nelerdir? HMK 119.",
        "Dava dilekçesinin zorunlu unsurları, Hukuk Muhakemeleri Kanunu'nun 119. maddesinde "
        "sayılmıştır.\n\n"
        "**Dilekçede bulunması gerekenler (md. 119/1):**\n"
        "a) Mahkemenin adı,\n"
        "b) Davacı ile davalının ad, soyad ve adresleri,\n"
        "c) Davacının T.C. kimlik numarası,\n"
        "ç) Varsa tarafların kanuni temsilcilerinin ve vekillerinin bilgileri,\n"
        "d) Davanın konusu ve mal varlığı haklarına ilişkin davalarda dava değeri,\n"
        "e) Davacının iddiasının dayanağı vakıaların sıra numarası altında açık özetleri,\n"
        "f) İddia edilen her vakıanın hangi delillerle ispat edileceği,\n"
        "g) Dayanılan hukuki sebepler,\n"
        "ğ) Açık bir şekilde talep sonucu,\n"
        "h) İmza.\n\n"
        "**Eksiklik hâlinde:** Md. 119/2 uyarınca; (a) mahkemenin adı, (d) dava değeri, "
        "(e) vakıaların özeti, (f) deliller ve (g) hukuki sebepler **dışındaki** bir unsurun "
        "eksik olması hâlinde hâkim, davacıya bir haftalık kesin süre verir; bu sürede "
        "tamamlanmazsa dava açılmamış sayılır. Sayılan bu beş unsurun eksikliği ise tamamlatma "
        "yoluna tabi değildir.",
    ),
    (
        "İş güvencesinden yararlanma şartları nelerdir? 4857 madde 18.",
        "İş güvencesi (geçerli sebeple fesih zorunluluğu), 4857 sayılı İş Kanunu'nun 18. "
        "maddesinde düzenlenir.\n\n"
        "Madde metni (1. fıkra, özet): \"Otuz veya daha fazla işçi çalıştıran işyerlerinde en az "
        "altı aylık kıdemi olan işçinin belirsiz süreli iş sözleşmesini fesheden işveren, işçinin "
        "yeterliliğinden veya davranışlarından ya da işletmenin, işyerinin veya işin gereklerinden "
        "kaynaklanan geçerli bir sebebe dayanmak zorundadır.\"\n\n"
        "**Yararlanma şartları:**\n"
        "- İşyerinde **en az 30 işçi** çalışması,\n"
        "- İşçinin **en az 6 aylık kıdemi** olması (yer altı işlerinde kıdem şartı aranmaz),\n"
        "- **Belirsiz süreli** iş sözleşmesi,\n"
        "- İşçinin işletmenin bütününü sevk ve idare eden işveren vekili konumunda olmaması.\n\n"
        "Bu şartları taşıyan işçi, geçersiz feshe karşı fesih bildiriminin tebliğinden itibaren "
        "**bir ay içinde** işe iade talebiyle arabulucuya, anlaşma sağlanamazsa iş mahkemesine "
        "başvurabilir (md. 20).",
    ),
    (
        "İşçi hangi hallerde iş sözleşmesini haklı nedenle feshedebilir? 4857/24.",
        "İşçinin haklı nedenle derhal fesih hakkı, 4857 sayılı İş Kanunu'nun 24. maddesinde üç "
        "grupta düzenlenir.\n\n"
        "**I- Sağlık sebepleri:** İşin niteliğinden doğan bir sebeple işçinin sağlığı veya yaşayışı "
        "için tehlike oluşması; işverenin veya başka bir işçinin bulaşıcı/sürekli hastalığı.\n\n"
        "**II- Ahlak ve iyi niyet kurallarına uymayan haller:** İşverenin işçiyi yanıltması, "
        "şeref ve namusuna dokunacak söz/davranışlar, cinsel taciz, hakaret veya sataşma, "
        "**ücretin zamanında ödenmemesi**, eksik ödenmesi gibi hâller.\n\n"
        "**III- Zorlayıcı sebepler:** İşçinin çalıştığı işyerinde bir haftadan fazla süreyle işin "
        "durmasını gerektiren zorlayıcı sebeplerin ortaya çıkması.\n\n"
        "**Önemli sonuç:** İşçi haklı nedenle feshederse **kıdem tazminatına hak kazanır**; ancak "
        "feshi kendisi yaptığı için ihbar tazminatı talep edemez. Md. II kapsamındaki fesihlerde, "
        "olayı öğrenmeden itibaren **6 iş günü** ve her hâlde **1 yıl** içinde fesih hakkı "
        "kullanılmalıdır (md. 26 hak düşürücü süre).",
    ),
    (
        "İhbar önelleri ne kadardır? 4857 sayılı Kanun madde 17.",
        "Süreli fesihte uygulanacak ihbar önelleri, 4857 sayılı İş Kanunu'nun 17. maddesinde "
        "kıdeme göre belirlenmiştir.\n\n"
        "**İhbar süreleri:**\n"
        "- İşi 6 aydan az sürmüş işçi için: **2 hafta**,\n"
        "- 6 ay ile 1,5 yıl arası: **4 hafta**,\n"
        "- 1,5 yıl ile 3 yıl arası: **6 hafta**,\n"
        "- 3 yıldan fazla sürmüş işçi için: **8 hafta**.\n\n"
        "**Açıklama:** Bu süreler asgari olup sözleşmeyle artırılabilir. Bildirim şartına uymayan "
        "taraf, bu sürelere ait ücret tutarında **ihbar tazminatı** ödemekle yükümlüdür. İşveren "
        "isterse ihbar süresine ait ücreti peşin ödeyerek sözleşmeyi derhal feshedebilir. "
        "İhbar tazminatı, kıdem tazminatından farklı olarak haklı nedenle yapılan fesihlerde "
        "ödenmez.",
    ),
    (
        "Ceza hukukunda kast nedir? TCK madde 21.",
        "Kast kavramı, Türk Ceza Kanunu'nun 21. maddesinde tanımlanır.\n\n"
        "Madde metni (1. fıkra): \"Suçun oluşması kastın varlığına bağlıdır. Kast, suçun kanuni "
        "tanımındaki unsurların bilerek ve istenerek gerçekleştirilmesidir.\"\n\n"
        "**Kastın türleri:**\n"
        "- **Doğrudan kast:** Failin unsurları bilerek ve isteyerek gerçekleştirmesi.\n"
        "- **Olası (muhtemel) kast (md. 21/2):** Failin, suçun kanuni tanımındaki unsurların "
        "gerçekleşebileceğini öngörmesine rağmen fiili işlemesi (\"olursa olsun\" tutumu). Bu "
        "hâlde ağırlaştırılmış müebbet hapis cezasını gerektiren suçlarda müebbet hapse, müebbet "
        "hapis cezasını gerektiren suçlarda 20-25 yıl hapse hükmolunur.\n\n"
        "**Temel ilke:** TCK m.21/1 gereği kural kasttır; taksirle işlenen fiiller ancak kanunda "
        "açıkça öngörülen hâllerde cezalandırılır (TCK m.22).",
    ),
    (
        "Meşru savunma hangi şartlarda kabul edilir? TCK 25.",
        "Meşru savunma (meşru müdafaa), Türk Ceza Kanunu'nun 25. maddesinin 1. fıkrasında bir "
        "hukuka uygunluk sebebi olarak düzenlenir.\n\n"
        "Madde metni: \"Gerek kendisine ve gerek başkasına ait bir hakka yönelmiş, gerçekleşen, "
        "gerçekleşmesi veya tekrarı muhakkak olan haksız bir saldırıyı o anda hâl ve koşullara göre "
        "saldırı ile orantılı biçimde defetmek zorunluluğu ile işlenen fiillerden dolayı faile ceza "
        "verilmez.\"\n\n"
        "**Saldırıya ilişkin şartlar:** Bir hakka yönelik, **haksız** ve **güncel** (gerçekleşen, "
        "gerçekleşmesi veya tekrarı muhakkak) bir saldırı bulunmalıdır.\n\n"
        "**Savunmaya ilişkin şartlar:** Savunma saldırıya karşı **zorunlu** ve saldırı ile "
        "**orantılı** olmalıdır.\n\n"
        "**Sınırın aşılması:** Meşru savunmada sınırın mazur görülebilecek bir heyecan, korku veya "
        "telaşla aşılması hâlinde faile ceza verilmez (TCK m.27/2).",
    ),
    (
        "İcra takibine itiraz edildi, alacaklı ne yapabilir? İtirazın iptali davası nedir?",
        "İlamsız icra takibine borçlunun itirazı üzerine takip durur. Alacaklının başvurabileceği "
        "yollardan biri, İcra ve İflas Kanunu'nun 67. maddesindeki **itirazın iptali davasıdır.**\n\n"
        "**İtirazın iptali davası (İİK m.67):**\n"
        "- Alacaklı, itirazın kendisine tebliğinden itibaren **bir yıl içinde** genel mahkemede "
        "dava açar.\n"
        "- Mahkeme davayı esastan inceler (genel yargılama).\n"
        "- Dava kabul edilirse itiraz iptal edilir ve takip kaldığı yerden devam eder.\n"
        "- İtirazın haksızlığına karar verilirse, borçlu alacağın **%20'sinden az olmamak üzere** "
        "icra inkâr tazminatına mahkûm edilebilir.\n\n"
        "**Alternatif yol — itirazın kaldırılması (İİK m.68):** Alacak; imzası ikrar edilmiş bir "
        "borç senedine veya resmî/onaylı bir belgeye dayanıyorsa, alacaklı icra mahkemesinden "
        "(daha hızlı, sınırlı incelemeyle) itirazın kaldırılmasını isteyebilir. Bu yolun süresi "
        "itirazın tebliğinden itibaren **altı aydır.**",
    ),
    (
        "Ayıplı mal nedir? Tüketici Kanunu'nda nasıl düzenlenmiş?",
        "Ayıplı mal, 6502 sayılı Tüketicinin Korunması Hakkında Kanun'un 8. maddesinde "
        "tanımlanır.\n\n"
        "Madde metni (1. fıkra): \"Ayıplı mal, tüketiciye teslimi anında, taraflarca kararlaştırılmış "
        "olan örnek ya da modele uygun olmaması ya da objektif olarak sahip olması gereken "
        "özellikleri taşımaması nedeniyle sözleşmeye aykırı olan maldır.\"\n\n"
        "**Ayıp türleri:** Maddi, hukuki veya ekonomik ayıp olabilir; sözleşmede belirtilen veya "
        "reklamda vaat edilen niteliği taşımamak da ayıp sayılır.\n\n"
        "**Tüketicinin seçimlik hakları (6502 m.11):**\n"
        "- Sözleşmeden dönme,\n"
        "- Bedelden indirim isteme,\n"
        "- Ücretsiz onarım isteme,\n"
        "- Malın ayıpsız misliyle değiştirilmesini isteme.\n\n"
        "**Zamanaşımı:** Aksine bir düzenleme yoksa ayıptan sorumluluk, malın teslim tarihinden "
        "itibaren **iki yıldır** (6502 m.12). Teslim anında ayıp tüketici tarafından biliniyorsa "
        "sözleşmeye aykırılıktan söz edilemez.",
    ),
    (
        "Mesafeli sözleşmelerde cayma hakkı kaç gündür?",
        "Mesafeli sözleşmelerde tüketicinin cayma hakkı, 6502 sayılı Tüketicinin Korunması "
        "Hakkında Kanun'un 48. maddesinde düzenlenir.\n\n"
        "**Cayma süresi:** Tüketici, **on dört gün** içinde herhangi bir gerekçe göstermeksizin ve "
        "cezai şart ödemeksizin sözleşmeden cayabilir.\n\n"
        "**Sürenin başlangıcı:**\n"
        "- Hizmet ifasına ilişkin sözleşmelerde sözleşmenin kurulduğu gün,\n"
        "- Mal teslimine ilişkin sözleşmelerde tüketicinin malı teslim aldığı gün.\n\n"
        "**Bilgilendirme yükümlülüğü:** Satıcı/sağlayıcı cayma hakkı konusunda tüketiciyi gereği "
        "gibi bilgilendirmezse, cayma süresi 14 günlük sürenin bittiği tarihten itibaren **bir yıl** "
        "uzar.\n\n"
        "**İstisnalar:** Tüketicinin özel istekleri doğrultusunda hazırlanan mallar, çabuk bozulan "
        "ürünler, ambalajı açılmış hijyenik ürünler gibi hâllerde cayma hakkı kullanılamaz "
        "(Mesafeli Sözleşmeler Yönetmeliği m.15).",
    ),
    (
        "Tacir kimdir ve basiretli iş adamı gibi davranma yükümlülüğü nedir? TTK 18.",
        "Tacirin tabi olduğu temel hükümler, Türk Ticaret Kanunu'nun 18. maddesinde yer alır. "
        "Tacir sıfatının kazanılması ise TTK m.12'de düzenlenir (bir ticari işletmeyi kısmen de "
        "olsa kendi adına işleten kişi tacirdir).\n\n"
        "**TTK m.18 hükümleri:**\n"
        "- Tacir, her türlü borcu için **iflasa tabidir** (md. 18/1).\n"
        "- Tacir, ticaret unvanını seçmek ve ticari işletmesini ticaret siciline tescil ettirmekle "
        "yükümlüdür.\n"
        "- **Basiretli iş adamı gibi hareket yükümlülüğü (md. 18/2):** \"Her tacirin, ticaretine ait "
        "bütün faaliyetlerinde basiretli bir iş adamı gibi hareket etmesi gerekir.\"\n\n"
        "**Basiretli iş adamı ölçütünün sonuçları:**\n"
        "- Tacirden, alanında öngörülü ve tedbirli bir kişinin göstereceği özen beklenir; "
        "bilmemesi mazeret sayılmaz.\n"
        "- Aşırı ifa güçlüğü (uyarlama) ve cezai şartın indirilmesi gibi konularda tacir lehine "
        "esnekliklerin sınırı bu ölçütle daralır.\n"
        "- İhtar ve ihbarların kural olarak yazılı şekilde yapılması gibi şekil kuralları tacirler "
        "için öngörülmüştür (md. 18/3).",
    ),
    (
        "Vekâletsiz iş görme nedir? TBK madde 526.",
        "Vekâletsiz iş görme, Türk Borçlar Kanunu'nun 526. maddesinde düzenlenen, bir kimsenin "
        "**herhangi bir yetkisi olmaksızın** başkasının işini görmesi hâlidir.\n\n"
        "Madde metni (1. fıkra): \"Bir kimse, sözleşmeden veya kanundan doğan bir yetkisi "
        "olmaksızın bir başkasının işini görmeye girişirse, ortaya çıkan borç ilişkisine vekâletsiz "
        "iş görme hükümleri uygulanır.\"\n\n"
        "**Türleri:**\n"
        "- **Gerçek (uygun) vekâletsiz iş görme (m.526):** İş gören, işsahibinin **yararına ve "
        "muhtemel iradesine uygun** biçimde hareket eder; iş sahibinden gerekli giderlerin "
        "ödenmesini isteyebilir.\n"
        "- **Gerçek olmayan vekâletsiz iş görme (m.530):** İş gören, başkasının işini **kendi "
        "yararına** görür; bu hâlde iş sahibi, elde edilen kazancın kendisine verilmesini "
        "isteyebilir.\n\n"
        "**Tipik örnek:** Komşusunun evindeki su kaçağını, kendisi yokken haber veremeden "
        "müdahale ederek önleyen kişi gerçek vekâletsiz iş görme hükümlerinden yararlanır.\n\n"
        "**Önemli sonuç:** İş gören, işe girişmesini iş sahibine **olanak bulur bulmaz** "
        "bildirmek ve onun hesabına özenle hareket etmekle yükümlüdür (m.527).",
    ),
    (
        "Önalım, iştira ve vefa hakları nedir, TBK'da nasıl düzenlenir?",
        "Bu üç hak, bir taşınmazın **belirli bir kişiye satılması veya geri alınmasını** sağlayan "
        "yenilik doğuran sözleşmesel haklardır; Türk Borçlar Kanunu'nun 237-247. maddelerinde "
        "düzenlenir.\n\n"
        "**Önalım (şufa) hakkı (TBK m.240):** Hak sahibine, taşınmazın üçüncü bir kişiye "
        "satılması hâlinde **aynı koşullarla öncelikli satın alma** yetkisi verir. (Paylı "
        "mülkiyetten doğan yasal önalım hakkı ise TMK m.732'de ayrıca düzenlenmiştir.)\n\n"
        "**İştira (alım) hakkı (TBK m.243):** Hak sahibine, taşınmazı **tek taraflı irade "
        "beyanıyla**, üçüncü kişiye satılıp satılmadığına bakılmaksızın, önceden belirlenmiş "
        "koşullarla satın alma yetkisi verir.\n\n"
        "**Vefa (geri alım) hakkı (TBK m.245):** Satıcıya, sattığı taşınmazı belirli bir bedelle "
        "**geri satın alma** yetkisi tanır.\n\n"
        "**Ortak özellikleri:** Sözleşmeyle kurulur, **resmî şekle** tabidir ve tapu kütüğüne "
        "şerh verilerek üçüncü kişilere karşı ileri sürülebilir hâle gelir; şerhin etkisi en "
        "fazla **on yıl** sürer (TBK m.238).",
    ),
    (
        "İcranın geri bırakılması nedir? İİK madde 33.",
        "İcranın geri bırakılması (tehiri), İcra ve İflas Kanunu'nun 33. maddesinde düzenlenen, "
        "**ilamlı icrada** borçluya tanınan bir savunma yoludur.\n\n"
        "**Temel mantığı:** Borçlu, kendisine icra emri tebliğ edildikten **sonra** doğan bir "
        "borçtan kurtulma sebebine (ödeme, takas, zamanaşımı, ibra vb.) dayanıyorsa, bunu icra "
        "mahkemesine bildirerek **icranın geçici olarak durdurulmasını** isteyebilir.\n\n"
        "**Usul:**\n"
        "- Talep, icra emrinin tebliğinden itibaren **yedi gün** içinde yapılmalıdır.\n"
        "- Sebep **resmî bir belgeye** dayanıyorsa icranın geri bırakılmasına karar verilir; "
        "değilse mahkeme, alacaklının **muvakkat (geçici) teminatı** karşılığında icrayı "
        "durdurabilir.\n\n"
        "**Önemli ayrım:** İcranın geri bırakılması, **icra emrinden sonra doğan** sebeplere "
        "dayanır; ilamın esasına yönelik itirazlar (örn. borcun hiç doğmamış olması) "
        "kanun yollarına (istinaf/temyiz) konu edilir, icra mahkemesinde ileri sürülemez.",
    ),
    (
        "Tehlikeli madde bulunduran işletmenin sorumluluğu nasıl düzenlenir? TBK madde 71.",
        "Tehlike sorumluluğu, Türk Borçlar Kanunu'nun 71. maddesinde düzenlenen bir "
        "**kusursuz sorumluluk** hâlidir.\n\n"
        "Madde metni (1. fıkra, özet): \"Önemli ölçüde tehlike arz eden bir işletmenin "
        "faaliyetinden zarar doğduğu takdirde, bu zarardan işletme sahibi ve varsa işleten "
        "müteselsilen sorumludur.\"\n\n"
        "**Unsurları:**\n"
        "- İşletmenin **önemli ölçüde tehlike** arz etmesi (niteliği, kullanılan araç/maddeler "
        "ve faaliyet alanı itibarıyla),\n"
        "- Bu faaliyetten bir **zarar** doğmuş olması,\n"
        "- **Kusur aranmaz** — işletme sahibi özen gösterdiğini ispatlasa bile sorumluluktan "
        "kurtulamaz.\n\n"
        "**Kurtuluş kanıtı:** İşletme sahibi ancak zararın **mücbir sebepten veya zarar "
        "görenin ya da üçüncü kişinin ağır kusurundan** doğduğunu ispatlarsa sorumluluktan "
        "kurtulabilir (m.71/2).\n\n"
        "**Uygulama alanı:** Akaryakıt depoları, kimyasal madde üretim tesisleri, yüksek "
        "gerilim hatları gibi faaliyetlerden doğan zararlarda sıkça uygulanır; mağdurun kusur "
        "ispatlamasına gerek kalmadan tazminat almasını kolaylaştırır.",
    ),
    (
        "TBK madde 27 neyi düzenler, kesin hükümsüzlük ne anlama gelir?",
        "Türk Borçlar Kanunu m.27, sözleşmelerin **kesin hükümsüzlük** hâllerini düzenler.\n\n"
        "Madde metni (özet): \"Kanunun emredici hükümlerine, ahlaka, kamu düzenine, "
        "kişilik haklarına aykırı veya konusu imkânsız olan sözleşmeler kesin olarak "
        "hükümsüzdür.\"\n\n"
        "**Temel özellikleri:**\n"
        "- **Re'sen dikkate alınır:** Hâkim, taraflar ileri sürmese bile kesin hükümsüzlüğü "
        "kendiliğinden gözetir.\n"
        "- **Herkes ileri sürebilir:** Sözleşmenin tarafı olmayan üçüncü kişiler de "
        "menfaatleri varsa hükümsüzlüğü ileri sürebilir.\n"
        "- **Süreye bağlı değildir:** Kesin hükümsüzlük iddiası zamanaşımı veya hak "
        "düşürücü süreye tabi değildir; her zaman ileri sürülebilir.\n"
        "- **Kısmi hükümsüzlük (m.27/2):** Sözleşmenin yalnızca bir kısmı hükümsüzse ve "
        "bu kısım olmaksızın sözleşme yapılmayacağı açıkça anlaşılmıyorsa, sözleşmenin "
        "geri kalanı geçerliliğini korur.\n\n"
        "**Örnek:** Kumar borcu için yapılan bir sözleşme, ahlaka aykırılık nedeniyle "
        "kesin hükümsüzdür; taraflardan biri bu sözleşmeye dayanarak edim talep edemez.",
    ),
    (
        "TMK madde 1023 ne anlama gelir, tapu siciline güven ilkesi nedir?",
        "Türk Medeni Kanunu m.1023, taşınmaz hukukunda büyük önem taşıyan **tapu siciline "
        "güven (iyiniyet karinesi)** ilkesini düzenler.\n\n"
        "Madde metni: \"Tapu kütüğündeki tescile iyiniyetle dayanarak mülkiyet veya bir "
        "başka ayni hak kazanan üçüncü kişinin bu kazanımı korunur.\"\n\n"
        "**Anlamı ve şartları:**\n"
        "- Bir kişi, tapu kütüğünde **görünen** duruma güvenerek bir taşınmaz üzerinde "
        "ayni hak (mülkiyet, ipotek, intifa vb.) elde ederse, bu kazanım, kütükte "
        "görünmeyen önceki bir hak sahibinin gerçek hakkı karşısında dahi **korunur**.\n"
        "- Koruma için kazananın **iyiniyetli** olması şarttır (TMK m.3); tapudaki "
        "yanlışlığı bilen veya bilmesi gereken kişi bu korumadan yararlanamaz.\n"
        "- Bu ilke, tapu sicilinin **güvenilirliğini ve işlem güvenliğini** sağlamak "
        "amacıyla, gerçek hak sahibinin menfaatine istisna getirir.\n\n"
        "**Örnek:** A'nın taşınmazı, sahte bir vekâletnameyle B adına tescil edilmiş ve "
        "B de bu taşınmazı iyiniyetli C'ye satmışsa; C'nin tapu kütüğüne güvenerek yaptığı "
        "kazanım, somut şartlar oluştuğunda korunabilir — A'nın hakkı ise B'ye karşı "
        "tazminat talebine dönüşebilir.",
    ),
    (
        "İş Kanunu madde 22 iş sözleşmesinde değişiklikle ilgili ne diyor?",
        "4857 sayılı İş Kanunu m.22, işverenin iş sözleşmesinin **esaslı unsurlarında "
        "değişiklik** yapma yetkisinin sınırlarını düzenler.\n\n"
        "Madde metni (özet): \"İşveren, iş sözleşmesiyle veya iş sözleşmesinin eki "
        "niteliğindeki personel yönetmeliği ve benzeri kaynaklar ya da işyeri "
        "uygulamasıyla oluşan çalışma koşullarında esaslı bir değişikliği ancak durumu "
        "işçiye yazılı olarak bildirmek suretiyle yapabilir. Bu şekle uygun "
        "yapılmayan ve işçi tarafından altı işgünü içinde yazılı olarak kabul "
        "edilmeyen değişiklikler işçiyi bağlamaz.\"\n\n"
        "**Önemli noktalar:**\n"
        "- Esaslı değişiklik **yazılı bildirimle** yapılmalı; işçinin **6 işgünü içinde "
        "yazılı kabulü** gerekir.\n"
        "- İşçi değişikliği kabul etmezse, işveren değişikliğin **geçerli bir nedene "
        "dayandığını** yazılı olarak açıklayıp bildirim süresine uyarak iş sözleşmesini "
        "feshedebilir; bu hâlde işçi de feshe karşı dava açabilir.\n"
        "- Şekle aykırı yapılan veya işçi tarafından kabul edilmeyen değişiklikler **işçiyi "
        "bağlamaz**; işçi eski koşullarda çalışmaya devam etme hakkını korur.\n\n"
        "**Örnek:** İşveren, işçinin ücretini veya görev yerini tek taraflı ve yazılı "
        "bildirim olmaksızın değiştiremez; bu yönde dayatılan bir değişikliği işçi "
        "kabul etmek zorunda değildir.",
    ),
    (
        "HMK madde 297 mahkeme kararının kapsamını nasıl düzenler?",
        "Hukuk Muhakemeleri Kanunu m.297, mahkeme **hükmünün** taşıması gereken zorunlu "
        "unsurları düzenler.\n\n"
        "Madde metni (özet): Hükümde; mahkeme adı, hâkim/hâkimlerin ve zabıt kâtibinin "
        "adı, tarafların ve varsa vekillerinin kimlikleri, iddia ve savunmaların özeti, "
        "anlaştıkları ve anlaşamadıkları hususlar, deliller ile bunların tartışılması ve "
        "değerlendirilmesi, sabit görülen vakıalarla bunlardan çıkarılan sonuç ve hukuki "
        "sebep, **hüküm sonucu** ve kanun yollarına başvuru bilgileri yer almalıdır.\n\n"
        "**Önemi:**\n"
        "- Hükmün **gerekçesiz** olması veya bu unsurlardan birini içermemesi, kararın "
        "**bozulması** için tek başına yeterli sebep olabilir; gerekçe, tarafların kanun "
        "yoluna etkili biçimde başvurabilmesi için zorunludur.\n"
        "- **Hüküm sonucu kısmı** (madde 297/2), şarta bağlı olamaz ve açık, anlaşılır, "
        "infaza elverişli biçimde yazılmalıdır; aksi hâlde infazda tereddüt doğar.\n\n"
        "**Pratik sonuç:** Bir kararın yalnızca sonuç kısmı değil, gerekçesi de incelenmeli; "
        "gerekçe ile hüküm arasında çelişki varsa bu durum istinaf/temyiz sebebi "
        "oluşturabilir.",
    ),
    (
        "TBK madde 480 eser sözleşmesinde ayıba karşı tekeffül ne anlama gelir?",
        "Türk Borçlar Kanunu m.480 vd., **eser sözleşmesinde** (TBK m.470) "
        "yüklenicinin, meydana getirdiği eserin **ayıplı olmasından doğan "
        "sorumluluğunu** (ayıba karşı tekeffül borcunu) düzenler.\n\n"
        "**Temel kurallar:**\n"
        "- İş sahibi, eseri teslim aldıktan sonra **işlerin olağan akışına göre "
        "makul bir süre içinde** gözden geçirmek ve ayıpları varsa yükleniciye "
        "**bildirmek** zorundadır (m.477); bildirmezse eseri kabul etmiş "
        "sayılabilir.\n"
        "- Ayıp tespit edilirse iş sahibi; **ücretsiz onarım, bedelden indirim** "
        "veya önemli bir ayıp varsa **sözleşmeden dönme** seçimlik haklarından "
        "birini kullanabilir (m.475).\n"
        "- Yüklenicinin **ağır kusuru** varsa, iş sahibinin bu hakları kullanma "
        "süresi uzayabilir ve ayrıca tazminat talep edilebilir (m.478).\n\n"
        "**Zamanaşımı:** Taşınmaz yapı eserlerinde tekeffül talepleri **beş yıllık** "
        "zamanaşımına tabidir (m.478); taşınır eserlerde ise genel zamanaşımı "
        "süreleri uygulanır.\n\n"
        "**Örnek:** Bir müteahhitten anahtar teslim alınan evde, teslimden kısa "
        "süre sonra duvarlarda ciddi nem ve çatlaklar ortaya çıkarsa, iş sahibi "
        "bu durumu yükleniciye bildirip ücretsiz onarım veya bedelden indirim "
        "talep edebilir.",
    ),
    (
        "TMK madde 1007 devletin sorumluluğu tapu sicilinden doğan zararlar için "
        "ne diyor?",
        "Türk Medeni Kanunu m.1007, **tapu sicilinin tutulmasından doğan "
        "zararlardan devletin sorumluluğunu** düzenler.\n\n"
        "Madde metni (özet): \"Tapu sicilinin tutulmasından doğan bütün zararlardan "
        "Devlet sorumludur. Devlet, zararın doğmasında kusuru bulunan görevlilere "
        "rücu eder.\"\n\n"
        "**Önemli noktalar:**\n"
        "- Bu, **kusursuz sorumluluk** esasına dayanan özel bir devlet "
        "sorumluluğu hâlidir; zarar gören, tapu memurunun kişisel kusurunu "
        "ispatlamak zorunda değildir — devletin sorumluluğu doğrudan **tapu "
        "sicilinin hatalı tutulmasından** kaynaklanır.\n"
        "- Bu davalar, genel görevli mahkemelerde (asliye hukuk) **devlet "
        "aleyhine** açılır; idari işlem niteliğinde olmadığından idari yargıya "
        "değil **adli yargıya** tabidir (yerleşik içtihat).\n"
        "- Devlet, ödediği tazminat için kusurlu bulunan **tapu görevlisine "
        "rücu** edebilir.\n\n"
        "**Örnek:** Tapu müdürlüğünün hatalı bir tescil işlemi nedeniyle "
        "taşınmazını kaybeden kişi, doğrudan tapu memuruna değil, **Hazine'ye "
        "karşı** TMK m.1007'ye dayanarak tazminat davası açabilir.",
    ),
    (
        "TBK madde 299 kira sözleşmesini nasıl tanımlıyor?",
        "Türk Borçlar Kanunu m.299, **kira sözleşmesinin tanımını ve temel "
        "unsurlarını** düzenler.\n\n"
        "Madde metni (özet): \"Kira sözleşmesi, kiraya verenin bir şeyin "
        "kullanılmasını veya kullanmayla birlikte ondan yararlanılmasını "
        "kiracıya bırakmayı, kiracının da buna karşılık kararlaştırılan kira "
        "bedelini ödemeyi üstlendiği sözleşmedir.\"\n\n"
        "**Önemli noktalar:**\n"
        "- Kira sözleşmesi **karşılıklı edimler** içeren, rızaen kurulan bir "
        "sözleşmedir; şekil şartına bağlı değildir (yazılı olmayan kira "
        "sözleşmeleri de geçerlidir, ancak ispat açısından yazılı olması "
        "önerilir).\n"
        "- İki temel edim söz konusudur: kiraya verenin **kullanım/yararlanmayı "
        "sağlama** borcu (TBK m.301-302) ve kiracının **kira bedelini ödeme** "
        "borcu (TBK m.313 vd.).\n"
        "- Konut ve çatılı işyeri kiralarında kiracıyı koruyucu özel hükümler "
        "(TBK m.339-356) ayrıca uygulanır; bu hükümlerin bir kısmı kiracı "
        "aleyhine değiştirilemez (emredici nitelikte).\n\n"
        "**Örnek:** Bir kişi dairesini aylık kira bedeli karşılığında başka "
        "birine kullanması için bıraktığında, taraflar arasında TBK m.299 "
        "anlamında bir kira sözleşmesi kurulmuş olur — yazılı sözleşme "
        "olmasa bile.",
    ),
    (
        "İcra ve İflas Kanunu madde 67 ne diyor, itirazın iptali davası nedir?",
        "İcra ve İflas Kanunu (2004 sayılı) m.67, **itirazın iptali davasını** "
        "düzenler.\n\n"
        "Madde metni (özet): \"Borçlu, takibe itiraz ederse alacaklı, itirazın "
        "tebliği tarihinden itibaren bir yıl içinde mahkemeye başvurarak "
        "itirazın iptalini isteyebilir... Bu davada borçlunun ödeme "
        "emrindeki borca itirazı haksız çıkarsa, borçlu alacağın yüzde "
        "yirmisinden aşağı olmamak üzere tazminata mahkûm edilir.\"\n\n"
        "**Önemli noktalar:**\n"
        "- Borçlu, ilamsız icra takibine **süresi içinde itiraz** ederse "
        "(İİK m.62, 7 gün), takip kendiliğinden durur; alacaklının alacağına "
        "kavuşabilmesi için bu itirazın ortadan kaldırılması gerekir.\n"
        "- Alacaklı, itirazın iptali için **genel mahkemede dava** açabilir "
        "(İİK m.67) veya icra mahkemesinde **itirazın kaldırılması** yoluna "
        "gidebilir (İİK m.68); hangi yolun seçileceği elindeki belgenin "
        "niteliğine göre değişir.\n"
        "- Dava, itirazın tebliğinden itibaren **1 yıllık süre** içinde "
        "açılmalıdır; bu süre geçtikten sonra alacaklı yalnızca genel "
        "hükümlere göre alacak davası açabilir.\n"
        "- Davayı kaybeden taraf, **%20'den az olmamak üzere icra inkâr "
        "tazminatına** mahkûm edilebilir — bu, tarafları gereksiz itiraz/"
        "takipten caydıran önemli bir müeyyidedir.\n\n"
        "**Örnek:** Alacaklı, ödeme emrine itiraz eden borçluya karşı 1 yıl "
        "içinde itirazın iptali davası açar; mahkeme itirazı haksız bulursa "
        "hem takip kaldığı yerden devam eder hem de borçlu icra inkâr "
        "tazminatı ödemek zorunda kalabilir.",
    ),
]


def main():
    data = [
        {"category": CATEGORY, "source": SOURCE, "user": u, "assistant": a}
        for (u, a) in PAIRS
    ]
    OUT_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"{len(data)} cift yazildi -> {OUT_FILE}")


if __name__ == "__main__":
    main()
