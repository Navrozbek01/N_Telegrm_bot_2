import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    text = (
        "Salom Botimga xush kelibsiz! Siz bu yerda mana shu hayvonlar haqida bilishingiz mumkin!\n\n"
        "/Sher\n"
        "/Yolbars\n"
        "/Fil\n"
        "/Tulki\n"
        "/Bori\n"
        "/Ayiq\n"
        "/Maymun\n"
        "/Kiyik\n"
        "/Arslon\n"
        "/Qoplon\n"
        "/Gepard\n"
        "/Kanguru\n"
        "/Zebr\n"
        "/Jirafa\n"
        "/Gippopotam\n"
        "/Nashshar\n"
        "/Suv_ayigi\n"
        "/Antilopa\n"
        "/Chumoli\n"
        "/Ari\n"
        "/Qaldirgoch\n"
        "/Qarga\n"
        "/Toyqush_Tovus\n"
        "/Tovuq\n"
        "/Goz\n"
        "/Ordak\n"
        "/Qoramol\n"
        "/Sigir\n"
        "/Ot\n"
        "/Eshak\n"
        "/Echki\n"
        "/Qoy\n"
        "/It\n"
        "/Mushuk\n"
        "/Burgut\n"
        "/Qunduz\n"
        "/Tulpor\n"
        "/Qirgiy\n"
        "/Boriqush\n"
        "/Kaklik\n"
        "/Jayra\n"
        "/Ilon\n"
        "/Tasma_ilon\n"
        "/Timsoh\n"
        "/Chayon\n"
        "/Qurbaqa\n"
        "/Baliq\n"
        "/Akula\n"
        "/Delfin\n"
        "/Kit\n"
        "/Pingvin\n"
        "/Ayroqi_baliq\n"
        "/Krab\n"
        "/Omba\n"
        "/Dengiz_yulduzi\n"
        "/Meduza\n"
        "/Karakal\n"
        "/Sirtlon\n"
        "/Kamelopard_jirafa\n"
        "/Lama\n"
        "/Alpaka\n"
        "/Yalpiz_qush\n"
        "/Kolibri\n"
        "/Papagoy\n"
        "/Tukan\n"
        "/Boyogli\n"
        "/Qunduz\n"
        "/Yirtqich_qush\n"
        "/Qizil_bori\n"
        "/Koala\n"
        "/Panda\n"
        "/Lemur\n"
        "/Orangutan\n"
        "/Shimpanze\n"
        "/Babun\n"
        "/Nosorog\n"
        "/Tovushqon\n"
        "/Kirpi\n"
        "/Kalamush\n"
        "/Sichqon\n"
        "/Tarakan\n"
        "/Orgimchak\n"
        "/Chivin\n"
        "/Qaldirgoch\n"
        "/Laylak\n"
        "/Turna\n"
        "/Qaz\n"
        "/Kaptar\n"
        "/Sichqoncha\n"
        "/Korshapalak\n"
        "/Tilla_baliqcha\n"
        "/Yilqiboqar\n"
        "/Qoramol_bugu\n"
        "/Giyohxor_qush\n"
        "/Qor_bars\n"
        "/Chakalak_qush\n"
        "/Dov_dov_qush\n"
        "/Burama_shoxli_kiyik\n"
        "/Qizil_tulki\n"
        "/Dovon_mushugi\n"
        "/Yilqiboqar"  
    )
    await message.answer(text)


@dp.message(Command('Sher'))
async def handle_message(message: Message):
    await message.answer("Sher — yirik yirtqich sutemizuvchi hayvon bo‘lib, Felidae oilasiga mansub. U Afrika va Hindistonning ba’zi hududlarida yashaydi. Erkak sherlarning tana uzunligi 2,5–3 metr, vazni 190–250 kg atrofida bo‘ladi, ayollari esa kichikroq va yengilroq. Erkak sherlarning bosh atrofida jingalak va quyuq rangdagi manalar bor, bu uning kuchi va yoshi belgisi hisoblanadi. Sherlar odatda parda — guruh bo‘lib yashaydi, u yerda bir nechta urg‘ochi va bitta yoki bir nechta erkak sher bo‘ladi. Ovlanish va hududni himoya qilish guruh bilan amalga oshiriladi. Sherning qichqirig‘i uzoq masofalarga eshitiladi va bu hududni belgilash uchun ishlatiladi. Sher tabiiy muvozanatni saqlashda muhim rol o‘ynaydi, ammo odam faoliyati tufayli uning soni kamaymoqda.")

@dp.message(Command('Yolbars'))
async def handle_message(message: Message):
    await message.answer("Yo‘lbars — eng yirik mushuksimon yirtqich hayvon bo‘lib, u Panthera tigris nomi bilan tanilgan. Asosan Osiyoda — Hindiston, Xitoy, Rossiya, Indoneziya kabi hududlarda yashaydi. Tanasining uzunligi 2,5–3,3 metr, vazni 100–300 kg gacha yetadi. Uning tanasi silliq, kuchli va to‘q sariq rangda bo‘lib, qora chiziqlar bilan qoplangan. Yo‘lbars yolg‘iz ovlanadi va juda sokin, yashirincha harakat qiladi. Ovlanishda kuchi, chaqqonligi va sabr-toqati bilan ajralib turadi. Asosan kiyik, cho‘chqa, maymun kabi hayvonlarni ovlaydi. Yo‘lbars ham yo‘qolib borayotgan turlar ro‘yxatiga kiritilgan va himoya ostida turadi.")

@dp.message(Command('Fil'))
async def handle_message(message: Message):
    await message.answer("Fil — dunyodagi eng yirik quruqlikdagi sutemizuvchi hayvon. U Afrika fili va Osiyo fili turlariga bo‘linadi. Tanasining uzunligi 6–7 metr, balandligi 3–4 metr, og‘irligi 5–7 tonnaga yetishi mumkin. Uzun xartumi — asosiy belgisi bo‘lib, u bilan ovqat oladi, suv ichadi va hid sezadi. Uzun va qalin quloqlari orqali issiqlikni chiqaradi. Fil o‘simlikxo‘r bo‘lib, asosan daraxt barglari, po‘stlog‘i va mevalar bilan oziqlanadi. Ular kuchli, ammo tinch hayvonlardir. Fil uzoq yashaydi — o‘rtacha 60–70 yil. Afsuski, so‘ydozlik va yashash joyi kamayishi sababli fil ham himoya ostida turadi.")

@dp.message(Command('Tulki'))
async def handle_message(message: Message):
    await message.answer("Tulki — o‘rtacha kattalikdagi yirtqich hayvon bo‘lib, mushuksimonlar emas, itlar oilasiga (Canidae) kiradi. Eng keng tarqalgan turi — qizil tulki. U Osiyo, Yevropa, Shimoliy Afrika va Amerikada uchraydi. Tanasining uzunligi 60–90 sm, dumining uzunligi 30–50 sm, vazni 5–10 kg bo‘ladi. Tulki chaqqon, ayyor va yolg‘iz yashovchi hayvon. Asosan qush, sichqon, hasharot va ba'zida mevalar bilan oziqlanadi. Juda ehtiyotkor va yaxshi eshitadi. Ular tunda faol bo‘ladi. Tulki ko‘plab ertak va hikoyalarda aql va hiyla ramzi sifatida tilga olinadi.")

@dp.message(Command('Bori'))
async def handle_message(message: Message):
    await message.answer("Bo‘ri — yirtqich hayvon bo‘lib, itlar oilasiga mansub va Canis lupus nomi bilan tanilgan. U Yevrosiyo va Shimoliy Amerikada keng tarqalgan. Bo‘rining tanasi 1–1.5 metr, vazni 30–60 kg atrofida bo‘ladi. Uning rangi odatda kulrang, ba’zida oq yoki qora tusda bo‘ladi. Bo‘rilar to‘dada yashaydi va ov qiladi. Asosan kiyik, quyon, qo‘y, sichqon kabi hayvonlar bilan oziqlanadi. Juda aqlli, kuchli va jips guruh bo‘lib harakat qiladi. Bo‘ri tabiatda muhim rol o‘ynaydi — kasal va zaif hayvonlarni yo‘q qilib ekotizimni muvozanatda ushlab turadi.")

@dp.message(Command('Ayiq'))
async def handle_message(message: Message):
    await message.answer("Ayiq — yirik yirtqich sutemizuvchi hayvon bo‘lib, ayiqlar oilasiga (Ursidae) mansub. Ular Yevropa, Osiyo va Shimoliy Amerikada yashaydi. Eng mashhur turlari: qo‘ng‘ir ayiq, oq ayiq (qutb ayiği) va qora ayiq. Tanasining uzunligi 1,5–3 metr, vazni esa 100–700 kg gacha bo‘ladi. Ayiqning panjalari kuchli, tirnoqlari uzun, hid bilish qobiliyati juda kuchli. U o‘simliklar, mevalar, baliq, hasharot va mayda hayvonlar bilan oziqlanadi. Qish oylarida uyquga ketadi. Ayiq odatda yolg‘iz yashaydi. Ular ba’zan odam yashaydigan joylarga ham yaqinlashadi.")

@dp.message(Command('Maymun'))
async def handle_message(message: Message):
    await message.answer("Maymun — aqlli va chaqqon sutemizuvchi hayvon bo‘lib, primatlar turkumiga kiradi. Ular tropik o‘rmonlarda, ayniqsa Afrikada, Janubi-Sharqiy Osiyo va Janubiy Amerikada yashaydi. Maymunlarning ko‘pchiligi daraxtlarda yashaydi, ba'zilari yerda yuradi. Tanasining uzunligi va vazni turiga qarab farq qiladi. Qo‘llari uzun, panjalari ushlashga qulay bo‘lib, ba’zilarida dum ham faol ishlatiladi. Ular meva, barg, hasharot va ba'zida mayda hayvonlar bilan oziqlanadi. Maymunlar juda ijtimoiy, bir-biri bilan aloqa qiladi, taqlid va o‘rganish qobiliyatiga ega.")

