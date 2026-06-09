"""
Seed — Kategori 4: Karar Özeti / Analizi
========================================
Mahkeme kararlarının yapılandırılmış, kaynaklı özetleri.
Kullanıcı karar metnini verir; asistan rehberdeki başlık şablonuyla özetler.
(Esas/Karar numaraları örnek/temsilîdir; hukuki ilkeler gerçektir.)

    python seeds/seed_karar_ozeti.py
    python akai_dataset_generator.py --mode import --file seeds/seed_karar_ozeti.json
"""

import json
from pathlib import Path

CATEGORY = "karar_ozeti"
SOURCE = "claude_seed"
OUT_FILE = Path(__file__).with_name("seed_karar_ozeti.json")

PAIRS = [
    (
        "Şu kararı özetle:\n\nYargıtay 9. Hukuk Dairesi, E. 2022/XXXX, K. 2023/YYYY. "
        "Davacı işçi, performans düşüklüğü gerekçesiyle işten çıkarıldığını, ancak kendisine "
        "önceden savunma hakkı tanınmadığını ve somut performans kriteri gösterilmediğini ileri "
        "sürerek işe iade istemiştir. Yerel mahkeme feshi geçerli sayarak davayı reddetmiş; "
        "Yargıtay, işverenin geçerli sebebi somut ve objektif verilerle ispatlayamadığını, ayrıca "
        "savunma alınmadığını belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 9. Hukuk Dairesi\n"
        "**Esas / Karar**: 2022/XXXX — 2023/YYYY\n\n"
        "**Uyuşmazlık konusu**: Performans düşüklüğüne dayalı feshin geçerli bir nedene dayanıp "
        "dayanmadığı ve işe iade talebinin yerindeliği.\n\n"
        "**Yerel mahkeme kararı**: Feshi geçerli kabul ederek işe iade davasını reddetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- İş Kanunu m.18 uyarınca geçerli sebebe dayanma yükü işverendedir; performans düşüklüğü "
        "soyut iddia ile değil, **somut ve objektif kriterlerle** ispatlanmalıdır.\n"
        "- Davranış veya yeterlilikten kaynaklanan fesihlerde işçinin **savunmasının alınması** "
        "zorunludur (m.19/2); bu yapılmadığından fesih usulen de geçersizdir.\n\n"
        "**Sonuç**: Bozma — Feshin geçerli nedene dayanmadığı ve savunma alınmadığı gerekçesiyle "
        "yerel mahkeme kararı bozulmuştur.\n\n"
        "**Emsal niteliği**: Performansa dayalı fesihlerde ispat yükünün işverende olduğu ve "
        "savunma alınmasının geçerlilik şartı olduğu yönünde emsal teşkil eder.",
    ),
    (
        "Bu kararı özetler misin?\n\nYargıtay 2. Hukuk Dairesi, E. 2021/XXXX, K. 2022/YYYY. "
        "Çekişmeli boşanma davasında yerel mahkeme tarafları eşit kusurlu kabul ederek tazminat "
        "taleplerini reddetmiştir. Davacı kadın, davalının sadakat yükümlülüğüne aykırı "
        "davrandığını ve ekonomik şiddet uyguladığını, kendisine ise herhangi bir kusur "
        "yüklenemeyeceğini ileri sürmüştür. Yargıtay, toplanan delillere göre davalı erkeğin ağır "
        "kusurlu olduğunu, kadına kusur yüklenemeyeceğini belirterek tazminat yönünden kararı "
        "bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 2. Hukuk Dairesi\n"
        "**Esas / Karar**: 2021/XXXX — 2022/YYYY\n\n"
        "**Uyuşmazlık konusu**: Boşanmada kusur dağılımı ve buna bağlı maddi-manevi tazminat "
        "talebinin değerlendirilmesi.\n\n"
        "**Yerel mahkeme kararı**: Tarafları eşit kusurlu sayarak tazminat taleplerini "
        "reddetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- TMK m.174 uyarınca maddi ve manevi tazminata hükmedilebilmesi için talep edenin "
        "**kusursuz veya daha az kusurlu** olması gerekir.\n"
        "- Dosyadaki delillere göre sadakat yükümlülüğüne aykırılık ve ekonomik şiddet nedeniyle "
        "**davalı erkek ağır kusurludur**; kadına kusur izafe edilemez. Eşit kusur tespiti "
        "hatalıdır.\n\n"
        "**Sonuç**: Bozma (tazminat yönünden) — Kusur dağılımının hatalı belirlendiği gerekçesiyle "
        "karar bozulmuştur.\n\n"
        "**Emsal niteliği**: Kusur dağılımının tazminat hakkını doğrudan etkilediği ve eşit kusur "
        "tespitinin somut delillerle bağdaşması gerektiği yönünde emsaldir.",
    ),
    (
        "Karar özeti çıkarır mısın:\n\nYargıtay 3. Hukuk Dairesi, E. 2020/XXXX, K. 2021/YYYY. "
        "Kira tespiti davasında kiraya veren, 8 yıldır aynı kiracıda olan taşınmaz için kira "
        "bedelinin emsallere göre çok düşük kaldığını ileri sürmüştür. Yerel mahkeme yalnızca ÜFE "
        "artışını uygulayarak talebi sınırlamıştır. Yargıtay, beş yıldan uzun süren kira "
        "ilişkilerinde hâkimin hakkaniyete ve emsal kira bedellerine göre tespit yapması "
        "gerektiğini belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 3. Hukuk Dairesi\n"
        "**Esas / Karar**: 2020/XXXX — 2021/YYYY\n\n"
        "**Uyuşmazlık konusu**: Uzun süreli kira ilişkisinde kira bedelinin tespitinde "
        "uygulanacak ölçüt.\n\n"
        "**Yerel mahkeme kararı**: Kira artışını yalnızca üretici/tüketici fiyat endeksi oranıyla "
        "sınırlandırmıştır.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- TBK m.344 uyarınca, beş yıldan uzun süren veya beş yıldan sonra yenilenen kira "
        "ilişkilerinde hâkim; endeks oranı, kiralananın durumu ve **emsal kira bedellerini** göz "
        "önünde tutarak **hakkaniyete** göre tespit yapar.\n"
        "- Salt endeks artışıyla sınırlama, uzun süreli kirada bu hükmün amacına aykırıdır.\n\n"
        "**Sonuç**: Bozma — Kira tespitinin hakkaniyet ve emsal değerlendirmesi yapılmadan "
        "belirlenmesi nedeniyle bozulmuştur.\n\n"
        "**Emsal niteliği**: Beş yılı aşan kira ilişkilerinde tespit davasında endeksin tek "
        "ölçüt olmayacağı, hakkaniyet incelemesi gerektiği yönünde emsaldir.",
    ),
    (
        "Şu kararı kısaca özetle:\n\nYargıtay 4. Hukuk Dairesi, E. 2019/XXXX, K. 2020/YYYY. "
        "Trafik kazası sonucu yaralanan davacı, maddi ve manevi tazminat talep etmiştir. Yerel "
        "mahkeme, davacının da kazada %25 kusurlu olduğunu kabul ederek tazminattan indirim "
        "yapmış ancak manevi tazminatı reddetmiştir. Yargıtay, bedensel zararlarda manevi "
        "tazminatın koşullarının oluştuğunu, müterafik kusurun yalnızca miktarda indirim sebebi "
        "olabileceğini belirterek manevi tazminatın reddini hatalı bulmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 4. Hukuk Dairesi\n"
        "**Esas / Karar**: 2019/XXXX — 2020/YYYY\n\n"
        "**Uyuşmazlık konusu**: Trafik kazasında müterafik (zarar görenin) kusurun manevi "
        "tazminata etkisi.\n\n"
        "**Yerel mahkeme kararı**: Davacının %25 kusuru nedeniyle maddi tazminattan indirim "
        "yapmış, manevi tazminat talebini ise reddetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- TBK m.56 uyarınca bedensel bütünlüğün ihlalinde hâkim, mağdura manevi tazminat "
        "verebilir; yaralanmanın varlığı ve ağırlığı bu koşulu oluşturur.\n"
        "- Zarar görenin kusuru (TBK m.52) tazminattan **indirim** sebebidir; manevi tazminatın "
        "tümden reddini gerektirmez.\n\n"
        "**Sonuç**: Bozma (manevi tazminat yönünden) — Manevi tazminatın koşulları oluştuğu hâlde "
        "reddedilmesi hatalı bulunmuştur.\n\n"
        "**Emsal niteliği**: Müterafik kusurun manevi tazminatı tümden ortadan kaldırmayıp yalnızca "
        "miktarda indirim sebebi olduğu yönünde emsaldir.",
    ),
    (
        "Bu kararı özetle:\n\nYargıtay 3. Hukuk Dairesi, E. 2021/XXXX, K. 2022/YYYY. "
        "Sıfır kilometre satın alınan araçta motor arızası çıkması üzerine tüketici, aracın ayıpsız "
        "misliyle değiştirilmesini talep etmiştir. Satıcı, arızanın giderilebilir olduğunu "
        "savunmuştur. Yerel mahkeme onarımla yetinilmesine karar vermiştir. Yargıtay, ayıbın "
        "önemli ve aracın güvenli kullanımını etkileyen nitelikte olduğunu, tüketicinin seçimlik "
        "haklarını serbestçe kullanabileceğini belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 3. Hukuk Dairesi\n"
        "**Esas / Karar**: 2021/XXXX — 2022/YYYY\n\n"
        "**Uyuşmazlık konusu**: Ayıplı araçta tüketicinin seçimlik haklarından hangisinin "
        "uygulanacağı.\n\n"
        "**Yerel mahkeme kararı**: Tüketicinin değiştirme talebine rağmen onarımla yetinilmesine "
        "hükmetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- 6502 sayılı Kanun m.11 uyarınca tüketici; sözleşmeden dönme, bedelden indirim, ücretsiz "
        "onarım veya **ayıpsız misliyle değiştirme** haklarından birini **serbestçe** seçebilir.\n"
        "- Ayıp önemli ve aracın güvenli kullanımını etkiliyorsa, satıcı tüketiciyi onarıma "
        "zorlayamaz.\n\n"
        "**Sonuç**: Bozma — Tüketicinin seçimlik hakkını kısıtlayan karar hatalı bulunmuştur.\n\n"
        "**Emsal niteliği**: Ayıplı malda seçimlik hakkın tüketiciye ait olduğu ve satıcının "
        "onarımı dayatamayacağı yönünde emsaldir.",
    ),
    (
        "Karar özetini çıkar:\n\nYargıtay 12. Hukuk Dairesi, E. 2020/XXXX, K. 2021/YYYY. "
        "Kambiyo senedine (bonoya) dayalı icra takibinde borçlu, senetteki imzanın kendisine ait "
        "olmadığını ileri sürerek imzaya itiraz etmiştir. İcra mahkemesi bilirkişi incelemesi "
        "yaptırmadan itirazı reddetmiştir. Yargıtay, imza itirazında bilirkişi incelemesi "
        "yapılmasının zorunlu olduğunu belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 12. Hukuk Dairesi\n"
        "**Esas / Karar**: 2020/XXXX — 2021/YYYY\n\n"
        "**Uyuşmazlık konusu**: Kambiyo senedine dayalı takipte imzaya itiraz hâlinde inceleme "
        "usulü.\n\n"
        "**Yerel mahkeme kararı**: İcra mahkemesi, bilirkişi (imza) incelemesi yaptırmadan imzaya "
        "itirazı reddetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- İİK m.170 uyarınca kambiyo senedindeki imzaya itiraz edilmesi hâlinde, icra mahkemesi "
        "imzanın borçluya ait olup olmadığını **bilirkişi incelemesiyle** belirlemek zorundadır.\n"
        "- İnceleme yaptırılmadan verilen ret kararı eksik incelemeye dayanmaktadır.\n\n"
        "**Sonuç**: Bozma — İmza incelemesi yaptırılmaması nedeniyle karar bozulmuştur.\n\n"
        "**Emsal niteliği**: Kambiyo takibinde imza itirazının mutlaka bilirkişi incelemesiyle "
        "çözülmesi gerektiği yönünde emsaldir.",
    ),
    (
        "Bu kararı özetler misin:\n\nYargıtay 3. Hukuk Dairesi, E. 2021/XXXX, K. 2022/YYYY. "
        "Davacı kiracı, kiraya verenin kira sözleşmesinde belirlenen TÜFE artış oranının çok "
        "üzerinde bir bedel talep ettiğini ileri sürerek kira tespiti istemiştir. Yerel mahkeme, "
        "5 yılı aşan kira ilişkisi bulunmadığını gözardı ederek doğrudan emsal kira bedeli "
        "üzerinden karar vermiş; Yargıtay, kira süresinin 5 yılı aşıp aşmadığının tartışılması "
        "gerektiğini belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 3. Hukuk Dairesi\n"
        "**Esas / Karar**: 2021/XXXX — 2022/YYYY\n\n"
        "**Uyuşmazlık konusu**: Kira tespit davasında uygulanacak ölçütün, kira ilişkisinin "
        "süresine göre TÜFE sınırı mı yoksa hakkaniyete göre emsal kira bedeli mi olduğu.\n\n"
        "**Yerel mahkeme kararı**: Kira ilişkisinin süresini tartışmadan doğrudan emsal kira "
        "bedeli üzerinden tespit kararı vermiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- TBK m.344 uyarınca, **beş yıldan kısa süren** kira ilişkilerinde belirlenecek kira "
        "bedeli, bir önceki kira yılındaki TÜFE artış oranını geçemez.\n"
        "- Hâkimin hakkaniyete göre ve emsal kira bedellerini dikkate alarak karar "
        "verebilmesi, ancak **beş yılı aşan** kira ilişkilerinde mümkündür (TBK m.344/3).\n"
        "- Yerel mahkeme, kira ilişkisinin beş yılı aşıp aşmadığını tartışmadan doğrudan "
        "emsal bedel esasını uygulayarak hatalı karar vermiştir.\n\n"
        "**Sonuç**: Bozma — Kira süresinin tespit edilmeden hatalı ölçüt uygulanması nedeniyle "
        "karar bozulmuştur.\n\n"
        "**Emsal niteliği**: Kira tespit davalarında uygulanacak ölçütün kira ilişkisinin beş "
        "yılı aşıp aşmadığına göre belirlenmesi gerektiği yönünde emsaldir (TBK m.344).",
    ),
    (
        "Şu özeti çıkarır mısın:\n\nYargıtay Hukuk Genel Kurulu, E. 2020/XXXX, K. 2021/YYYY. "
        "Davacı, trafik kazasında aracının hasarlandığını, sigorta şirketinin eksper raporuna "
        "dayanarak ödeme yaptığını ancak değer kaybı tazminatını ayrıca ödemediğini ileri "
        "sürerek dava açmıştır. Yerel mahkeme, hasar bedelinin ödenmesiyle tüm zararın "
        "karşılandığı gerekçesiyle davayı reddetmiş; Hukuk Genel Kurulu, değer kaybının hasar "
        "bedelinden bağımsız ayrı bir zarar kalemi olduğunu vurgulayarak kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay Hukuk Genel Kurulu\n"
        "**Esas / Karar**: 2020/XXXX — 2021/YYYY\n\n"
        "**Uyuşmazlık konusu**: Trafik kazası sonucu aracın onarılmış olmasının, ayrıca "
        "**değer kaybı** tazminatı talep etmeye engel olup olmadığı.\n\n"
        "**Yerel mahkeme kararı**: Onarım/hasar bedelinin ödenmesiyle zararın tamamen "
        "karşılandığı gerekçesiyle değer kaybı talebini reddetmiştir.\n\n"
        "**Hukuk Genel Kurulu değerlendirmesi**:\n"
        "- Bir aracın kaza geçirmiş ve onarılmış olması, piyasa değerinde **kalıcı bir "
        "azalmaya** (değer kaybına) yol açar; bu, onarım giderinden bağımsız, ayrı ve gerçek "
        "bir zarar kalemidir (TBK m.49).\n"
        "- Zarar görenin malvarlığında oluşan bu eksilmenin tazmin edilmemesi, **tam tazmin "
        "ilkesine** aykırılık oluşturur.\n"
        "- Değer kaybı miktarının aracın markası, modeli, hasar derecesi ve piyasa "
        "koşulları dikkate alınarak bilirkişi incelemesiyle belirlenmesi gerekir.\n\n"
        "**Sonuç**: Bozma — Değer kaybı talebinin ayrı bir zarar kalemi olarak "
        "değerlendirilmemesi nedeniyle karar bozulmuştur.\n\n"
        "**Emsal niteliği**: Trafik kazalarında değer kaybının, onarım bedelinden bağımsız "
        "ayrı bir tazminat kalemi olarak talep edilebileceği yönünde yerleşik içtihattır.",
    ),
    (
        "Bu Yargıtay kararını özetle:\n\nYargıtay 13. Hukuk Dairesi, E. 2022/XXXX, K. 2023/YYYY. "
        "Davacı tüketici, ayıplı çıkan bir cep telefonunu satıcıya iade etmek istediğini, "
        "ancak satıcının yalnızca tamir teklif ettiğini belirterek bedel iadesi talep "
        "etmiştir. Yerel mahkeme, satıcının tamir seçeneğini sunmasının yeterli olduğu "
        "gerekçesiyle davayı reddetmiş; Yargıtay, seçimlik hakların tüketiciye ait olduğunu "
        "belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 13. Hukuk Dairesi\n"
        "**Esas / Karar**: 2022/XXXX — 2023/YYYY\n\n"
        "**Uyuşmazlık konusu**: Ayıplı maldan doğan seçimlik hakların kim tarafından "
        "kullanılacağı — satıcı mı yoksa tüketici mi tercih eder.\n\n"
        "**Yerel mahkeme kararı**: Satıcının ücretsiz onarım imkânı sunmasını yeterli "
        "görerek bedel iadesi talebini reddetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- 6502 sayılı Kanun m.11 uyarınca, malın ayıplı çıkması hâlinde tüketici; "
        "sözleşmeden dönme (bedel iadesi), bedelden indirim, ücretsiz onarım veya "
        "ayıpsız misli ile değiştirme seçimlik haklarından dilediğini **kendisi seçmekte "
        "serbesttir**.\n"
        "- Bu seçim hakkı satıcıya değil, tüketiciye aittir; satıcının tek taraflı olarak "
        "onarımı dayatması kanuna aykırıdır.\n"
        "- Tüketicinin sözleşmeden dönme hakkını kullanması hâlinde satıcı, malı geri "
        "alıp bedeli iade etmekle yükümlüdür.\n\n"
        "**Sonuç**: Bozma — Seçimlik hakkın tüketiciye değil satıcıya bırakılması nedeniyle "
        "karar bozulmuştur.\n\n"
        "**Emsal niteliği**: Ayıplı malda seçimlik hakların satıcı tarafından "
        "sınırlandırılamayacağı, tercihin tüketiciye ait olduğu yönünde emsaldir (6502 m.11).",
    ),
    (
        "Şu kararı özetler misin:\n\nYargıtay 4. Hukuk Dairesi, E. 2021/XXXX, K. 2022/YYYY. "
        "Davacı, sosyal medyada hakkında asılsız ve aşağılayıcı paylaşımlar yapıldığını "
        "ileri sürerek manevi tazminat talep etmiştir. Yerel mahkeme, paylaşımların "
        "\"eleştiri sınırları içinde\" olduğu gerekçesiyle davayı reddetmiş; Yargıtay, "
        "ifadelerin eleştiri boyutunu aştığını ve kişilik haklarına saldırı oluşturduğunu "
        "belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 4. Hukuk Dairesi\n"
        "**Esas / Karar**: 2021/XXXX — 2022/YYYY\n\n"
        "**Uyuşmazlık konusu**: Sosyal medya paylaşımlarının ifade özgürlüğü/eleştiri "
        "sınırları içinde mi kaldığı, yoksa kişilik haklarına saldırı mı oluşturduğu.\n\n"
        "**Yerel mahkeme kararı**: Paylaşımları eleştiri sınırları içinde değerlendirerek "
        "manevi tazminat talebini reddetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- İfade özgürlüğü anayasal güvence altında olmakla birlikte, eleştirinin "
        "**kişiyi hedef alan aşağılama, hakaret veya asılsız isnatlara** dönüşmesi "
        "hâlinde TMK m.24-25 kapsamında kişilik haklarına saldırı oluşur.\n"
        "- Eleştiri ile hakaretin sınırı; ifadenin **konuyla ilgili, ölçülü ve "
        "gerçeklere dayalı** olup olmadığına göre belirlenir; kişiyi küçük düşürmeyi "
        "amaçlayan ifadeler bu sınırı aşar.\n"
        "- Somut olayda paylaşımların içeriği, üslubu ve yaygınlık derecesi dikkate "
        "alındığında bunların salt eleştiri olmaktan çıkıp **saldırı niteliği** "
        "kazandığı tespit edilmiştir.\n\n"
        "**Sonuç**: Bozma — Paylaşımların kişilik haklarına saldırı oluşturduğu "
        "gözetilmeden karar verilmesi nedeniyle yerel mahkeme kararı bozulmuştur.\n\n"
        "**Emsal niteliği**: Sosyal medyada yapılan paylaşımların eleştiri ile kişilik "
        "haklarına saldırı arasındaki sınırının; ifadenin ölçülülüğü, gerçekliği ve "
        "amacına göre belirlenmesi gerektiği yönünde emsaldir (TMK m.24-25).",
    ),
    (
        "Bu kararı özetler misin:\n\nYargıtay 6. Hukuk Dairesi, E. 2020/XXXX, K. 2021/YYYY. "
        "Davacı kiracı, kiraya verenin kendisine haber vermeden kiralananın anahtarını "
        "değiştirip eşyalarını dışarı çıkardığını, bunun hukuka aykırı bir tahliye olduğunu "
        "ileri sürerek tazminat talep etmiştir. Yerel mahkeme, kiracının kira borcunu "
        "ödemediğini gerekçe göstererek davayı reddetmiş; Yargıtay, kiraya verenin "
        "kendiliğinden tahliye yapamayacağını belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 6. Hukuk Dairesi\n"
        "**Esas / Karar**: 2020/XXXX — 2021/YYYY\n\n"
        "**Uyuşmazlık konusu**: Kiraya verenin, kira borcu bulunsa dahi mahkeme kararı "
        "olmaksızın kiracıyı kendiliğinden (\"kilit değiştirerek\") tahliye edip "
        "edemeyeceği.\n\n"
        "**Yerel mahkeme kararı**: Kiracının kira borcu bulunduğunu gerekçe göstererek "
        "tazminat talebini reddetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- Kira borcunun varlığı, kiraya verene **kendiliğinden el koyma ve tahliye** "
        "hakkı vermez; tahliye, ancak kanunda öngörülen yargısal yollarla (icra takibi, "
        "tahliye davası, TBK m.315) gerçekleştirilebilir.\n"
        "- Kiraya verenin kilidi değiştirip eşyaları çıkarması, **zilyetliğe karşı "
        "saldırı** (TMK m.981) ve aynı zamanda haksız fiil (TBK m.49) niteliğindedir; "
        "kiracının bu nedenle uğradığı zararların tazmini gerekir.\n"
        "- Kira borcunun varlığı, ancak kiraya verenin **karşı dava veya def'i yoluyla** "
        "ileri sürebileceği bir husustur; kendiliğinden yapılan haksız tahliyeyi "
        "meşrulaştırmaz.\n\n"
        "**Sonuç**: Bozma — Kiraya verenin kendiliğinden tahliye eyleminin hukuka "
        "aykırılığı gözetilmeden karar verilmesi nedeniyle yerel mahkeme kararı "
        "bozulmuştur.\n\n"
        "**Emsal niteliği**: Kira borcu bulunsa dahi kiraya verenin yargı kararı "
        "olmaksızın kendiliğinden tahliye yapamayacağı, aksi hâlde haksız fiil "
        "sorumluluğu doğacağı yönünde yerleşik içtihattır.",
    ),
    (
        "Şu kararı özetle:\n\nYargıtay 11. Hukuk Dairesi, E. 2021/XXXX, K. 2022/YYYY. "
        "Davacı şirket, distribütörlük sözleşmesinin davalı üretici tarafından haklı "
        "bir sebep olmaksızın ve makul bir süre verilmeden feshedildiğini ileri sürerek "
        "tazminat talep etmiştir. Yerel mahkeme, sözleşmede 'taraflardan biri her zaman "
        "feshedebilir' hükmü bulunduğu gerekçesiyle davayı reddetmiş; Yargıtay, sürekli "
        "sözleşmelerde fesih hakkının dürüstlük kuralıyla sınırlı olduğunu belirterek "
        "kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 11. Hukuk Dairesi\n"
        "**Esas / Karar**: 2021/XXXX — 2022/YYYY\n\n"
        "**Uyuşmazlık konusu**: Sözleşmede tanınan serbest fesih hakkının, sürekli "
        "borç ilişkilerinde sınırsız ve her zaman kullanılıp kullanılamayacağı.\n\n"
        "**Yerel mahkeme kararı**: Sözleşmedeki serbest fesih hükmüne dayanarak "
        "feshi geçerli kabul etmiş ve tazminat talebini reddetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- Distribütörlük gibi **sürekli borç ilişkilerinde**, sözleşmede tanınan "
        "serbest fesih hakkı dahi **dürüstlük kuralı** (TMK m.2) ve **makul süre "
        "verme yükümlülüğü** ile sınırlıdır.\n"
        "- Uzun süredir devam eden bir ticari ilişkinin ani ve hazırlıksız şekilde "
        "sona erdirilmesi, karşı tarafı **ciddi yatırım ve organizasyon zararına** "
        "uğratabilir; bu durumda fesih hakkının kullanılma şekli **hakkın kötüye "
        "kullanılması** (TMK m.2/2) teşkil edebilir.\n"
        "- Mahkemenin, sözleşmedeki fesih serbestisi hükmünü tek başına yeterli "
        "görmesi ve somut olaydaki makul süre ile dürüstlük unsurlarını "
        "tartışmaması eksik incelemedir.\n\n"
        "**Sonuç**: Bozma — Fesih hakkının dürüstlük kuralı ve makul süre "
        "yükümlülüğü çerçevesinde değerlendirilmemesi nedeniyle karar bozulmuştur.\n\n"
        "**Emsal niteliği**: Sürekli borç ilişkilerinde sözleşmesel fesih hakkının "
        "dahi dürüstlük kuralı ve makul süre ilkesiyle sınırlı olduğu, aksi hâlde "
        "tazminat sorumluluğu doğabileceği yönünde emsaldir (TMK m.2).",
    ),
    (
        "Bu kararı özetler misin:\n\nYargıtay 2. Hukuk Dairesi, E. 2020/XXXX, K. 2021/YYYY. "
        "Davacı koca, eşinin sosyal medyada başka bir erkekle samimi mesajlaştığını "
        "tespit ettiğini, bu nedenle boşanmak istediğini ve eşinin kusurlu olduğunu "
        "ileri sürmüştür. Yerel mahkeme, mesajların tek başına aldatma kanıtı "
        "sayılamayacağı gerekçesiyle her iki tarafı da kusursuz kabul etmiş; Yargıtay, "
        "mesaj içeriğinin değerlendirilme biçiminde hataya işaret ederek kararı kısmen "
        "bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 2. Hukuk Dairesi\n"
        "**Esas / Karar**: 2020/XXXX — 2021/YYYY\n\n"
        "**Uyuşmazlık konusu**: Sosyal medya/mesajlaşma kayıtlarının, boşanma "
        "davasında **kusur belirlemesinde** delil olarak nasıl değerlendirileceği.\n\n"
        "**Yerel mahkeme kararı**: Mesaj içeriklerini tek başına yetersiz görerek "
        "tarafları kusursuz kabul etmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- Mesajlaşma kayıtları, doğrudan fiziksel bir sadakatsizliği ispat etmese "
        "bile, içeriğine göre **evlilik birliğine duyulması gereken saygı ve "
        "sadakat yükümlülüğüne aykırılığı** (TMK m.185) gösterebilir.\n"
        "- Mahkemenin, mesajların **niteliğini, sıklığını ve samimiyet derecesini** "
        "tek tek değerlendirmeden topluca \"yetersiz delil\" olarak nitelendirmesi "
        "eksik incelemedir.\n"
        "- Kusur belirlemesi, boşanmanın sonuçları (nafaka, tazminat) bakımından "
        "doğrudan etkili olduğundan, bu tür delillerin **ayrıntılı ve gerekçeli** "
        "biçimde tartışılması gerekir.\n\n"
        "**Sonuç**: Kısmi bozma — Mesajlaşma kayıtlarının kusur değerlendirmesinde "
        "yetersiz incelendiği gerekçesiyle karar bozulmuştur.\n\n"
        "**Emsal niteliği**: Boşanma davalarında dijital iletişim kayıtlarının, "
        "sadakat yükümlülüğüne aykırılığın değerlendirilmesinde **somut içerik ve "
        "bağlamına göre** delil olarak dikkate alınması gerektiği yönünde emsaldir.",
    ),
    (
        "Şu kararı özetle:\n\nYargıtay 3. Hukuk Dairesi, E. 2021/XXXX, K. 2022/YYYY. "
        "Davacı, apartman yöneticisi olarak görev yaparken kendisine ödenmesi gereken "
        "yönetim ücretinin ödenmediğini ileri sürerek alacak davası açmıştır. Yerel "
        "mahkeme, yönetici ile kat malikleri kurulu arasında yazılı bir ücret sözleşmesi "
        "bulunmadığı gerekçesiyle davayı reddetmiştir. Yargıtay, kat malikleri kurulu "
        "kararıyla belirlenen ücretin yazılı sözleşme şartı aranmaksızın talep "
        "edilebileceğini belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 3. Hukuk Dairesi\n"
        "**Esas / Karar**: 2021/XXXX — 2022/YYYY\n\n"
        "**Uyuşmazlık konusu**: Apartman yöneticisinin ücret alacağının, yazılı bir "
        "sözleşme bulunmaması hâlinde talep edilip edilemeyeceği.\n\n"
        "**Yerel mahkeme kararı**: Yazılı ücret sözleşmesi bulunmadığı gerekçesiyle "
        "alacak talebini reddetmiştir.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- Kat Mülkiyeti Kanunu (634 sayılı) m.34-40 uyarınca yöneticinin ücreti, kat "
        "malikleri kurulunca **karar altına alınması** ile belirlenir; ayrıca yazılı "
        "bir sözleşme şartı aranmaz.\n"
        "- Yönetim ücretine ilişkin kurul kararının varlığı ve yöneticinin fiilen görev "
        "yaptığının ispatı yeterli olup, vekâlet hükümlerine kıyasen (TBK m.502 vd.) "
        "ücret talebi haklı görülmelidir.\n"
        "- Yerel mahkemenin salt \"yazılı sözleşme yok\" gerekçesiyle davayı reddetmesi "
        "eksik incelemeye dayanmaktadır.\n\n"
        "**Sonuç**: Bozma — Yazılı sözleşme aranmaksızın kurul kararına dayalı ücret "
        "talebinin değerlendirilmesi gerektiği gerekçesiyle karar bozulmuştur.\n\n"
        "**Emsal niteliği**: Apartman yöneticisinin ücret alacağında, kat malikleri "
        "kurulu kararının yazılı sözleşme yerine geçebileceği ve vekâlet hükümlerinin "
        "kıyasen uygulanabileceği yönünde emsal teşkil eder.",
    ),
    (
        "Bu kararı özetler misin?\n\nYargıtay 11. Hukuk Dairesi, E. 2022/XXXX, K. 2023/YYYY. "
        "Bir tüketici, internetten satın aldığı elektronik cihazın kargoda hasar "
        "görmesi nedeniyle satıcıdan bedel iadesi talep etmiş; satıcı, hasarın kargo "
        "şirketinin sorumluluğunda olduğunu, kendisinin sorumlu tutulamayacağını ileri "
        "sürmüştür. Yerel mahkeme satıcıyı sorumlu tutmamıştır. Yargıtay, mesafeli "
        "satışlarda malın tüketiciye **hasarsız teslim** edilmesinden satıcının sorumlu "
        "olduğunu belirterek kararı bozmuştur.",
        "**Karar Özeti**\n\n"
        "**Mahkeme**: Yargıtay 11. Hukuk Dairesi\n"
        "**Esas / Karar**: 2022/XXXX — 2023/YYYY\n\n"
        "**Uyuşmazlık konusu**: Mesafeli satışta kargo sırasında oluşan hasardan "
        "satıcının mı yoksa kargo şirketinin mi sorumlu olduğu.\n\n"
        "**Yerel mahkeme kararı**: Hasarın kargo şirketinden kaynaklandığını kabul "
        "ederek satıcıyı sorumlu tutmamıştır.\n\n"
        "**Yargıtay değerlendirmesi**:\n"
        "- Mesafeli Sözleşmeler Yönetmeliği ve 6502 sayılı Tüketicinin Korunması "
        "Hakkında Kanun çerçevesinde, satıcı malı **tüketiciye hasarsız ulaştırmakla** "
        "yükümlüdür; taşıma sürecinde oluşan hasar satıcı ile tüketici arasındaki "
        "ilişkide satıcının **ayıplı ifa** sorumluluğunu doğurur (6502 sayılı Kanun "
        "m.8, m.11).\n"
        "- Satıcının kargo şirketine karşı **rücu hakkı** saklı olmakla birlikte, "
        "tüketiciye karşı doğrudan sorumluluğu bundan etkilenmez.\n\n"
        "**Sonuç**: Bozma — Hasarlı teslimattan satıcının sorumlu olduğu ve tüketicinin "
        "seçimlik haklarını satıcıya karşı kullanabileceği gerekçesiyle karar "
        "bozulmuştur.\n\n"
        "**Emsal niteliği**: Mesafeli satışlarda taşıma sırasında oluşan hasarlardan "
        "satıcının tüketiciye karşı doğrudan sorumlu olduğu, kargo şirketine rücu "
        "hakkının bu sorumluluğu ortadan kaldırmadığı yönünde emsal teşkil eder.",
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
