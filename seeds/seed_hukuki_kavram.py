"""
Seed — Kategori 2: Hukuki Kavram Tanımı
=======================================
Temel ve ileri hukuki kavramların katmanlı, kaynaklı tanımları.

    python seeds/seed_hukuki_kavram.py
    python akai_dataset_generator.py --mode import --file seeds/seed_hukuki_kavram.json
"""

import json
from pathlib import Path

CATEGORY = "hukuki_kavram"
SOURCE = "claude_seed"
OUT_FILE = Path(__file__).with_name("seed_hukuki_kavram.json")

PAIRS = [
    (
        "İstinaf ile temyiz arasındaki fark nedir?",
        "İkisi de yerel mahkeme kararına karşı başvurulan kanun yollarıdır; ancak inceleme "
        "mercileri ve kapsamları farklıdır.\n\n"
        "**İstinaf (HMK m.341 vd.)**\n"
        "- Merci: **Bölge Adliye Mahkemesi (İstinaf)**.\n"
        "- İlk derece mahkemesi kararı hem **maddi vakıa** hem **hukuki** yönden yeniden "
        "incelenir; gerektiğinde dosya üzerinden yeni karar verilir.\n"
        "- Kural olarak kararın tebliğinden itibaren **iki hafta** içinde başvurulur.\n\n"
        "**Temyiz (HMK m.361 vd.)**\n"
        "- Merci: **Yargıtay**.\n"
        "- Yalnızca **hukuka uygunluk** denetimi yapılır; maddi vakıa yeniden incelenmez "
        "(hukuk denetimi).\n"
        "- İstinaf kararının tebliğinden itibaren kural olarak **iki hafta** içinde başvurulur.\n\n"
        "**Özetle:** İstinaf hem olayı hem hukuku denetleyen bir \"ikinci derece yargılaması\", "
        "temyiz ise sadece hukuki denetimdir. Ayrıca her karar temyize açık değildir; HMK m.362 "
        "belirli parasal sınırların altındaki kararları temyiz dışında bırakır.",
    ),
    (
        "İhtiyati tedbir ile ihtiyati haciz arasındaki fark nedir?",
        "Her ikisi de yargılama sonuçlanmadan hak kaybını önleyen geçici hukuki korumalardır; "
        "ancak amaçları ve dayanakları farklıdır.\n\n"
        "**İhtiyati tedbir (HMK m.389 vd.)**\n"
        "- Genel bir geçici koruma tedbiridir; **para alacağı dışındaki** uyuşmazlıklarda da "
        "uygulanır.\n"
        "- Amaç: Dava konusu şey üzerinde mevcut durumun (statükonun) korunması veya bir "
        "sakıncanın önlenmesi (ör. tapuya tedbir şerhi, bir işin yapılmasının durdurulması).\n\n"
        "**İhtiyati haciz (İİK m.257 vd.)**\n"
        "- Yalnızca **para alacakları** için öngörülmüş bir icra hukuku kurumudur.\n"
        "- Amaç: Borçlunun mallarına geçici olarak el konularak alacağın tahsilinin güvence "
        "altına alınması.\n\n"
        "**Temel fark:** İhtiyati tedbir dava konusu şeyi/durumu korur; ihtiyati haciz ise para "
        "alacağının tahsil güvencesini sağlar. Her ikisinde de haksız çıkma ihtimaline karşı "
        "kural olarak teminat yatırılması istenir.",
    ),
    (
        "Menfi tespit davası nedir?",
        "Menfi (olumsuz) tespit davası, bir borcun veya hukuki ilişkinin **mevcut olmadığının** "
        "mahkemece tespitini amaçlayan davadır. İcra hukukundaki özel hâli İcra ve İflas "
        "Kanunu'nun 72. maddesinde düzenlenmiştir.\n\n"
        "**Tipik kullanım:** Hakkında icra takibi başlatılan veya kendisine borç isnat edilen "
        "kişi, aslında borçlu olmadığını ileri sürerek bu davayı açar (ör. ödenmiş bir borç için "
        "ikinci kez takip yapılması, sahte senet).\n\n"
        "**İcra takibinden önce/sonra:**\n"
        "- Takipten **önce** açılırsa, mahkeme talep üzerine takibin durdurulmasına karar "
        "verebilir.\n"
        "- Takipten **sonra** açılırsa takip kural olarak durmaz; ancak borçlu, alacağın "
        "%15'inden az olmamak üzere teminat göstererek takibin durdurulmasını isteyebilir.\n\n"
        "**İstirdat davasından farkı:** Menfi tespitte borç henüz ödenmemiştir (borçlu "
        "olunmadığının tespiti istenir); ödeme yapıldıktan sonra geri alınması isteniyorsa "
        "**istirdat davası** (İİK m.72/7) söz konusu olur.",
    ),
    (
        "Müteselsil sorumluluk ne demektir?",
        "Müteselsil (zincirleme) sorumluluk, birden fazla borçlunun aynı borcun **tamamından** "
        "alacaklıya karşı sorumlu olması durumudur (TBK m.162 vd.).\n\n"
        "**İşleyişi:**\n"
        "- Alacaklı, borcun tamamını borçluların **herhangi birinden** isteyebilir; tahsil "
        "edemediğini diğerlerine başvurarak tamamlatabilir.\n"
        "- Borçlulardan biri borcu öderse, hepsi alacaklıya karşı borçtan kurtulur.\n"
        "- Ödeyen borçlu, diğerlerine **rücu** ederek onların payını talep edebilir (TBK m.167).\n\n"
        "**Doğduğu hâller:** Kanundan (ör. haksız fiilde birden fazla failin sorumluluğu — "
        "TBK m.61) veya sözleşmeden (tarafların müteselsil sorumluluğu kararlaştırması) "
        "kaynaklanabilir.\n\n"
        "**Önemli not:** Müteselsil borçlulukta alacaklı lehine güçlü bir tahsil imkânı vardır; "
        "borçlular kendi aralarındaki iç ilişkide ise paylarına göre sorumludur.",
    ),
    (
        "Muvazaa nedir, türleri nelerdir?",
        "Muvazaa, tarafların gerçek iradelerine uymayan, üçüncü kişileri yanıltmak amacıyla "
        "yaptıkları danışıklı (görünüşte) işlemdir. Dayanağı TBK m.19'dur (sözleşmenin yorumu, "
        "muvazaa).\n\n"
        "**Türleri:**\n"
        "- **Mutlak muvazaa:** Taraflar aslında hiçbir işlem yapmak istemez, yalnızca üçüncü "
        "kişilere karşı görünüşte bir işlem yaratırlar (ör. mallarını alacaklılardan kaçırmak "
        "için tapuda gerçekte satış olmadığı hâlde satış göstermek).\n"
        "- **Nispi (mevsuf) muvazaa:** Taraflar gerçekte bir işlem yapmak ister ama onu başka bir "
        "işlem görüntüsü altında gizler (ör. bağışı satış gibi göstermek).\n\n"
        "**Sonucu:** Görünüşteki (muvazaalı) işlem **geçersizdir**. Nispi muvazaada gizlenen "
        "gerçek işlem, kendi geçerlilik şartlarını taşıyorsa ayakta kalır. Muvazaa her türlü "
        "delille ispatlanabilir ve hâkim tarafından dikkate alınır; muvazaa iddiası "
        "zamanaşımına tabi değildir.",
    ),
    (
        "Sebepsiz zenginleşme nedir?",
        "Sebepsiz zenginleşme, bir kişinin **haklı bir sebep olmaksızın** başkasının mal "
        "varlığından zenginleşmesi hâlinde, bu kazanımı iade yükümlülüğü doğuran bir borç "
        "kaynağıdır (TBK m.77 vd.).\n\n"
        "**Unsurları:**\n"
        "- Bir tarafın mal varlığında **zenginleşme**,\n"
        "- Diğer tarafın mal varlığında **fakirleşme**,\n"
        "- Zenginleşme ile fakirleşme arasında **illiyet bağı**,\n"
        "- Zenginleşmenin **haklı bir sebebe dayanmaması** (geçersiz sözleşme, gerçekleşmeyen "
        "sebep veya borç olmadığı hâlde yapılan ödeme).\n\n"
        "**Örnek:** Geçersiz bir sözleşmeye dayanarak yapılan ödeme; yanlışlıkla başkasının "
        "hesabına gönderilen para.\n\n"
        "**Zamanaşımı (TBK m.82):** Hak sahibinin iade hakkını öğrenmesinden itibaren **2 yıl**, "
        "her hâlde zenginleşmenin gerçekleştiği tarihten itibaren **10 yıl**. İyiniyetli "
        "zenginleşen yalnızca elinde kalanı iade ederken, kötüniyetli olan zenginleşmenin "
        "tamamından sorumludur.",
    ),
    (
        "Ön alım (şufa) hakkı nedir?",
        "Ön alım (şufa) hakkı, paylı mülkiyette bir paydaşın payını üçüncü bir kişiye satması "
        "hâlinde, diğer paydaşlara o payı **öncelikle satın alma** yetkisi veren haktır "
        "(TMK m.732 vd.).\n\n"
        "**İşleyişi:**\n"
        "- Yasal ön alım hakkı **paydaş olmaktan** doğar; ayrıca sözleşmeyle de "
        "kurulabilir (sözleşmeden doğan ön alım, TBK m.240).\n"
        "- Pay üçüncü kişiye satıldığında, ön alım hakkı sahibi aynı koşullarla payı satın "
        "alabilir.\n"
        "- Hak, satışın kendisine bildirilmesinden itibaren **3 ay** ve her hâlde satıştan "
        "itibaren **2 yıl** içinde, **dava açılarak** kullanılır (TMK m.733/3). Bu süreler hak "
        "düşürücüdür.\n\n"
        "**Önemli not:** Ön alım hakkı yalnızca **satış** ve satışa benzer devirlerde işler; "
        "bağış, miras gibi devirlerde kullanılamaz. Paydaşlar arasındaki satışlarda da ön alım "
        "hakkı ileri sürülemez.",
    ),
    (
        "Zilyetlik ile mülkiyet arasındaki fark nedir?",
        "İkisi de eşya üzerindeki durumu ifade eder; ancak biri **fiilî**, diğeri **hukuki** bir "
        "ilişkidir.\n\n"
        "**Mülkiyet (TMK m.683)**\n"
        "- Bir şey üzerindeki en geniş **ayni haktır**; sahibine kullanma, yararlanma ve "
        "tasarruf (devretme, üzerinde hak kurma) yetkisi verir.\n"
        "- Hukuki bir ilişkidir; taşınmazlarda kural olarak **tapu siciline tescil** ile "
        "kazanılır.\n\n"
        "**Zilyetlik (TMK m.973)**\n"
        "- Bir şey üzerinde **fiilî hâkimiyet** kurmuş olmaktır; mülkiyetten bağımsızdır.\n"
        "- Kiracı, ödünç alan veya hatta hırsız bile zilyettir; ama malik değildir.\n\n"
        "**Pratik fark:** Malik aynı zamanda zilyet olabilir; ancak her zilyet malik değildir. "
        "Zilyetlik, mülkiyet karinesi sağlar (TMK m.985: taşınır zilyedi onun maliki sayılır) ve "
        "zilyetliğin korunmasına ilişkin davalar (m.981 vd.) açılabilir.",
    ),
    (
        "Ayni hak ile şahsi (kişisel) hak arasındaki fark nedir?",
        "Bu ayrım, bir hakkın **kime karşı** ileri sürülebileceğine ilişkindir.\n\n"
        "**Ayni hak**\n"
        "- Bir eşya üzerinde doğrudan **hâkimiyet** sağlar ve **herkese karşı** (mutlak) ileri "
        "sürülebilir.\n"
        "- Örnekler: mülkiyet (TMK m.683), intifa hakkı (TMK m.794), rehin/ipotek (TMK m.850 vd.), "
        "geçit hakkı.\n"
        "- Ayni haklar **sınırlı sayı (numerus clausus)** ilkesine tabidir; yalnızca kanunda "
        "öngörülen türler kurulabilir. Taşınmazlarda kural olarak tapuya tescille doğar; sahibine "
        "takip ve öncelik hakkı verir.\n\n"
        "**Şahsi (alacak) hak**\n"
        "- Yalnızca **belirli bir kişiye karşı** (nispi) ileri sürülebilir; bir edimin yerine "
        "getirilmesini isteme yetkisidir.\n"
        "- Örnekler: kira sözleşmesinden doğan haklar, satıştan doğan teslim borcu, alacak.\n\n"
        "**Pratik sonuç:** Eşya el değiştirse bile ayni hak takip eder (ör. ipotekli taşınmaz "
        "satılsa da ipotek devam eder). Şahsi hak ise kural olarak yalnızca borçlusuna karşı "
        "geçerlidir; bu nedenle bazı şahsi haklar (ör. kira) tapuya şerh edilerek güçlendirilir.",
    ),
    (
        "Kesin hüküm ne anlama gelir?",
        "Kesin hüküm (kaziye-i muhkeme), bir uyuşmazlık hakkında verilen ve artık olağan kanun "
        "yollarıyla değiştirilemeyen mahkeme kararının kazandığı kesinlik durumudur. "
        "HMK m.303'te düzenlenir.\n\n"
        "**İki boyutu vardır:**\n"
        "- **Şeklî kesinlik:** Karara karşı başvurulabilecek olağan kanun yollarının "
        "(istinaf, temyiz) tükenmesi veya süresinde başvurulmaması.\n"
        "- **Maddî kesinlik (kesin hüküm etkisi):** Aynı taraflar arasında, aynı dava konusu ve "
        "aynı sebebe dayanan bir uyuşmazlığın **yeniden dava edilememesi** ve verilmiş kararın "
        "sonraki davalarda bağlayıcı olması.\n\n"
        "**Üç unsur (kesin hükmün sınırları):** Tarafların, dava konusunun (müddeabih) ve dava "
        "sebebinin aynı olması gerekir.\n\n"
        "**Sonucu:** Kesin hüküm bulunması bir **dava şartıdır** (HMK m.114/1-i); hâkim bunu "
        "re'sen gözetir ve aynı uyuşmazlık yeniden açılırsa davayı usulden reddeder.",
    ),
    (
        "Derdestlik nedir?",
        "Derdestlik, aynı uyuşmazlık hakkında **görülmekte olan (henüz sonuçlanmamış) bir "
        "davanın** varlığını ifade eder. HMK m.114/1-ı uyarınca, aynı davanın daha önceden açılmış "
        "ve hâlen görülmekte olması bir **dava şartı** eksikliğidir.\n\n"
        "**Amacı:** Aynı taraflar arasında, aynı konu ve sebeple birden fazla davanın yürümesini "
        "ve çelişik kararların çıkmasını önlemektir.\n\n"
        "**Şartları (kesin hükümdekine paralel):**\n"
        "- Tarafların aynı olması,\n"
        "- Dava konusunun aynı olması,\n"
        "- Dava sebebinin aynı olması.\n\n"
        "**Sonucu:** İkinci dava açıldığında derdestlik itirazı ileri sürülürse (veya hâkim "
        "re'sen tespit ederse), sonraki dava **usulden reddedilir**. Kesin hükümden farkı, "
        "burada ilk davanın henüz **derdest** (devam ediyor) olmasıdır; kesin hükümde ise dava "
        "kesinleşmiş bir kararla sonuçlanmıştır.",
    ),
    (
        "Kusursuz sorumluluk nedir?",
        "Kusursuz sorumluluk, bir kişinin **kusuru bulunmasa bile** belirli bir zarardan sorumlu "
        "tutulması hâlidir. Kusurun şart olduğu genel haksız fiil sorumluluğunun (TBK m.49) "
        "istisnasıdır.\n\n"
        "**Başlıca türleri:**\n"
        "- **Hakkaniyet sorumluluğu (TBK m.65):** Ayırt etme gücü bulunmayan kişinin verdiği "
        "zararın hakkaniyet gereği kısmen/tamamen tazmini.\n"
        "- **Özen (gözetim) sorumluluğu:** Adam çalıştıranın sorumluluğu (TBK m.66), ev başkanının "
        "sorumluluğu, hayvan bulunduranın sorumluluğu (TBK m.67).\n"
        "- **Tehlike sorumluluğu (TBK m.71):** Önemli ölçüde tehlike arz eden bir işletmenin "
        "faaliyetinden doğan zararlardan, kusur aranmaksızın işletme sahibinin sorumluluğu.\n\n"
        "**Mantığı:** Tehlike yaratan veya başkasını çalıştırarak yarar sağlayan kişinin, bundan "
        "doğan riski de üstlenmesi (\"yarar-riziko\" ilkesi) esas alınır. Bu sorumluluklarda "
        "genellikle illiyet bağının kesilmesi (mücbir sebep, zarar görenin veya üçüncü kişinin "
        "ağır kusuru) dışında kurtuluş imkânı sınırlıdır.",
    ),
    (
        "Defi ile itiraz arasındaki fark nedir?",
        "İkisi de davalının kendisini savunma yollarıdır; ancak hâkimin bunları dikkate alış "
        "biçimi farklıdır.\n\n"
        "**İtiraz**\n"
        "- Davanın veya talebin **doğmadığını ya da hiç var olmadığını** ileri sürer (ör. "
        "borcun hiç doğmaması, tarafların yetkisizliği, kesin hüküm).\n"
        "- Hâkim tarafından **re'sen** (taraf ileri sürmese de) dikkate alınır.\n\n"
        "**Defi**\n"
        "- Hakkın **var olduğunu kabul eder**, ancak onun ileri sürülmesini önleyen bir "
        "karşı-hak ileri sürer (ör. zamanaşımı defi — TBK m.161, ödemezlik defi — TBK m.97, "
        "takas defi — TBK m.139).\n"
        "- Hâkim tarafından **kendiliğinden dikkate alınmaz**; ilgili tarafın açıkça ileri "
        "sürmesi gerekir; bazı defiler (zamanaşımı gibi) feragate konu olabilir.\n\n"
        "**Pratik sonuç:** Bir savunmanın itiraz mı yoksa defi mi olduğu, onu kimin ve ne zaman "
        "ileri sürmesi gerektiğini belirler — örneğin zamanaşımı definin cevap dilekçesinde "
        "açıkça ileri sürülmesi gerekirken, görevsizlik itirazı hâkim tarafından kendiliğinden "
        "gözetilebilir.",
    ),
    (
        "Takas (mahsup) nedir?",
        "Takas, karşılıklı ve birbirine benzer (genellikle para) borcu bulunan iki kişiden "
        "birinin, kendi alacağını borcuyla **karşılıklı olarak sona erdirmesi** imkânı veren bir "
        "kurumdur (TBK m.139 vd.).\n\n"
        "**Şartları (TBK m.140):**\n"
        "- İki taraf **birbirine karşı** alacaklı ve borçlu olmalı,\n"
        "- Her iki borç da **aynı cins** (genellikle para veya türdeş eşya) olmalı,\n"
        "- Takas isteyenin alacağı **muaccel** olmalı (karşı tarafın borcunun muacceliyeti "
        "şart değildir).\n\n"
        "**İşleyişi:** Takas, kendiliğinden gerçekleşmez; taraflardan birinin karşı tarafa "
        "**bildirimde bulunmasıyla** (tek taraflı yenilik doğuran beyan) sonuç doğurur ve "
        "borçlar, takas beyanının yapıldığı andan değil, **takasa elverişli hâle geldikleri "
        "andan itibaren** sona ermiş sayılır (TBK m.145).\n\n"
        "**Örnek:** A'nın B'den 10.000 TL alacağı, B'nin de A'dan 6.000 TL alacağı varsa, "
        "taraflardan biri takas beyanında bulunduğunda B'nin borcu tamamen, A'nın borcu ise "
        "kısmen (4.000 TL'ye) sona erer.",
    ),
    (
        "Tahkim nedir, mahkemeye gitmekten farkı ne?",
        "Tahkim, tarafların aralarındaki bir uyuşmazlığı, devlet mahkemeleri yerine "
        "**özel hakemler** eliyle çözümlemeyi kararlaştırdıkları alternatif bir uyuşmazlık "
        "çözüm yoludur. İç hukukta Hukuk Muhakemeleri Kanunu m.407 vd., yabancılık unsuru "
        "taşıyan uyuşmazlıklarda ise 4686 sayılı Milletlerarası Tahkim Kanunu uygulanır.\n\n"
        "**Mahkemeden farkları:**\n"
        "- **Kaynağı:** Tahkim, tarafların **tahkim sözleşmesi** ile iradi olarak seçtiği bir "
        "yoldur; mahkemeye başvuru ise kanuni bir haktır.\n"
        "- **Karar verenler:** Devlet hâkimi yerine, tarafların seçtiği veya belirlenmesini "
        "kararlaştırdığı **hakem(ler)** karar verir.\n"
        "- **Kanun yolu:** Hakem kararlarına karşı istinaf/temyiz yerine sınırlı sebeplerle "
        "**iptal davası** açılabilir (HMK m.439).\n"
        "- **Gizlilik ve hız:** Tahkim genellikle daha hızlı sonuçlanır ve kamuya açık "
        "değildir; ticari uyuşmazlıklarda sıkça tercih edilir.\n\n"
        "**Önemli sınır:** Tahkim, tarafların **üzerinde serbestçe tasarruf edebileceği** "
        "haklara ilişkin uyuşmazlıklarla sınırlıdır (HMK m.408); örneğin boşanma, velayet gibi "
        "ayni nitelikte olmayan ve kamu düzenini ilgilendiren konularda tahkim mümkün değildir.",
    ),
    (
        "Hapis hakkı nedir?",
        "Hapis hakkı, alacaklıya, **borçluya ait bir taşınırı veya kıymetli evrakı elinde "
        "tutarak alacağı ödenene kadar geri vermeme** yetkisi tanıyan bir güvence (teminat) "
        "hakkıdır (TMK m.950 vd.).\n\n"
        "**Şartları:**\n"
        "- Alacaklının, borçluya ait bir şey üzerinde **rızaen ve hukuka uygun** bir biçimde "
        "zilyetliği bulunmalı,\n"
        "- Alacak **muaccel** olmalı,\n"
        "- Şeyin niteliği ile alacak arasında **bağlantı** bulunmalı (örn. tamir için "
        "bırakılan eşyanın tamircide kalması) — tacirler arasında bu bağlantı şartı aranmaz "
        "(TMK m.951).\n\n"
        "**Sonucu:** Hapis hakkı sahibi, alacağını alana kadar şeyi geri vermeyi reddedebilir; "
        "borçlu iflas ederse veya ödeme yapmazsa, alacaklı şeyi **rehinmiş gibi paraya "
        "çevirme** yetkisine de sahiptir (TMK m.953).\n\n"
        "**Örnek:** Aracını tamir ettiren bir kişi tamir bedelini ödemezse, tamirci aracı "
        "hapis hakkına dayanarak elinde tutabilir.",
    ),
    (
        "Nispi (göreceli) butlan ile mutlak butlan arasındaki fark nedir?",
        "İkisi de bir hukuki işlemin **geçersizliğine** yol açar, ancak etki alanı ve "
        "sonuçları farklıdır.\n\n"
        "**Mutlak butlan (kesin hükümsüzlük)**\n"
        "- Kanunun emredici hükümlerine, ahlaka, kamu düzenine veya kişilik haklarına "
        "aykırılık ya da konunun imkânsızlığı gibi **ağır sakatlıklarda** söz konusu "
        "olur (TBK m.27).\n"
        "- **Herkes** ileri sürebilir, hâkim **re'sen** dikkate alır, **süreye tabi "
        "değildir**.\n\n"
        "**Nispi butlan (iptal edilebilirlik)**\n"
        "- İrade sakatlıkları (yanılma, aldatma, korkutma — TBK m.30-39) gibi, yalnızca "
        "**korunması amaçlanan tarafın menfaatini** ilgilendiren sakatlıklarda söz "
        "konusu olur.\n"
        "- Yalnızca **korunan taraf** iptal hakkını kullanabilir; bu hak **bir yıllık "
        "hak düşürücü süreye** tabidir (TBK m.39) ve süre geçince işlem geçerli "
        "hâle gelir (icazet).\n\n"
        "**Pratik fark:** Mutlak butlanda işlem baştan itibaren ve herkese karşı "
        "geçersizdir; nispi butlanda ise işlem, hak sahibi süresinde iptal etmedikçe "
        "geçerliliğini korur — yani \"sakat ama düzeltilebilir\" bir durumdur.",
    ),
    (
        "Sebep-sonuç (illiyet) bağı nedir, neden tazminat hukukunda bu kadar önemli?",
        "İlliyet (nedensellik) bağı, bir kişinin eylemi (veya eylemsizliği) ile ortaya "
        "çıkan zarar arasındaki **sebep-sonuç ilişkisini** ifade eder ve tazminat "
        "sorumluluğunun kurucu unsurlarından biridir (TBK m.49 vd.).\n\n"
        "**Neden bu kadar önemli?**\n"
        "Bir kişinin kusurlu veya hukuka aykırı bir davranışı bulunsa bile, zarar "
        "**bu davranıştan değil başka bir sebepten** doğmuşsa, o kişi zarardan "
        "sorumlu tutulamaz. İlliyet bağı, sorumluluğun sınırlarını çizen bir "
        "**filtre** görevi görür.\n\n"
        "**İlliyet bağını kesen sebepler:**\n"
        "- **Mücbir sebep** (deprem, sel gibi öngörülemez ve karşı konulamaz "
        "olaylar),\n"
        "- **Zarar görenin ağır kusuru**,\n"
        "- **Üçüncü kişinin ağır kusuru**.\n\n"
        "Bu sebeplerden biri zararın **asıl ve belirleyici** nedeni hâline gelmişse, "
        "failin davranışıyla zarar arasındaki bağ kopar ve sorumluluk —tam veya "
        "kısmen— ortadan kalkabilir (TBK m.51-52).\n\n"
        "**Örnek:** Bir sürücü kırmızı ışıkta geçse bile, kazaya asıl sebep aniden "
        "yola fırlayan bir kişiyse, illiyet bağı bu üçüncü kişinin davranışına "
        "kayabilir ve sürücünün sorumluluğu azalabilir veya kalkabilir.",
    ),
    (
        "Hakkın kötüye kullanılması yasağı (TMK m.2) somut olarak ne anlama gelir, "
        "örnek verir misiniz?",
        "TMK m.2/2'de düzenlenen bu ilke, **biçimsel olarak var olan bir hakkın**, "
        "açıkça **dürüstlük kuralına aykırı** biçimde kullanılması hâlinde hukuk "
        "düzeni tarafından korunmayacağını ifade eder.\n\n"
        "**Unsurları:**\n"
        "- Kişinin elinde **biçimsel olarak bir hak** bulunmalı,\n"
        "- Bu hak, **açıkça** (bariz şekilde) amacının dışında, başkasına zarar "
        "vermek veya haksız bir menfaat sağlamak amacıyla kullanılmalı,\n"
        "- Hakkın bu şekilde kullanılması ile elde edilecek yarar ile karşı tarafa "
        "verdiği zarar arasında **açık bir oransızlık** bulunmalı.\n\n"
        "**Örnekler:**\n"
        "- Bir alacaklının, çok küçük bir miktar borç için borçlunun tüm "
        "malvarlığını haczettirmesi,\n"
        "- Kiraya verenin, yıllarca sorun çıkarmadığı bir tahliye taahhüdüne "
        "yıllar sonra, sırf kiracıyı zor durumda bırakmak için dayanması,\n"
        "- Bir mirasçının, sırf diğer mirasçıyı mağdur etmek amacıyla, kendisine "
        "hiçbir somut yararı olmayan bir paylaşım talebinde ısrar etmesi.\n\n"
        "**Sonucu:** Hâkim, böyle bir durumu tespit ederse hakkın kullanılmasını "
        "**korumaz**; yani hak biçimsel olarak var olsa da, mahkeme bu hakka "
        "dayanan talebi reddedebilir. Bu nedenle TMK m.2, tüm özel hukuk "
        "ilişkilerinde bir **denge ve denetim mekanizması** işlevi görür.",
    ),
    (
        "Zamanaşımı ile hak düşürücü süre arasındaki fark nedir?",
        "Her iki kavram da belirli bir süre geçince hakkın ya da talep yetkisinin "
        "etkilenmesiyle ilgilidir; ancak hukuki nitelikleri ve sonuçları farklıdır.\n\n"
        "**Zamanaşımı**\n"
        "- Kaynağı: TBK m.146 vd. (genel 10 yıl); özel düzenlemeler farklı süreler belirler "
        "(örn. haksız fiil için TBK m.72: 2 yıl/10 yıl).\n"
        "- Niteliği: Defi niteliğindedir — alacaklının alacak hakkı varlığını korur; yalnızca "
        "borçlu zamanaşımı defini ileri sürerse mahkeme dikkate alır. Hâkim resen gözetemez.\n"
        "- Sonucu: Borç sona ermez, sadece 'doğal borç'a (TBK m.78) dönüşür; borçlu "
        "gönüllü öderse bunu geri alamaz.\n"
        "- Kesilmesi ve durması: TBK m.153-161 kapsamında belirli olaylarla (dava açma, "
        "icra takibi, borçlunun ikrarı) kesilebilir veya durabilir.\n\n"
        "**Hak Düşürücü Süre**\n"
        "- Kaynağı: Kanunla belirlenir (örn. iptal davası için TMK m.156: 1 yıl; "
        "tapu tescil talebi için bazı özel düzenlemeler).\n"
        "- Niteliği: Hakkı doğrudan sona erdirir — süre geçince hak yokluğu söz konusudur. "
        "Hâkim resen gözetmek zorundadır.\n"
        "- Sonucu: Süre geçince hak tamamen ortadan kalkar; borçlunun gönüllü ödemesi de "
        "hukuki dayanak kalmayacağından iade edilebilir.\n"
        "- Kesilmesi ve durması: Kural olarak kesilmez ve durmaz.\n\n"
        "**Özet Karşılaştırma**\n"
        "| Özellik | Zamanaşımı | Hak Düşürücü Süre |\n"
        "|---|---|---|\n"
        "| Hâkim resen gözetir mi? | Hayır | Evet |\n"
        "| Hak sona erer mi? | Hayır (defi) | Evet |\n"
        "| Kesilebilir mi? | Evet | Kural olarak hayır |\n"
        "| Hukuki dayanağı | TBK m.146+ | İlgili özel kanun |",
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