@dp.message(Command('Kiyik'))
async def handle_message(message: Message):
    await message.answer("Kiyik — o‘rta kattalikdagi o‘simlikxo‘r hayvon bo‘lib, shoxli hayvonlar (bo‘riso‘xtali) oilasiga kiradi. U dasht, cho‘l va o‘rmonlarda yashaydi. Kiyiklar yengil, chaqqon va juda tez yuguradi — soatiga 60–80 km tezlikda harakatlana oladi. Tanasining uzunligi 1–1.5 metr, vazni 30–50 kg bo‘ladi. Erkak kiyiklarda egri shoxlar bo‘ladi. Asosan o‘t, barg va mevalar bilan oziqlanadi. Kiyiklar to‘da bo‘lib yuradi va yirtqichlardan qochishda juda chaqqonlik ko‘rsatadi. Ular ko‘plab hududlarda tabiatni muhofaza qilish qonunlari bilan himoyalangan.")

@dp.message(Command('Arslon'))
async def handle_message(message: Message):
    await message.answer("Arslon — yirik yirtqich hayvon bo‘lib, mushuksimonlar oilasiga, xususan Panthera leo turiga mansub. U Afrikaning savannalarida va Hindistonning ba’zi hududlarida yashaydi. Erkak arslonning tanasi uzun, vazni 180–250 kg gacha bo‘ladi, boshi atrofida qalin qora yoki sarg‘ish yollari (manalari) bo‘ladi. Urg‘ochilari yengilroq va yollarsiz bo‘ladi. Arslonlar guruh bo‘lib — pardada yashaydi. Asosan zebra, kiyik, buffalo kabi hayvonlarni ovlaydi. Arslon jasorat, kuch va hokimiyat timsoli sifatida ko‘plab madaniyatlarda qadrlanadi.")

@dp.message(Command('Qoplon'))
async def handle_message(message: Message):
    await message.answer("Qoplon — yirtqich mushuksimon hayvon bo‘lib, ilmiy nomi Panthera pardus. U Afrikada, Osiyo o‘rmonlari va tog‘larida yashaydi. Tanasining uzunligi 1–1,8 metr, vazni 30–90 kg bo‘ladi. Qoplonning terisi sarg‘ish tusda bo‘lib, ustida qora xalqa shaklidagi dog‘lar mavjud. U juda chaqqon, kuchli va daraxtga yaxshi tirmashadi. Ovni yolg‘iz qiladi — asosan kiyik, quyon, qush va mayda hayvonlar bilan oziqlanadi. Tungi hayot tarziga ega. Qoplon sezgir va yashirin harakat qiladi. Ko‘plab hududlarda u yo‘qolib ketish xavfi ostida turadi va himoya qilinadi.")

@dp.message(Command('Gepard'))
async def handle_message(message: Message):
    await message.answer("Gepard — dunyodagi eng tez yuguradigan yirtqich hayvon bo‘lib, mushuksimonlar oilasiga mansub. Ilmiy nomi — Acinonyx jubatus. U asosan Afrika savannalarida yashaydi. Tanasining uzunligi 1,1–1,5 metr, vazni 40–65 kg bo‘ladi. Gepardning tanasi oriq, oyoqlari uzun va muskulli, terisi sarg‘ish va mayda qora nuqtalar bilan qoplangan. U qisqa masofada soatiga 100–120 km tezlikda yugura oladi. Asosan gazel, impala va kichik tuyoqlilarni ovlaydi. Gepard yolg‘iz yashaydi, juda ehtiyotkor va tinch hayvondir. Ayrim hududlarda u yo‘qolib borayotgan tur hisoblanadi.")

@dp.message(Command('Kanguru'))
async def handle_message(message: Message):
    await message.answer("Kanguru — Avstraliyaga xos, katta sutemizuvchi hayvon bo‘lib, marsupialar oilasiga kiradi. U o‘ziga xos orqa oyoqlari kuchli va uzun, old oyoqlari kichikroq. Tananing uzunligi 1–1,5 metr atrofida, vazni esa 30–90 kg bo‘ladi. Kangurular katta va kuchli dumga ega bo‘lib, bu unga muvozanatni saqlashda yordam beradi. Ular asosan o‘tlar, barglar va urug‘lar bilan oziqlanadi. Eng qiziq tomoni — ular orqa oyoqlari yordamida katta sakrashlar bilan tez harakatlana oladi. Kangurular o‘zining o‘ziga xos chaqaloqni (jo‘ja) onaning qornida maxsus sumkada olib yuradi. Ular ijtimoiy guruhda yashaydi va asosan tong yoki kechqurun faol bo‘ladi.")

@dp.message(Command('Zebr'))
async def handle_message(message: Message):
    await message.answer("Zebr — o‘txo‘r, yirik sutemizuvchi hayvon bo‘lib, otlar oilasiga kiradi. U asosan Afrikaning cho‘llari va ochiq yaylovlarida yashaydi. Zebrlarning tanasi o‘rtacha uzunligi 2–2,5 metr, bo‘yi 1,2–1,5 metr va vazni 200–400 kg atrofida bo‘ladi. Eng mashhur xususiyati — tanasidagi qora va oq chiziqlar (zebra chizmalari), ular har bir hayvonda noyob va takrorlanmasdir. Bu chiziqlar ularni yirtqichlardan himoya qiladi va issiqlikni boshqarishda yordam beradi. Zebralar to‘da bo‘lib yashaydi, o‘t va barg bilan oziqlanadi. Juda tez yuguradi va xavf paytida katta masofani qamrab olishga qodir. Zebralar ijtimoiy va bir-biriga bog‘liq hayvonlardir.")

@dp.message(Command('Jirafa'))
async def handle_message(message: Message):
    await message.answer("Jirafa — dunyodagi eng baland sutemizuvchi hayvon bo‘lib, jirafalar oilasiga kiradi. U Afrikaning quruq va yarim o‘rmonli hududlarida yashaydi. Jirafaning bo‘yi 4,5 dan 6 metrga yetadi, vazni esa 800 dan 1,200 kilogrammgacha bo‘ladi. Uzoq bo‘yni yordamida baland daraxtlarning barglarini osonlik bilan yeya oladi, ayniqsa akatsiya daraxti uning sevimli o‘simligi hisoblanadi. Jirafa tanasida tanani qoplagan g‘aroyib to‘q dog‘lar bor, bu har bir jirafada noyob naqshdir. Jirafalar asosan tong va kechqurun faol bo‘lib, tez yugura oladi. Ular ijtimoiy hayvonlar bo‘lib, kichik guruhlarda yashaydi.")

@dp.message(Command('Gippopotam'))
async def handle_message(message: Message):
    await message.answer("Gippopotam (yoki suv toshqopi) — katta o‘lchamli yarim suvda yashovchi sutemizuvchi hayvon bo‘lib, gippopotamlar oilasiga kiradi. U asosan Afrika daryolari va ko‘llarida uchraydi. Gippopotamning tanasi og‘ir va qalin teri bilan qoplangan, uzunligi 3,3—5 metr, vazni esa 1,500—3,200 kg ga yetadi. Ular suvda ko‘p vaqt o‘tkazib, tana haroratini pasaytiradi va terisini quyoshdan himoya qiladi. Gippopotamlar asosan kechasi o‘tlar bilan oziqlanadi va suvda ko‘p dam oladi. Gippopotam juda kuchli va agressiv hayvon bo‘lib, o‘z hududini himoya qilishda juda qat’iyatli bo‘ladi. Ularning katta jag‘lari va kuchli tishlari bor, bu ularni yirtqichlardan himoya qiladi.")

@dp.message(Command('Nashshar'))
async def handle_message(message: Message):
    await message.answer("Nashshar — yirik va kuchli yirtqich qush bo‘lib, burgutlar oilasiga kiradi. U ko‘pincha O‘rta Osiyo, Rossiya, Hindiston va Markaziy Osiyoda uchraydi. Nashsharning qanotlari keng va uzun bo‘lib, ularni uchish uchun juda qulay qiladi. U uzun masofalarga uchib, mayda va o‘rtacha o‘lchamdagi hayvonlarni ovlaydi — asosan kemiruvchilar, mayda sutemizuvchilar va boshqa qushlar bilan oziqlanadi. Nashshar o‘zining kuchli tumshug‘i va panjalari bilan ovini ushlab oladi. Bu qush ko‘pincha baland joylarda, qoyalarda yoki o‘rmon chetida o‘z uyasini quradi. Nashshar uzoq umr ko‘radi va tabiiy muhitda muhim yirtqich hisoblanadi.")

@dp.message(Command('Suv_ayigi'))
async def handle_message(message: Message):
    await message.answer("Suv ayiği — yarim suv hayvoni bo‘lib, ayiqlar oilasiga kiradi. U asosan Shimoliy Amerika va Osiyoning ba’zi hududlarida, ko‘llar va daryolar atrofida yashaydi. Suv ayiğining tana uzunligi 1,2—1,5 metrga yetadi, vazni esa 60—120 kg atrofida bo‘ladi. U juda yaxshi suzuvchi bo‘lib, suv ostida uzoq vaqt qolishi mumkin. Suv ayiği asosan baliq, suvda yashovchi hasharotlar, va o‘simliklar bilan oziqlanadi. Teri qalin va suvga chidamli, bu unga sovuq suvda qulay yashash imkonini beradi. Suv ayiği tunda faolroq bo‘lib, ko‘pincha ov qilish uchun suvga tushadi.")

@dp.message(Command('Antilopa'))
async def handle_message(message: Message):
    await message.answer("Antilopa — o‘rmon va ochiq maydonlarda yashovchi, tez yugurishga mo‘ljallangan sutemizuvchi hayvon. U antilopalar oilasiga kiradi va dunyoning turli qismlarida, asosan Afrika va Osiyoda tarqalgan. Antilopalar o‘rtacha hajmda bo‘lib, vaznlari 30 dan 300 kg gacha o‘zgaradi. Ularning uzun oyoqlari va yengil tanasi yuqori tezlikda yugurishga yordam beradi, bu esa yirtqichlardan qochish uchun zarurdir. Antilopalarning boshida ko‘pincha burmalar yoki to‘g‘ri cho‘zilgan shoxlar bo‘ladi, bu shaxsga qarab farq qiladi. Ular asosan o‘t va barglar bilan oziqlanadi. Antilopalar ijtimoiy hayvon bo‘lib, kichik yoki katta guruhlarda yashaydi.")

@dp.message(Command('Chumoli'))
async def handle_message(message: Message):
    await message.answer("Chumoli — kichik, ijtimoiy hayvon bo‘lib, hasharotlar sinfiga kiradi. U dunyoning deyarli barcha hududlarida yashaydi va minglab turdagi chumolilar mavjud. Chumolilar kichik o‘lchamiga qaramay, juda kuchli va tashkilotchilardir. Ular guruh bo‘lib yashaydi, murakkab koloniyalar hosil qiladi va aniq vazifalar bo‘yicha bo‘linib ishlaydi: ishchi chumolilar ovqat to‘playdi, askarlar esa koloniyani himoya qiladi. Chumolilar er ostida yoki daraxtlarda maxfiy tarmoqlar quradi. Ular o‘z vazifalarini ifodalovchi kimyoviy izlar — feromonlar yordamida bir-biriga signal beradi. Chumolilar tabiiy muhitda o‘simlik urug‘larini tarqatishda va tuproq havalandirishda muhim rol o‘ynaydi.")

@dp.message(Command('Ari'))
async def handle_message(message: Message):
    await message.answer("Ari — asosan asal ishlab chiqaruvchi hasharot bo‘lib, asalarilar oilasiga mansub. Ularning tanasi kichik, qopqog‘i qalin tuklar bilan qoplangan bo‘lib, qanotlari tez-tez tebranadi. Arilar o‘zaro juda tashkilotchilardir va murakkab ijtimoiy tuzilishga ega bo‘lgan koloniyalarda yashaydi. Ular gulchang (polen) va nektarni to‘playdi, bu orqali asal ishlab chiqariladi. Asal nafaqat ozuqa sifatida ishlatiladi, balki tabiiy antibiotik xususiyatlarga ham ega. Arilar tabiatda o‘simliklarning changlanishida muhim rol o‘ynaydi, shuning uchun ular ekotizimning asosiy o‘yinchilaridan biridir. Ari koloniyasida bosh ari (malika), ishchi arilar va erkak arilar mavjud.")

@dp.message(Command('Qaldirgoch'))
async def handle_message(message: Message):
    await message.answer("Qaldirg‘och — kichik, tez uchuvchi qush bo‘lib, asosan yoz va bahor mavsumlarida uchraydi. Ular qaldirg‘oqlar oilasiga kiradi va dunyoning ko‘plab hududlarida, jumladan O‘zbekiston va Markaziy Osiyoda keng tarqalgan. Qaldirg‘oqlar uzun va tor qanotlari bilan juda tez va mahorat bilan ucha oladi, shuningdek, ular havo orqali hasharotlarni tutib ovqatlanadi. Ularning tana uzunligi taxminan 15 sm atrofida, vazni esa 20-30 grammga teng. Qaldirg‘oqlar ko‘pincha odam yashaydigan joylarga yaqin joylarda, ayniqsa qishloqlarda, daraxtlar yoki bino tomlarida g‘oza quradi. Ular ko‘chuvchi qush bo‘lib, qish oylarida issiqroq hududlarga ko‘chib ketadi.")

@dp.message(Command('Qarga'))
async def handle_message(message: Message):
    await message.answer("Qarg‘a — o‘rmonlar, shaharlarda va ochiq maydonlarda keng tarqalgan, aqlli va moslashuvchan qush. Ularning oilasi korvidlar oilasiga kiradi. Qarg‘alar qora rangli patlarga ega bo‘lib, o‘lchamlari o‘rtacha bo‘lib, uzunligi taxminan 40-50 sm atrofida. Ular zo‘ravon emas, lekin juda mulohazakor va muammolarni hal qilishda ajoyib qobiliyatga ega. Qarg‘alar turli ovozlarni eslab qolishi, vositalardan foydalanishi va murakkab ijtimoiy tuzilmada yashashi bilan mashhur. Ular omnivor — ya’ni, o‘simlik va hayvonlardan oziqlanadi, chiqindilarni tozalashda ham muhim rol o‘ynaydi. Qarg‘alar odatda o‘ziga xos «til»ga ega bo‘lib, o‘zaro turli signal va chaqiriqlar orqali muloqot qiladi.")

@dp.message(Command('Toyqush_Tovus'))
async def handle_message(message: Message):
    await message.answer("Toyqush (Tovus) — go‘zal va nufuzli qush bo‘lib, asosan Janubiy Osiyo va Hindiston mintaqasida yashaydi. U fazoviy qushlar oilasiga mansub bo‘lib, o‘zining uzun va rang-barang dum patlari bilan mashhur. Erkak toyqushlar o‘zining yorqin ko‘k, yashil va oltin rangdagi patlarini yoyib, go‘zal abanalar yaratadi, bu holat ko‘payish davrida ayollarni jalb qilish uchun ishlatiladi. Toyqushning dumidagi kozcha deb ataladigan patlar ko‘plab ranglarda porlaydi. Ayol toyqush esa odatda kichikroq va kam rang-barang bo‘ladi. Toyqushlar asosan o‘simliklar, urug‘lar va kichik hasharotlar bilan oziqlanadi. Ular o‘zining ko‘zni qamashtiruvchi ko‘rinishi bilan madaniyat va san’atda ko‘p marotaba ramz sifatida ishlatilgan")

@dp.message(Command('Tovuq'))
async def handle_message(message: Message):
    await message.answer("Tovuq — inson tomonidan ming yillardan beri boqiladigan eng keng tarqalgan uy hayvonlaridan biri. U qushlar oilasiga mansub bo‘lib, dastlab yovvoyi tovuqdan (Gallus gallus) kelib chiqqan. Tovuqning tana uzunligi odatda 30-40 sm atrofida, vazni esa 1,5-4 kg gacha bo‘ladi. Erkak tovug‘lar — xo‘rozlar, urg‘ochilari esa tovuqlar deb ataladi. Tovuq dehqonchilikda tuxum va go‘sht manbai sifatida juda muhim hisoblanadi. Ular asosan don va o‘simlik qoldiqlari bilan oziqlanadi. Tovuqning xulq-atvori juda oson, u insonlarga yaqin bo‘lib, tez moslashadi. Shuningdek, tovuqning «kokilish» ovozi ko‘p madaniyatlarda vaqtni bildirish uchun ishlatiladi.")

@dp.message(Command('Goz'))
async def handle_message(message: Message):
    await message.answer("G‘oz — uy hayvoni bo‘lib, ko‘plab xalqlarda go‘sht, tuxum va jun manbai sifatida boqiladi. U ko‘klar oilasiga mansub bo‘lib, yovvoyi ajdodlari Shimoliy Yevroosiyo va Shimoliy Amerikada yashagan. G‘ozlar o‘rtacha vazni 3—7 kilogramm bo‘lib, ularning rangi oq, kulrang, jigarrang yoki qora bo‘lishi mumkin. Bu qushlar suvda va quruqlikda yashashga moslashgan, suzish qobiliyati yuqori. G‘ozlar ijtimoiy hayvon bo‘lib, kichik guruhlarda yashaydi va ovoz chiqarib bir-birlari bilan muloqot qiladi. Ular asosan o‘tlar, urug‘lar va kichik suv o‘simliklari bilan oziqlanadi. G‘ozning shovqinli ovozi uni yaxshi himoya qiladi — ko‘pincha uylarni va maysazorlarni yovvoyi hayvonlardan himoya qilish uchun ishlatiladi.")

@dp.message(Command('Ordak'))
async def handle_message(message: Message):
    await message.answer("O‘rdak — suv qushlari oilasiga mansub bo‘lib, dunyo bo‘ylab keng tarqalgan. Ular ko‘pincha daryo, ko‘l va boshqa suv havzalarida yashaydi. O‘rdaklar o‘rtacha 50-70 sm uzunlikda bo‘lib, vazni 1—3 kilogrammga yetadi. Erkak va urg‘ochi o‘rdaklar orasida rang-barang farqlar mavjud: erkaklarning patlari ko‘proq yorqin va ko‘zga tashlanadigan bo‘lsa, urg‘ochilarining rangi ko‘proq soyali va kamrang bo‘ladi. O‘rdaklar asosan o‘tlar, urug‘lar, kichik suv hayvonlari va hasharotlar bilan oziqlanadi. Ular suvda yaxshi suzadi va uzoq masofalarga ko‘chib o‘tadi. O‘rdaklar insonlar tomonidan tuxum va go‘shti uchun keng boqiladi. Shuningdek, ularning shovqinli ovozlari bilan ko‘plab madaniyatlarda tanilgan.")

@dp.message(Command('Qoramol'))
async def handle_message(message: Message):
    await message.answer("Qoramol — bu chorvachilikda keng tarqalgan, go‘sht, sut va teri manbai hisoblangan katta sutemizuvchi hayvon. U sigirlar oilasiga mansub bo‘lib, butun dunyo bo‘ylab ko‘plab nasl turlari mavjud. Qoramolning o‘rtacha vazni 500 dan 900 kilogrammgacha bo‘lib, ayrim yirik nasllar 1000 kilogrammdan ham og‘ir bo‘lishi mumkin. Ularning rangi oq, qora, jigarrang yoki rang-barang bo‘lishi mumkin. Qoramollar asosan o‘tlar, urug‘lar va boshqa o‘simliklar bilan oziqlanadi. Bu hayvonlar ijtimoiy bo‘lib, guruhlarda yashaydi. Ular insonlarga sut va go‘sht yetkazib berishda muhim rol o‘ynaydi. Bundan tashqari, qoramol terisi va yog‘i ham sanoatda keng qo‘llaniladi.")

@dp.message(Command('Sigir'))
async def handle_message(message: Message):
    await message.answer("Sigir — qoramolning eng keng tarqalgan va inson tomonidan eng ko‘p boqiladigan nasl turi hisoblanadi. U sut, go‘sht, teri va boshqa mahsulotlar olish uchun parvarish qilinadi. Sigirlar sutemizuvchilar oilasiga mansub bo‘lib, katta tanasi, kuchli oyoqlari va o‘tlarni yeyishga moslashgan tili bor. Ularning o‘rtacha vazni 450—700 kilogrammga yetadi, ayrim yirik nasllar esa 1000 kilogrammdan oshishi mumkin. Sigirlarning rangi juda xilma-xil bo‘lib, oq, qora, jigarrang va rang-barang dog‘lar bilan farqlanadi. Ular ijtimoiy hayvon bo‘lib, odatda guruhlarda yashaydi. Sigirlar asosan o‘tlar, urug‘lar va boshqa o‘simliklar bilan oziqlanadi. Insonlar uchun sigir suti muhim oziq-ovqat manbai hisoblanadi va ko‘plab madaniyatlarda sut mahsulotlari keng iste’mol qilinadi.")

@dp.message(Command('Ot'))
async def handle_message(message: Message):
    await message.answer("Ot — inson tomonidan asrlar davomida boqilib, yurish, yuk tashish, sport va ko‘ngilochar maqsadlarda foydalaniladigan katta, kuchli va chidamli sutemizuvchi hayvon. Otlar Equidae oilasiga mansub bo‘lib, ularning turli nasllari va turlari mavjud. Otlarning o‘rtacha bo‘y uzunligi 1,4—1,8 metr, vazni esa 400—600 kilogramm atrofida bo‘ladi, lekin ba’zi nasllar bundan ham katta bo‘lishi mumkin. Ularning ko‘zlari katta, quloqlari esa o‘tkir eshitishga moslashgan. Otlar tez yugurish qobiliyatiga ega bo‘lib, uzoq masofalarga chidamlilik bilan yurishi mumkin. Otlarga asosan o‘tlar, butalar va boshqa o‘simliklar oziq bo‘ladi. Insonlar otlarni asosan transport vositasi, sport turlari (masalan, polo, at poygasi) va qishloq xo‘jaligida ishlatishadi.")

@dp.message(Command('Eshak'))
async def handle_message(message: Message):
    await message.answer("Eshak — inson tomonidan uzoq yillardan beri boqiladigan, kuchli va chidamli sudemizuvchi hayvon bo‘lib, asosan yuk tashish va qishloq xo‘jaligida ishlatiladi. U Equidae oilasiga mansub bo‘lib, otga qaraganda kichikroq va qalinroq tana tuzilishiga ega. Eshaklarning vazni odatda 180 dan 400 kilogrammgacha bo‘ladi, bo‘y uzunligi esa 1—1,4 metr atrofida. Ularning quloqlari uzun va eshitish qobiliyati yaxshi rivojlangan. Eshaklar qattiq sharoitlarda, ayniqsa tog‘li va cho‘l hududlarda ishlashga moslashgan. Ular o‘tlar va boshqa o‘simliklarni yeyadi. Eshak insonlarga yuk tashish, qishloq xo‘jaligi ishlarida yordam berish, shuningdek ba’zi madaniyatlarda sut va go‘sht manbai sifatida ham ahamiyatlidir.")

@dp.message(Command('Echki'))
async def handle_message(message: Message):
    await message.answer("Echki — kichik o‘lchamdagi sudemizuvchi hayvon bo‘lib, odatda uy sharoitida parvarish qilinadi. U Bovidae oilasiga mansub va insonlarga sut, go‘sht, jun hamda teri manbai sifatida xizmat qiladi. Echkilarning vazni odatda 20 dan 70 kilogrammgacha, bo‘yi esa 40—70 santimetr atrofida bo‘ladi. Ularning boshida har xil shakldagi, ba’zan jingalak, ba’zan to‘g‘ri qorachalar bo‘ladi. Echki juda moslashuvchan hayvon bo‘lib, tog‘li va qurg‘oqchil hududlarda ham yashay oladi. Ular asosan o‘tlar, barglar, butalar va boshqa o‘simliklar bilan oziqlanadi. Echki ijtimoiy hayvon bo‘lib, ko‘pincha kichik guruhlarda yashaydi.")

@dp.message(Command('Qoy'))
async def handle_message(message: Message):
    await message.answer("Qo‘y — odamlar tomonidan ming yillardan beri boqiladigan sudemizuvchi hayvon bo‘lib, u Bovidae oilasiga mansub. Qo‘ylar asosan jun, go‘sht va sut manbai sifatida juda muhimdir. Ularning vazni turiga qarab 30 dan 140 kilogrammgacha o‘zgaradi, bo‘yi esa 50—100 santimetr atrofida bo‘ladi. Qo‘ylarning boshida turli shakldagi qorachalar bo‘lishi mumkin, ba’zan erkak qo‘ylarda jingalak va katta qorachalar bo‘ladi. Qo‘ylar o‘tlarni, barglarni va boshqa o‘simliklarni yeydi. Ular ijtimoiy hayvonlar bo‘lib, ko‘pincha qo‘mondonlik ostidagi guruhlarda yashaydi. Qo‘ylarning naslchiligi ham odamlar uchun muhim ahamiyatga ega.")

@dp.message(Command('It'))
async def handle_message(message: Message):
    await message.answer("It — insonlarning eng yaqin do‘sti bo‘lgan uy hayvoni, Canidae oilasiga mansub sudemizuvchi hayvon. Itlar minglab yillar davomida odam bilan birga yashab, turli maqsadlarda: qo‘riqlash, ov qilish, sport, terapiya va shunchaki do‘stlik uchun yetishtirilgan. Itlarning turli zotlari bor, ularning vazni va o‘lchami juda farq qiladi — kichik zotlar 1-2 kg bo‘lsa, katta zotlar 70 kg dan oshadi. Itlar juda aqlli, ijtimoiy va o‘rganuvchan hayvonlardir. Ular odamning nutqini va kayfiyatini tushunishga qodir. Itlarning sezgirligi va fidoyiligi ularni inson hayotida juda muhim qiladi.")

@dp.message(Command('Mushuk'))
async def handle_message(message: Message):
    await message.answer("Mushuk — insonlar tomonidan ming yillardan beri uy hayvoni sifatida boqiladigan, Felidae oilasiga mansub mayda yirtqich sudemizuvchi hayvon. Mushuklar o‘zining mustaqilligi, egiluvchanligi va tozaligi bilan mashhur. Ularning o‘rtacha vazni 3—6 kilogramm atrofida bo‘lib, turli zotlarga qarab farq qilishi mumkin. Mushuklar juda yaxshi ovchilar bo‘lib, asosan kichik kemiruvchilar va qushlarni ovlashadi. Ular inson bilan yaxshi munosabatda bo‘lib, ko‘plab oilalarda do‘st va hamrohlik qiluvchi hayvon hisoblanadi. Mushuklarning sezgir quloqlari va ko‘zlari kechasi ham yaxshi ko‘rishiga yordam beradi.")

@dp.message(Command('Burgut'))
async def handle_message(message: Message):
    await message.answer("Burgut — yirik va kuchli yirtqich qush bo‘lib, Accipitridae oilasiga mansub. U O‘rta Osiyo, Yevropa va Shimoliy Amerikada keng tarqalgan. Burgut qanotlarining ochilishi 2,2 metrgacha yetishi mumkin, vazni esa 4—7 kilogramm atrofida bo‘ladi. Bu qush juda yaxshi ko‘rish qobiliyatiga ega bo‘lib, uzoq masofadan ham kichik hayvonlarni aniqlay oladi. U asosan o‘rdak, quyon, baliq va boshqa kichik hayvonlar bilan oziqlanadi. Burgut kuchli qanotlari bilan uzoq masofaga uchib, yuqori balandliklarda parvoz qiladi. U sharaf va kuch ramzi sifatida ko‘plab madaniyatlarda hurmat qilinadi.")

@dp.message(Command('Qunduz'))
async def handle_message(message: Message):
    await message.answer("Qunduz — suvda ham, quruqlikda ham yashay oladigan yirik kemiruvchi hayvon bo‘lib, Castoridae oilasiga mansub. U asosan Shimoliy Amerika va Yevropaning sovuqroq hududlarida uchraydi. Qunduzning vazni 16—30 kilogramm atrofida bo‘lib, tanasi zich va suv o'tkazmaydigan jun bilan qoplangan. Ular daryolar va ko‘llar yaqinida yashaydi, daraxtlarni kesib, ularni g‘ovaklar qurish uchun ishlatadi. Qunduzlar o‘z yashash joylarini o‘zgartirib, g‘ovaklar quradi, bu esa atrof-muhitga ijobiy ta’sir ko‘rsatadi. Ular kechqurun faol bo‘lib, ozuqani asosan daraxt po‘stlog‘i va o‘tlar tashkil qiladi.")

@dp.message(Command('Tulpor'))
async def handle_message(message: Message):
    await message.answer("Tulpor — qadimiy va mardonavor ot zotlaridan biri bo‘lib, asosan Markaziy Osiyo hududlarida tarqalgan. U O‘rta asrlarda jang otlari sifatida keng qo‘llangan. Tulpor otlari tez yugurish qobiliyatiga ega, chidamliligi bilan ajralib turadi va uzoq masofalarga bardosh bera oladi. Ularning tanasi muskul va kuchli bo‘lib, baland bo‘yli bo‘ladi. Tulpor otlari ko‘pincha ko‘chmanchi xalqlar tomonidan o‘g‘rilik va janglarda ishlatilgan. Bugungi kunda ularning nasllari saqlanib qolgan va ko‘plab ot sporti turlarida ishtirok etadi.")

@dp.message(Command('Qirgiy'))
async def handle_message(message: Message):
    await message.answer("Qirg‘iy — yirik yirtqich qush bo‘lib, Accipitridae oilasiga mansub. U O‘zbekiston va boshqa Markaziy Osiyo mamlakatlarida keng tarqalgan. Qirg‘iy qanotlarini ochganda uzunligi taxminan 1,5 metrgacha yetadi, vazni esa 1—2 kilogramm atrofida bo‘ladi. Bu qush asosan mayda sutemizuvchilar, qushlar va sudralib yuruvchilar bilan oziqlanadi. Qirg‘iy kuchli tirnoqlari va tumshug‘i bilan o‘z ovini tutadi. Ular ko‘pincha ochiq joylarda, tog‘ va cho‘l hududlarida yashaydi. Qirg‘iylar tez va chaqqon uchish qobiliyatiga ega bo‘lib, ov paytida yuqori balandliklardan hujum qiladi.")

@dp.message(Command('Boriqush'))
async def handle_message(message: Message):
    await message.answer("Bo‘riqush — yirik yirtqich qushlardan biri bo‘lib, Falconidae oilasiga mansub. U asosan O‘zbekiston va Markaziy Osiyo hududlarida uchraydi. Bo‘riqush uzunligi taxminan 40-50 sm, qanotlarining ochilishi esa 1 metrga yaqin bo‘ladi. U juda tez va chaqqon uchuvchi qush hisoblanadi. Bo‘riqush asosan kichik sutemizuvchilar, qushlar va hasharotlar bilan oziqlanadi. U o‘zining o‘tkir ko‘zlari va kuchli tumshug‘i bilan ovini ushlaydi. Bu qushlar ochiq va to‘qayzor hududlarda yashashni afzal ko‘radi.")

@dp.message(Command('Kaklik'))
async def handle_message(message: Message):
    await message.answer("Kaklik — kichik va o‘rmon qushlari oilasiga mansub, odatda tog‘ va tepaliklarda yashovchi qush turi. Ularning uzunligi taxminan 30-40 santimetr atrofida bo‘lib, ko‘plab turlari mavjud. Kakliklar o‘zining go‘zal, rang-barang patlari bilan ajralib turadi va asosan yerda ovlanadi. Ular urug‘lar, barglar, mevalar va mayda hasharotlar bilan oziqlanadi. Kaklik qushlari ko‘pincha o‘rmon chetlarida, qoramol va toshloq yerlarda yashaydi. Ularning jonli ovozi va kurashuvchi tabiatlari ular uchun xarakterlidir.")

@dp.message(Command('Jayra'))
async def handle_message(message: Message):
    await message.answer("Jayra — O‘rta Osiyo va boshqa mintaqalarda uchraydigan yirtqich qushlardan biri. U Qirg‘iylar oilasiga mansub bo‘lib, o‘zining katta qanotlari va kuchli tirnoqlari bilan ajralib turadi. Jayraning tanasi uzunligi taxminan 70–90 sm, qanotlarini yoyganda esa 1,5 metrgacha yetishi mumkin. U asosan kichik sutemizuvchilar, qushlar va sudralib yuruvchilar bilan oziqlanadi.")

@dp.message(Command('Ilon'))
async def handle_message(message: Message):
    await message.answer("Ilon — sudralib yuruvchi sudraluvchilar sinfiga mansub hayvon. Ularning tanasi uzun va yupqa bo‘lib, oyoqlari yo‘q. Ilonlar turli xil muhitlarda yashaydi: o‘rmonlar, cho‘llar, botqoqlar va boshqalar. Ular asosan kichik hayvonlar bilan oziqlanadi. Ko‘pchilik ilonlar zaharli bo‘lishi mumkin, lekin ba’zilari zaharsiz. Ilonlar tishlari yordamida ovqatni ushlaydi va yutadi. Ularning ko‘plari terisini muntazam yangilab turadi.")

@dp.message(Command('Tasma_ilon'))
async def handle_message(message: Message):
    await message.answer("Tasma ilon — bu uzun va yupqa tana shakliga ega bo‘lgan sudralib yuruvchi hayvon. Unga “tasma” deb nom berilishining sababi tanasida chiziqlar yoki tasma shaklidagi naqshlar bo‘lishidir. Tasma ilonlar ko‘pincha o‘rmon va o'tloqlarda yashaydi. Ular kichik hayvonlar, masalan, kemiruvchilar va qushlarni ovqat qiladi. Ba’zi turlari oz miqdorda zaharli bo‘lishi mumkin, lekin odatda odamlar uchun xavf tug‘dirmaydi. Tasma ilonlar o‘zining nozik va moslashuvchan tana tuzilishi bilan yashash muhitida yaxshi harakatlana oladi.")

@dp.message(Command('Timsoh'))
async def handle_message(message: Message):
    await message.answer("Timsoh — yirik suvda yashovchi yirtqich sudraluvchilar oilasiga mansub hayvon. Ular asosan tropik va subtropik mintaqalarda, daryolar, ko'llar va botqoqlarda yashaydi. Timsohlar kuchli va bardoshli tana tuzilishiga ega bo‘lib, qattiq terisi va kuchli jag‘ mushaklari bilan mashhur. Ularning uzun tishlari va kuchli chaynash kuchi o‘ljani ushlashda yordam beradi. Timsohlar ovqat sifatida baliq, qushlar va boshqa hayvonlarni yeydi. Ular suvda juda yaxshi suzadi va yerda ham tez harakatlana oladi. Timsohlarning ko‘plab turlari mavjud bo‘lib, eng yiriklari 5 metrgacha uzunlikka yetadi. Ular odatda o‘z hududlarini himoya qiladi va agressiv bo‘lishi mumkin.")

@dp.message(Command('Chayon'))
async def handle_message(message: Message):
    await message.answer("Chayon — kichik o‘lchamli lekin zaharli hasharot, asosan issiq va quruq iqlimlarda yashaydi. Ularning tana uzunligi odatda 5 dan 20 santimetrgacha bo‘lib, ko‘p sonli turlari mavjud. Chayonlarning tanasi qattiq qobiq bilan qoplangan bo‘lib, ularni himoya qiladi. Eng xavflisi — ularning dumida joylashgan zaharli igna, bu zahar dushman yoki o‘ljaga zarar yetkazadi. Chayonlar asosan kechasi faol bo‘lib, kichik hasharotlar, maxluqlar bilan oziqlanadi. Ular tuproq ostida yoki toshlar ostida yashashni afzal ko‘radi. Chayon zahari ayrim turlarida inson uchun xavfli bo‘lishi mumkin, ammo ko‘pchilik uchun ular asosan xavfsizdir.")

@dp.message(Command('Qurbaqa'))
async def handle_message(message: Message):
    await message.answer("Qurbaqa — nam va suvli muhitlarda yashovchi amfibiya (ikkihayotli) hayvon. Ularning tanasi yumshoq, namlikni saqlovchi teri bilan qoplangan bo‘lib, suvda ham, quruqlikda ham yashay oladi. Qurbaqalar suvda tuxum qo‘yib, suvda yashovchi larvalar (kurbaqa tug‘malari) dan rivojlanadi. Ularning o‘lchami turlarga qarab o‘zgarib, kichikidan kattaigacha bo‘ladi. Qurbaqalar ko‘pincha hasharotlar, chiriyotgan o‘simliklar va kichik suv hayvonlarini yeydi. Ularning ovozi, ayniqsa yomg‘irli kunlarda, juda baland va eshitilishi mumkin. Qurbaqalar ekologik tizimda muhim rol o‘ynab, hasharotlarni nazorat qiladi va o‘z navbatida boshqa hayvonlar uchun oziq bo‘lib xizmat qiladi.")

@dp.message(Command('Baliq'))
async def handle_message(message: Message):
    await message.answer("Baliq — suvda yashovchi umurtqali hayvon bo‘lib, asosan suv ostida nafas olish uchun o‘pka o‘rniga suvdan kislorod oluvchi peshonalari bor. Ular turli o‘lcham va shakllarda bo‘lib, dengiz va sho‘r suv, shuningdek, sho‘ra va toza suv havzalarida uchraydi. Baliqlar oziq-ovqat zanjirida muhim rol o‘ynaydi va odamlar uchun ham asosiy protein manbai hisoblanadi.")

@dp.message(Command('Akula'))
async def handle_message(message: Message):
    await message.answer("Akula — dengizda yashovchi yirik yirtqich baliq bo‘lib, o‘zining keskin tishlari va tezligi bilan tanilgan. Ular asosan baliqlar, mollyuskalar va boshqa dengiz hayvonlari bilan oziqlanadi. Akulalar okean ekotizimida muhim rol o‘ynaydi va ko‘plab turlari mavjud, ularning ayrimlari xavfli hisoblanadi, ammo odamlar uchun odatda hujum qilmaydi.")

@dp.message(Command('Delfin'))
async def handle_message(message: Message):
    await message.answer("Delfin — akulli baliqlar oilasiga mansub, juda aqlli va ijtimoiy dengiz sutemizuvchilaridan biridir. Ular suv ostida yaxshi suzish qobiliyatiga ega, o‘zaro tovushlar va imo-ishoralar orqali muloqot qilishadi. Delfinlar ko‘pincha kichik baliqlar va kalmarlar bilan oziqlanadi. Ularning do‘stona tabiatlari va o‘rgatishga moyilligi tufayli odamlar bilan aloqasi yaxshi. Delfinlar ko‘plab madaniyatlarda donolik va do‘stlik ramzi sifatida qadrlanadi.")

@dp.message(Command('Kit'))
async def handle_message(message: Message):
    await message.answer("Kit — dunyodagi eng katta dengiz sutemizuvchisi bo‘lib, suv ostida yashaydi. U o‘ta katta hajmga ega, ba’zi turlari uzunligi 30 metrga va vazni 150 tonnagacha yetishi mumkin. Kitlar odatda dengizda plankton va kichik dengiz organizmlari bilan oziqlanadi. Ularning yurishi va ovoz chiqarishi dengizda uzoq masofalarni bosib o‘tishda yordam beradi. Kitlar ijtimoiy hayvonlar bo‘lib, guruhlarda yashaydi va murakkab muloqot tizimiga ega. Ular insoniyat tomonidan qadimdan e’tiborga olinib, ko‘plab madaniyatlarda muqaddas hayvon sifatida hurmat qilinadi.")

@dp.message(Command('Pingvin'))
async def handle_message(message: Message):
    await message.answer("Pingvin — qutb mintaqasida yashovchi, ucholmaydigan qush turidir. Ular sovuq iqlimga moslashgan va suvda juda yaxshi suzuvchilardir. Pingvinlar asosan baliq, kalmar va boshqa dengiz hayvonlari bilan oziqlanadi. Ularning tanasi qalin tuxum teri va yog‘ qatlami bilan qoplangan, bu sovuqqa chidamliligini ta’minlaydi. Quruqlikda esa ular tik yurishadi va ko‘pincha guruhlarda yashaydi. Pingvinlar ko‘plab turlarga bo‘linadi, eng mashhuri — imperator pingvini bo‘lib, u eng katta va eng sovuqqa chidamli hisoblanadi.")

@dp.message(Command('Ayroqi_baliq'))
async def handle_message(message: Message):
    await message.answer("Ayroqi baliq — ko‘pincha tropik va subtropik suv havzalarida uchraydigan, o‘ziga xos rang-barang va qiziqarli baliq turidir. Ularning tana tuzilishi turli ranglar va naqshlar bilan bezatilgan bo‘lib, ular o‘z yashash muhitida kamuflyaj vazifasini bajaradi. Ayroqi baliqlar asosan kichik dengiz organizmlari va plankton bilan oziqlanadi. Ular akvariumlarda ham keng tarqalgan, chunki juda chiroyli va o‘ziga jalb qiluvchi ko‘rinishga ega. Ayroqi baliqning ba’zi turlari sayoz suvda yashaydi, boshqalari esa chuqurroq dengiz zonalarida uchraydi.")

@dp.message(Command('Krab'))
async def handle_message(message: Message):
    await message.answer("Krab — dengizda va sho‘r suv havzalarida yashovchi, asosan qattiq qobiq bilan o‘ralgan, to‘rtta juft oyog‘i bor dengiz umurtqasiz hayvon. Ular o‘z tanasini himoya qilish uchun qobig‘idan foydalanadi. Krablar asosan suv tubida yashaydi va o‘simliklar hamda kichik hayvonlarni yeydi. Ularning qarsillagan oyoqlari va tez harakatlanishlari ularni yirtqichlardan himoya qiladi. Krablar sho‘rlik suvda va ba’zi turlari shirin suvda ham yashaydi. Ko‘plab mamlakatlarda krab go‘shti qadrlanadi va oziq-ovqat sifatida keng iste’mol qilinadi.")

@dp.message(Command('Omba'))
async def handle_message(message: Message):
    await message.answer("Omba — bu quruqlikda va suvda yashay oladigan, ko‘pincha Afrika va Osiyo daryolarida uchraydigan kichik yoki o‘rta o‘lchamdagi baliq yoki suv hayvonining nomi sifatida ishlatilishi mumkin. Lekin aniq “Omba” hayvoni haqida keng ma'lumot kam, chunki bu nom ba’zi hududlarda turlicha hayvonlarga nisbatan ishlatilishi mumkin.")

@dp.message(Command('Dengiz_yulduzi'))
async def handle_message(message: Message):
    await message.answer("Dengiz yulduzi — suyuq muhitda harakatlanadi. U oziq-ovqatni kichik mollyuskalar va baliqlardan oladi. Tabiatda ko‘plab turlari mavjud.")

@dp.message(Command('Meduza'))
async def handle_message(message: Message):
    await message.answer("Meduza — dengizda yashovchi yumshoq tanali hayvon. U o‘zining o‘tkir tikanlari bilan himoyalanadi. Ko‘pincha oqim bilan harakatlanadi.")

@dp.message(Command('Karakal'))
async def handle_message(message: Message):
    await message.answer("Karakal — o‘rta kattalikdagi yirtqich mushuk bo‘lib, Asiya va Afrikada yashaydi. Uzoq quloqlari va qora uchi bilan ajralib turadi. Tez va chaqqon yirtqich hisoblanadi, kichik hayvonlarni ovlaydi. Quruq joylarda ko‘p uchraydi.")

@dp.message(Command('Sirtlon'))
async def handle_message(message: Message):
    await message.answer("Sirtlon — o‘rta kattalikdagi yirtqich mushuk bo‘lib, mushuksimonlar oilasiga kiradi. U asosan Afrikada, xususan savanna va o‘rmonli hududlarda yashaydi. Tanasining uzunligi 1–1,5 metr, vazni 30–60 kg atrofida bo‘ladi. Sirtlonning terisi och sariq rangda bo‘lib, qora dog‘lar bilan qoplangan. U yolg‘iz yashaydi va kichik o‘lchamli hayvonlar, masalan, quyon, kiyik va qushlarni ovlaydi. Sirtlon juda yashirin harakat qiladi va daraxtlarga chiqish qobiliyatiga ega.")

@dp.message(Command('Kamelopard_jirafa'))
async def handle_message(message: Message):
    await message.answer("Kamelopard jirafa — jirafaning boshqa nomi bo‘lib, dunyodagi eng baland sutemizuvchi hayvon hisoblanadi. U Afrikaning savanna va o‘rmonli hududlarida yashaydi. Bo‘yi 4,5–6 metr, vazni 800–1200 kg gacha yetadi. Uzun bo‘yni va oyoqlari unga baland daraxtlarning barglarini, ayniqsa akatsiyani yeyish imkonini beradi. Jirafaning terisidagi noyob dog‘lar har bir hayvonda o‘ziga xosdir. Ular kichik guruhlarda yashaydi va tez yugurish qobiliyatiga ega.")

@dp.message(Command('Lama'))
async def handle_message(message: Message):
    await message.answer("Lama — Janubiy Amerikada, xususan And tog‘larida yashovchi uy hayvoni bo‘lib, kamelidlar oilasiga kiradi. U insonlar tomonidan yuk tashish va jun olish uchun boqiladi. Lamaning bo‘yi 1,7–1,9 metr, vazni 120–200 kg atrofida. Ular o‘t va boshqa o‘simliklar bilan oziqlanadi. Lamalar ijtimoiy hayvonlar bo‘lib, tinch tabiatga ega, ammo xavf sezganda tupurish orqali o‘zini himoya qiladi. Ular chidamli va uzoq masofalarga yurishga qodir.")

@dp.message(Command('Alpaka'))
async def handle_message(message: Message):
    await message.answer("Alpaka — lamaning kichikroq qarindoshi bo‘lib, Janubiy Amerikada, asosan Peru va Boliviyada boqiladi. U kamelidlar oilasiga kiradi va yumshoq, sifatli jun uchun yetishtiriladi. Alpakalar bo‘yi 0,8–1 metr, vazni 50–80 kg atrofida. Ular o‘t va boshqa o‘simliklar bilan oziqlanadi. Alpakalar juda tinch va ijtimoiy hayvonlar bo‘lib, odamlar bilan yaxshi munosabatda bo‘ladi. Ularning juni kiyim-kechak ishlab chiqarishda yuqori baholanadi.")

@dp.message(Command('Yalpiz_qush'))
async def handle_message(message: Message):
    await message.answer("Yalpiz qush — kichik, rang-barang qush bo‘lib, asosan tropik o‘rmonlarda yashaydi. Ularning patlari yorqin yashil, ko‘k va qizil ranglarda bo‘ladi. Yalpiz qushlar tez uchish qobiliyatiga ega bo‘lib, hasharotlar va nektar bilan oziqlanadi. Ularning uzun tumshug‘i va nozik qanotlari ovqat olishda yordam beradi. Yalpiz qushlar ko‘pincha o‘rmonlarda va bog‘larda uchraydi va tabiatda changlatuvchi sifatida muhim rol o‘ynaydi.")

@dp.message(Command('Kolibri'))
async def handle_message(message: Message):
    await message.answer("Kolibri — dunyodagi eng kichik qush turlaridan biri bo‘lib, Amerikada, xususan tropik va subtropik hududlarda yashaydi. Ularning vazni 2–20 gramm, uzunligi esa 5–10 sm atrofida. Kolibrilar juda tez qanot tebratishi (sekundiga 50–80 marta) bilan mashhur bo‘lib, havoda bir joyda qotib qolishi mumkin. Ular asosan nektar, hasharotlar va o‘simlik shirasi bilan oziqlanadi. Kolibrilarning yorqin, metall rangdagi patlari ularni juda jozibali qiladi.")

@dp.message(Command('Papagoy'))
async def handle_message(message: Message):
    await message.answer("Papagoy — rang-barang va aqlli qush bo‘lib, tropik va subtropik hududlarda, asosan Avstraliya, Janubiy Amerika va Afrikada yashaydi. Ularning patlari yorqin ko‘k, yashil, qizil va sariq ranglarda bo‘ladi. Papagoylar ovozlarni taqlid qilish qobiliyatiga ega bo‘lib, ba’zilari inson nutqini o‘rganadi. Ular meva, urug‘lar, hasharotlar va nektar bilan oziqlanadi. Papagoylar ijtimoiy hayvonlar bo‘lib, guruhlarda yashaydi va ko‘pincha uy hayvoni sifatida boqiladi.")

@dp.message(Command('Tukan'))
async def handle_message(message: Message):
    await message.answer("Tukan — Janubiy va Markaziy Amerikada yashovchi, katta va rang-barang tumshug‘i bilan mashhur qush. Ularning tumshug‘i yorqin ranglarda bo‘lib, tanasidan kattaroq ko‘rinadi. Tukanlar o‘rmonlarda yashaydi va meva, hasharotlar va kichik hayvonlar bilan oziqlanadi. Ularning uzunligi 30–60 sm atrofida, vazni esa 130–680 grammgacha bo‘ladi. Tukanlar ijtimoiy va shovqinli qushlar bo‘lib, o‘ziga xos ovozlari bilan muloqot qiladi.")

@dp.message(Command('Boyogli'))
async def handle_message(message: Message):
    await message.answer("Boyo‘g‘li — yirtqich qush bo‘lib, asosan Yevropa, Osiyo va Shimoliy Amerikada yashaydi. U boyo‘g‘lilar oilasiga kiradi va o‘zining o‘tkir ko‘zlari va kuchli tumshug‘i bilan mashhur. Boyo‘g‘lilar kechasi faol bo‘lib, kichik sutemizuvchilar, qushlar va hasharotlar bilan oziqlanadi. Ularning patlari yumshoq bo‘lib, ovoz chiqarmasdan uchishga yordam beradi. Boyo‘g‘lilar o‘rmonlarda, shahar atrofida va ochiq joylarda yashaydi.")

@dp.message(Command('Qunduz'))
async def handle_message(message: Message):
    await message.answer("Qunduz — suvda ham, quruqlikda ham yashay oladigan yirik kemiruvchi hayvon bo‘lib, Castoridae oilasiga mansub. U asosan Shimoliy Amerika va Yevropaning sovuqroq hududlarida uchraydi. Qunduzning vazni 16–30 kg atrofida bo‘lib, tanasi zich va suv o‘tkazmaydigan jun bilan qoplangan. Ular daryolar va ko‘llar yaqinida yashaydi, daraxtlarni kesib, g‘ovaklar quradi. Qunduzlar o‘z yashash joylarini o‘zgartirib, atrof-muhitga ijobiy ta’sir ko‘rsatadi. Ozuqa sifatida daraxt po‘stlog‘i va o‘tlar ishlatiladi.")

@dp.message(Command('Yirtqich_qush'))
async def handle_message(message: Message):
    await message.answer("Yirtqich qush — ov qilish uchun maxsus moslashgan qushlar guruhiga aytiladi, masalan, burgut, qirg‘iy, bo‘riqush va boshqalar. Ular o‘tkir tumshug‘i, kuchli tirnoqlari va ajoyib ko‘rish qobiliyati bilan ajralib turadi. Yirtqich qushlar asosan kichik sutemizuvchilar, boshqa qushlar, hasharotlar va sudraluvchilar bilan oziqlanadi. Ular ochiq joylarda, o‘rmonlarda va tog‘larda yashaydi, ko‘pincha baland joylarda uya quradi.")

@dp.message(Command('Qizil_bori'))
async def handle_message(message: Message):
    await message.answer("Qizil bo‘ri — Canidae oilasiga mansub yirtqich hayvon bo‘lib, Shimoliy Amerika va Yevrosiyoda yashaydi. U oddiy bo‘ridan kichikroq bo‘lib, vazni 20–40 kg, uzunligi 1–1,3 metr atrofida. Qizil bo‘rilar qizg‘ish-kulrang junlari bilan ajralib turadi. Ular to‘da bo‘lib yashaydi va kichik sutemizuvchilar, qushlar va o‘simliklar bilan oziqlanadi. Qizil bo‘rilar tabiatda muvozanatni saqlashda muhim rol o‘ynaydi.")

@dp.message(Command('Koala'))
async def handle_message(message: Message):
    await message.answer("Koala — Avstraliyaga xos marsupial hayvon bo‘lib, koala oilasiga kiradi. U o‘zining yumshoq kulrang junlari va katta quloqlari bilan mashhur. Koalalar daraxtlarda yashaydi va asosan evkalipt barglari bilan oziqlanadi. Ularning vazni 4–15 kg, uzunligi esa 60–85 sm atrofida. Koalalar ko‘p vaqtini daraxtlarda uxlab o‘tkazadi, chunki evkalipt barglari past kaloriyali bo‘lib, energiyani tejashga majbur qiladi. Ular yolg‘iz yashaydi va tinch tabiatga ega.")

@dp.message(Command('Panda'))
async def handle_message(message: Message):
    await message.answer("Panda — Xitoyning tog‘li hududlarida yashovchi ayiqsimon hayvon bo‘lib, o‘zining oq-qora rangli junlari bilan tanilgan. Ularning vazni 70–120 kg, uzunligi 1,2–1,8 metr atrofida. Pandalar asosan bambuk bilan oziqlanadi, lekin ba’zida kichik hayvonlar va hasharotlar ham yeydi. Pandalar yolg‘iz yashaydi va ko‘pincha tinch tabiatga ega. Ular yo‘qolib ketish xavfi ostida bo‘lib, tabiatni muhofaza qilish dasturlari orqali himoyalanadi.")

@dp.message(Command('Lemur'))
async def handle_message(message: Message):
    await message.answer("Lemur — Madagaskarga xos primat bo‘lib, lemurlar oilasiga kiradi. Ularning uzunligi 30–60 sm, vazni 0,5–5 kg atrofida bo‘ladi. Lemurlar daraxtlarda yashaydi va meva, barglar, hasharotlar bilan oziqlanadi. Ular ijtimoiy hayvonlar bo‘lib, guruhlarda yashaydi va o‘ziga xos ovozlar orqali muloqot qiladi. Lemurlarning ko‘zlari katta va kechasi yaxshi ko‘rishga yordam beradi. Ular yo‘qolib ketish xavfi ostida bo‘lib, himoya qilinadi.")

@dp.message(Command('Orangutan'))
async def handle_message(message: Message):
    await message.answer("Orangutan — Janubi-Sharqiy Osiyoda, xususan Borneo va Sumatra o‘rmonlarida yashovchi katta primat. Ularning vazni 30–90 kg, uzunligi 1,2–1,5 metr atrofida. Orangutanlar qizg‘ish-jigarrang junlari va uzun qo‘llari bilan ajralib turadi. Ular daraxtlarda yashaydi, meva, barglar va hasharotlar bilan oziqlanadi. Orangutanlar juda aqlli bo‘lib, asboblardan foydalanish qobiliyatiga ega. Ular yolg‘iz yashaydi va yo‘qolib ketish xavfi ostida.")

@dp.message(Command('Shimpanze'))
async def handle_message(message: Message):
    await message.answer("Shimpanze — Afrikada yashovchi primat bo‘lib, insonning eng yaqin qarindoshi hisoblanadi. Ularning vazni 40–70 kg, uzunligi 1–1,7 metr atrofida. Shimpanzelar ijtimoiy hayvonlar bo‘lib, guruhlarda yashaydi va murakkab muloqot tizimiga ega. Ular meva, barglar, hasharotlar va ba’zida kichik hayvonlar bilan oziqlanadi. Shimpanzelar asboblardan foydalanish va muammolarni hal qilish qobiliyati bilan mashhur. Ular himoya ostida, chunki yashash joylari kamaymoqda.")

@dp.message(Command('Babun'))
async def handle_message(message: Message):
    await message.answer("Babun — Afrikada va Arabistonning ba’zi qismlarida yashovchi primat bo‘lib, maymunlar oilasiga kiradi. Ularning vazni 15–40 kg, uzunligi 50–100 sm atrofida. Babunlar o‘zining katta tishlari va uzun yuzlari bilan ajralib turadi. Ular ijtimoiy hayvonlar bo‘lib, katta guruhlarda yashaydi. Babunlar meva, o‘simliklar, hasharotlar va kichik hayvonlar bilan oziqlanadi. Ular o‘z guruhlarini himoya qilishda agressiv bo‘lishi mumkin.")

@dp.message(Command('Nosorog'))
async def handle_message(message: Message):
    await message.answer("Nosorog — Afrikada va Osiyoda yashovchi yirik sutemizuvchi hayvon bo‘lib, o‘zining katta shoxi va qalin terisi bilan mashhur. Ularning vazni 800–2500 kg, uzunligi 3–4 metr atrofida. Nosoroglar o‘simlikxo‘r bo‘lib, o‘tlar, barglar va butalar bilan oziqlanadi. Ular yolg‘iz yashaydi va ko‘pincha tinch tabiatga ega, ammo xavf sezganda agressiv bo‘lishi mumkin. Nosoroglar yo‘qolib ketish xavfi ostida bo‘lib, himoya qilinadi.")

@dp.message(Command('Tovushqon'))
async def handle_message(message: Message):
    await message.answer("Tovushqon — kichik sutemizuvchi hayvon bo‘lib, quyonlar oilasiga kiradi. Ular Yevropa, Osiyo va boshqa hududlarda yashaydi. Tovushqonlarning vazni 1–2 kg, uzunligi 30–50 sm atrofida. Ular tez yugurish qobiliyatiga ega bo‘lib, o‘tlar, barglar va ildizlar bilan oziqlanadi. Tovushqonlar ko‘pincha yirtqichlardan qochish uchun chuqurchalarda yashaydi. Ular ijtimoiy hayvonlar bo‘lib, guruhlarda yashashni afzal ko‘radi.")

@dp.message(Command('Kirpi'))
async def handle_message(message: Message):
    await message.answer("Kirpi — kichik sutemizuvchi hayvon bo‘lib, o‘zining tikanli junlari bilan mashhur. Ular Yevropa, Osiyo va Afrikada yashaydi. Kirpi uzunligi 20–30 sm, vazni 0,5–1,2 kg atrofida. Ular hasharotlar, kichik sudraluvchilar va o‘simliklar bilan oziqlanadi. Kirpilar tikanlari orqali yirtqichlardan himoyalanadi va xavf paytida shar shaklida o‘raladi. Ular kechasi faol bo‘lib, qishda uyquga ketadi.")

@dp.message(Command('Kalamush'))
async def handle_message(message: Message):
    await message.answer("Kalamush — kichik kemiruvchi hayvon bo‘lib, dunyoning deyarli barcha hududlarida yashaydi. Ularning uzunligi 20–40 sm, vazni 100–500 gramm atrofida. Kalamushlar juda moslashuvchan bo‘lib, shaharlar, qishloqlar va o‘rmonlarda yashaydi. Ular hamma narsani yeydi: o‘simliklar, oziq-ovqat qoldiqlari va kichik hayvonlar. Kalamushlar aqlli va ijtimoiy bo‘lib, guruhlarda yashaydi. Ular tez ko‘payadi va ba’zida zararkunanda sifatida ko‘riladi.")

@dp.message(Command('Sichqon'))
async def handle_message(message: Message):
    await message.answer("Sichqon — kichik kemiruvchi hayvon bo‘lib, dunyoning ko‘p joylarida uchraydi. Ularning uzunligi 8–10 sm, vazni 20–50 gramm atrofida. Sichqonlar o‘simliklar, urug‘lar va kichik hasharotlar bilan oziqlanadi. Ular juda chaqqon va tez ko‘payadi. Sichqonlar shahar va qishloq muhitlarida yashaydi, ko‘pincha uylarda oziq-ovqat qoldiqlarini yeydi. Ularning kichik o‘lchami ularni yirtqichlardan yashirinishga yordam beradi.")

@dp.message(Command('Tarakan'))
async def handle_message(message: Message):
    await message.answer("Tarakan — dunyoda keng tarqalgan hasharot bo‘lib, issiq va nam muhitlarda yashaydi. Ularning uzunligi 1–5 sm atrofida bo‘lib, qattiq qanotlari va tez harakatlanish qobiliyatiga ega. Tarakonlar hamma narsani yeydi: oziq-ovqat qoldiqlari, o‘simliklar va hatto organik moddalar. Ular juda chidamli bo‘lib, og‘ir sharoitlarda ham yashay oladi. Tarakonlar ko‘pincha zararkunanda sifatida ko‘riladi va ularning tez ko‘payishi muammo hisoblanadi.")

@dp.message(Command('Orgimchak'))
async def handle_message(message: Message):
    await message.answer("O‘rgimchak — sakkiz oyoqli hasharot bo‘lib, dunyoning deyarli barcha hududlarida uchraydi. Ular o‘zining to‘r to‘qish qobiliyati bilan mashhur bo‘lib, bu to‘r orqali hasharotlarni ovlaydi. O‘rgimchaklarning o‘lchami bir necha millimetrdan bir necha santimetrgacha bo‘ladi. Ular asosan hasharotlar bilan oziqlanadi. Ba’zi turlari zaharli bo‘lib, odamlar uchun xavf tug‘dirishi mumkin, lekin ko‘pchiligi xavfsizdir. O‘rgimchaklar tabiatda hasharotlarni nazorat qilishda muhim rol o‘ynaydi.")

@dp.message(Command('Chivin'))
async def handle_message(message: Message):
    await message.answer("Chivin — kichik uchuvchi hasharot bo‘lib, dunyoda minglab turlari mavjud. Ularning uzunligi odatda 3–10 mm atrofida. Chivinlar ko‘pincha nam muhitlarda yashaydi va organik moddalar, nektar yoki qon bilan oziqlanadi. Ba’zi turlari, masalan, bezgak chivini, kasallik tarqatuvchi sifatida xavflidir. Chivinlarning tez ko‘payishi va keng tarqalishi ularni zararkunanda sifatida ko‘rishga sabab bo‘ladi.")

@dp.message(Command('Laylak'))
async def handle_message(message: Message):
    await message.answer("Laylak — katta, uzun oyoqli qush bo‘lib, ko‘pincha Yevropa, Afrika va Osiyoda uchraydi. Ularning qanotlari keng, uzunligi 1,5–2 metr atrofida. Laylaklar ko‘chmanchi qushlar bo‘lib, qishda issiq mintaqalarga ko‘chib o‘tadi. Ular asosan hasharotlar, baliqlar va kichik sudraluvchilar bilan oziqlanadi. Laylaklar o‘zining katta uyalari bilan mashhur bo‘lib, ko‘pincha daraxtlar yoki binolar tepasida uya quradi. Ular ko‘plab madaniyatlarda omad va farovonlik ramzi sifatida qadrlanadi.")

@dp.message(Command('Turna'))
async def handle_message(message: Message):
    await message.answer("Turna — uzun oyoqli va uzun bo‘yinli qush bo‘lib, ko‘pincha botqoqli va suvli hududlarda yashaydi. Ularning uzunligi 1–1,4 metr, qanotlari keng bo‘lib, 2 metrgacha ochiladi. Turnalar ko‘chmanchi qushlar bo‘lib, hasharotlar, baliqlar va o‘simliklar bilan oziqlanadi. Ular o‘zining o‘ziga xos raqsi va baland ovozlari bilan mashhur. Turnalar ko‘plab madaniyatlarda uzoq umr va sadoqat ramzi sifatida hurmat qilinadi.")

@dp.message(Command('Qaz'))
async def handle_message(message: Message):
    await message.answer("Qaz — suv qushlari oilasiga mansub bo‘lib, g‘ozga o‘xshash, lekin kichikroq. Ular Yevropa, Osiyo va Shimoliy Amerikada yashaydi. Qazlarning uzunligi 60–90 sm, vazni 2–4 kg atrofida. Ular o‘tlar, urug‘lar va suv o‘simliklari bilan oziqlanadi. Qazlar ko‘chmanchi bo‘lib, qishda issiqroq hududlarga uchib o‘tadi. Ular ijtimoiy hayvonlar bo‘lib, guruhlarda yashaydi va o‘ziga xos ovozlari bilan muloqot qiladi.")

@dp.message(Command('Kaptar'))
async def handle_message(message: Message):
    await message.answer("Kaptar — dunyoda keng tarqalgan qush bo‘lib, ko‘pincha shaharlarda va qishloqlarda uchraydi. Ularning uzunligi 30–35 sm, vazni 300–400 gramm atrofida. Kaptarlar urug‘lar, donlar va oziq-ovqat qoldiqlari bilan oziqlanadi. Ular ijtimoiy bo‘lib, guruhlarda yashaydi va o‘zining yo‘naltirish qobiliyati bilan mashhur. Kaptarlar ko‘p madaniyatlarda tinchlik ramzi sifatida qadrlanadi.")

@dp.message(Command('Sichqoncha'))
async def handle_message(message: Message):
    await message.answer("Sichqoncha — kichik kemiruvchi hayvon bo‘lib, sichqonlarga o‘xshaydi, lekin yanada kichikroq. Ularning uzunligi 5–10 sm, vazni 10–30 gramm atrofida. Sichqonchalar o‘simliklar, urug‘lar va kichik hasharotlar bilan oziqlanadi. Ular shahar va qishloq muhitlarida yashaydi, ko‘pincha yirtqichlardan yashirinish uchun chuqurchalarda yoki yoriqlarda yashaydi.")

@dp.message(Command('Korshapalak'))
async def handle_message(message: Message):
    await message.answer("Korshapalak — yagona uchuvchi sutemizuvchi hayvon bo‘lib, dunyoning ko‘p hududlarida yashaydi. Ularning qanotlari uzunligi 15 sm dan 1,7 metrgacha bo‘ladi. Korshapalaklar kechasi faol bo‘lib, hasharotlar, meva yoki qon bilan oziqlanadi. Ular ovozli echolokatsiya orqali yo‘nalish topadi. Korshapalaklar tabiatda hasharotlarni nazorat qilishda muhim rol o‘ynaydi.")

@dp.message(Command('Tilla_baliqcha'))
async def handle_message(message: Message):
    await message.answer("Tilla baliqcha — kichik, rang-barang akvarium baliqlari bo‘lib, asosan uy hayvoni sifatida boqiladi. Ularning uzunligi 5–15 sm atrofida bo‘lib, yorqin sariq, qizil yoki oq ranglarda bo‘ladi. Tilla baliqchalar o‘simliklar, kichik hasharotlar va maxsus baliq ovqatlari bilan oziqlanadi. Ularning chiroyli ko‘rinishi va oson parvarishi ularni mashhur uy hayvoniga aylantirgan.")

@dp.message(Command('Yilqiboqar'))
async def handle_message(message: Message):
    await message.answer("Yilqiboqar — dengizda yashovchi umurtqasiz hayvon bo‘lib, ko‘pincha suv tubida yoki qoyalarda uchraydi. Ularning tanasi o‘ziga xos shaklda bo‘lib, uzun oyoqlari bilan harakatlanadi. Yilqiboqarlar kichik dengiz hayvonlari va o‘simliklar bilan oziqlanadi. Ularning qattiq qobig‘i ularni yirtqichlardan himoya qiladi.")

@dp.message(Command('Qoramol_bugu'))
async def handle_message(message: Message):
    await message.answer("Qoramol bug‘u — katta shoxli hayvon bo‘lib, Yevropa, Osiyo va Shimoliy Amerikada yashaydi. Ularning vazni 100–300 kg, uzunligi 1,5–2,5 metr atrofida. Erkaklarning katta, shoxli shoxlari har yili yangilanadi. Qoramol bug‘ulari o‘simlikxo‘r bo‘lib, o‘tlar, barglar va daraxt po‘stlog‘i bilan oziqlanadi. Ular ijtimoiy bo‘lib, guruhlarda yashaydi.")

@dp.message(Command('Giyohxor_qush'))
async def handle_message(message: Message):
    await message.answer("Giyohxor qush — o‘simliklar bilan oziqlanadigan qush turlari guruhiga aytiladi. Ular urug‘lar, meva va barglar bilan oziqlanadi. Giyohxor qushlar ko‘pincha o‘rmonlarda, bog‘larda va ochiq joylarda yashaydi. Ularning tumshug‘i o‘simliklarni yeyishga moslashgan bo‘lib, ekologiyada urug‘larni tarqatishda muhim rol o‘ynaydi.")

@dp.message(Command('Qor_bars'))
async def handle_message(message: Message):
    await message.answer("Qor bars — yirik yirtqich mushuk bo‘lib, Osiyoning tog‘li hududlarida yashaydi. Ularning vazni 25–55 kg, uzunligi 1–1,3 metr atrofida. Qor barslari oq-kulrang junlari bilan ajralib turadi, bu ularni sovuq muhitda kamuflyaj qiladi. Ular kiyik, qo‘y va boshqa tog‘ hayvonlari bilan oziqlanadi. Qor barslari yolg‘iz yashaydi va yo‘qolib ketish xavfi ostida.")

@dp.message(Command('Chakalak_qush'))
async def handle_message(message: Message):
    await message.answer("Chakalak qush — kichik, faol qush bo‘lib, ko‘pincha o‘rmon va bog‘larda uchraydi. Ularning uzunligi 10–15 sm atrofida bo‘lib, hasharotlar va urug‘lar bilan oziqlanadi. Chakalak qushlar tez harakatlanadi va o‘zining shovqinli ovozlari bilan mashhur. Ular tabiatda hasharotlarni nazorat qilishda yordam beradi.")

@dp.message(Command('Dov_dov_qush'))
async def handle_message(message: Message):
    await message.answer("Dov-dov qush — kichik qush bo‘lib, kaptarlarga o‘xshaydi va o‘zining yumshoq, takrorlanuvchi ovozlari bilan tanilgan. Ular urug‘lar, meva va kichik hasharotlar bilan oziqlanadi. Dov-dov qushlar o‘rmonlarda, bog‘larda va shahar atrofida yashaydi. Ular tinchlik va sevgi ramzi sifatida ko‘plab madaniyatlarda hurmat qilinadi.")

@dp.message(Command('Burama_shoxli_kiyik'))
async def handle_message(message: Message):
    await message.answer("Burama shoxli kiyik — o‘zining o‘ziga xos burama shoxlari bilan mashhur bo‘lgan kiyik turi. Ular Yevropa va Osiyoda yashaydi, vazni 30–100 kg atrofida. Burama shoxli kiyiklar o‘simlikxo‘r bo‘lib, o‘tlar, barglar va mevalar bilan oziqlanadi. Ular ijtimoiy bo‘lib, guruhlarda yashaydi va yirtqichlardan qochish uchun tez yuguradi.")

@dp.message(Command('Qizil_tulki'))
async def handle_message(message: Message):
    await message.answer("Qizil tulki — eng keng tarqalgan tulki turi bo‘lib, Yevropa, Osiyo, Shimoliy Amerika va Avstraliyada yashaydi. Ularning vazni 5–10 kg, uzunligi 60–90 sm atrofida. Qizil tulkilar qizg‘ish junlari va uzun dumlari bilan ajralib turadi. Ular hamma narsani yeydi: kichik hayvonlar, o‘simliklar va hasharotlar. Tulkilar ayyor va moslashuvchan bo‘lib, shahar va qishloq muhitlarida yashaydi.")

@dp.message(Command('Dovon_mushugi'))
async def handle_message(message: Message):
    await message.answer("Dovon mushugi — kichik yirtqich mushuk bo‘lib, O‘rta Osiyo va boshqa tog‘li hududlarda yashaydi. Ularning vazni 2–6 kg, uzunligi 50–80 sm atrofida. Dovon mushuklari yolg‘iz yashaydi va kichik sutemizuvchilar, qushlar va hasharotlar bilan oziqlanadi. Ularning junlari qalin bo‘lib, sovuq muhitga moslashgan. Dovon mushuklari kechasi faol va juda yashirin harakat qiladi.")

@dp.message(Command('Yilqiboqar'))
async def handle_message(message: Message):
    await message.answer("Yilqiboqar – bu hayvon nomi sifatida ko‘pchilikka notanish bo‘lishi mumkin, chunki u xalq og‘zaki ijodida yoki eski adabiy matnlarda uchrashi mumkin. Keling, so‘zni tahlil qilib tushunishga harakat qilaylik:")

@dp.message()
async def hamma_message(message: Message):
    await message.reply("Iltimos Mavjut bolgan Hayvon nomini / dan keyin kiriting !")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())
