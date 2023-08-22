# Copyright (C) 2021-2023, Mindee.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://opensource.org/licenses/Apache-2.0> for full license details.

import string
from typing import Dict

__all__ = ["VOCABS"]


VOCABS: Dict[str, str] = {
    "digits": string.digits,
    "ascii_letters": string.ascii_letters,
    "punctuation": string.punctuation,
    "currency": "£€¥¢฿",
    "ancient_greek": "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
    "arabic_letters": "ءآأؤإئابةتثجحخدذرزسشصضطظعغـفقكلمنهوىي",
    "persian_letters": "پچڢڤگ",
    "hindi_digits": "٠١٢٣٤٥٦٧٨٩",
    "arabic_diacritics": "ًٌٍَُِّْ",
    "arabic_punctuation": "؟؛«»—",
    "sanskrit_unicode": "ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓क़ख़ग़ज़ड़ढ़फ़य़ॠॢॣ।॥०१२३४५६७८९॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ",
    "sanskrit_numerals": "१२३४५६७८९०",
    "sanskrit_alphabets":"अआइईउऊएऐओऔअंअँअःआःआंआँइःइंइँईःईंउःउँउंऊःऊँऊंएःएँएंऐःऐंओःओंऔःऔंऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवसशषहक्षत्रज्ञकाकिकीकुकूक्रर्ककृकोकौकेकैकंक़कॉकःकखाखिखीखुखूखेखैख्रर्खख़खॉखंखृखोखौखःगागिगीगुगूगेगैगोगौगृग्रर्गगॉग़गंगःघौघैघाघीघूघ़घॉघृघोघेघिघुघंघॅघःघँघङृङौङैङाङीङूङङॉङोङेङ्ङिङुङंङ्रङॅङँचृचौचैचाचीचूच़चॉचोचेचिचुचंच्रचॅचँर्चचःछृछौछैछाछीछूछ़छॉछोछेछिछुछंछॅछ्रर्छछँछःजृजौजैजाजीजूज़जॉजोजेजिजुजंजॅज्रर्जजँजःझृझौझैझाझीझूझ़झॉझोझेझिझुझंझॅझ्रझःर्झझँञःञॉञंञँटृटौटैटाटीटूट़टॉटोटेटिटुटंटॅट्रर्टटःटँठृठौठैठाठीठूठ़ठॉठोठेठिठुठंठॅठ्रठःर्ठठँडृडौडैडाडीडूडॉडोडेडिडुडंडॅड्रडःर्डडँढृढौढैढाढीढूढ़ढॉढोढेढिढुढंढॅढ्रढःढँणृणौणैणाणीणूणॉणोणेणिणुणंणॅण्रणःणँर्णतृतौतैतातीतूत़तॉतोतेतितुतंतॅत्रतःततँर्तथृथौथैथाथीथूथ़थॉथोथेथिथुथंथॅथ्रथःथँर्थदृदौदैदादीदूद़दॉदोदेदिदुदंदॅद्रदःदँर्दधृधौधैधाधीधूध़धॉधोधेधिधुधंधॅध्रधःधँर्धनौनैनानीनूनृनोनेनिनुनंनॅन्रनःनँनॉऩपृपौपैपापीपूप़पॉपोपेपिपुपंपॅप्रपःर्पपँफृफौफैफाफीफूफ़फॉफोफेफिफुफंफॅफ्रफःफँँर्फबृबौबाबीबूब़बॉबोबेबिबुबंबॅब्रबःर्बबँभृभौभैभाभीभूभ़भॉभोभेभिभुभंभॅभ्रभःभँर्भमृमौमैमामीमूम़मॉमोमेमिमुमंमॅम्रमःमँर्मयृयौयैयायीयूय़यॉयोयेयियुयंयॅय्रयःयँर्यरृरौरैरारीरूऱरॉरोरेरिरुरंरॅर्ररःरँलृलौलैलालीलूल़लॉलोलेलिलुलंलॅल्रलःलँर्लवृवौवैवावीवूव़वॉवोवेविवुवंवॅव्रवःवँर्वसृसौसैसासीसूस़सॉसोसेसिसुससंसॅस्रसःसँर्सशृशौशैशाशीशूश़शॉशोशेशिशुशंशॅश्रशःशँर्शषृषौषैषाषीषूष़षॉषोषेषिषुषंषॅष्रषःर्षषँहृहौहैहाहीहूह़हॉहोहेहिहुहंहॅह्रहःहँर्हश्रृश्रौश्रैश्राश्रीश्रूश्रॉश्रोश्रेश्रिश्रुश्रंश्रॅश्रःश्रँर्श्रक्षृक्षौक्षैक्षाक्षीक्षूक्ष़क्षॉक्षोक्षेक्षिक्षुक्षंक्षॅक्ष्रक्षःक्षँर्क्षत्रृत्रौत्रैत्रात्रीत्रूत्ऱत्रॉत्रोत्रेत्रित्रुत्रंत्रॅत्रःत्रँर्त्रळः",
    
    "sanskrit_transliterated": "'(-0123456789:A[abcdeghijklmnoprstuvy|ñāēīōśū̥̄̐।॥ḍḥṁṃṅṇṛṣṭ", #.\u200c\u200d",
    "sanskrit_transliterated_refined": "ÑñĀāēĪīōŚśŪū˜।॥ḌḍḤḥḶḷḸḹḺḻṁṂṃṄṅṆḷṚṛṜṝṢṣṬṭ"

}

VOCABS['bengali'] = 'শ০ূৃৰজআঔঅঊিঢ়খ৵পঢই৳ফঽ৪লেঐযঃঈঠুধড়৲ৄথভটঁঋৱরডৢছ৴ঙওঘস১৹ণগ৷৩ত৮হ৭োষৎ৶কন৬চমৈা়ীৠঝএ৻ব৯য়উৌঞ৺২ংৣদ৫্ৗ-।'
VOCABS['gujarati'] = '૮લઔ૨સખાઑઈઋૐઓવૄ૦઼ઁનઞઊ૫ીશફણ૬૭બ૧રળૌુઠઐઉષપેઇઅૃઝજૉક૱૯ગઍદો૪ૅએંહડઘ૩ૂછઙઃઽટતધિૈયઢ્આમથચભ-'
VOCABS['gurumukhi'] = 'ਗ਼ਵਨਁਰਊਖਂਆਜੈਲੴਣ੧ਛਭਫ੮੯ਚਔੀਯਹਲ਼ਞ੩ੜਫ਼ੁਮ੫ਤੇਦਸ਼ਟੰ੭ਓਅਃਡਾਉਠੱਈ੦ੵਖ਼ਏਕਥ੬ਧੲੑਝਿ੨ਐਬਪਘਸ਼ਙੌਜ਼ੋਗ੍ੳਇ੪ੂਢ-।'
VOCABS['kannada'] = 'ಚೕಒಉೖಂಲಾಝಟೆಅ೬ೇ೨ಬಡವಜಢಞಔಏಧಶಭತಳೀಕಐಈಠಪ೫ಣ೮ೞಆಯುಗೢಋದಘೂ್ೈ೦ಓಱಃಹ೯ೋಮ೭ೠಥಖಫಇರ೪ಛಙೣಿ೩ೌೄಷಌಸನ಼ಊಎ೧ೃೊ-'
VOCABS['malayalam'] = '൪ഉ൮ള൵ഔംസഞഎഷ൫ൄൌ-ഃൈീഌഛഇണാഈഹധ൭ജച൱൴൹യതൻശഒ൯ഗർഊആവഖൠൣ൩ോൽ൧അ൳ൗപഭൃ്മെഐൡഓദഏറിഠരൺ൰ൾങട൦ഢൢഡലേഴഝൊ൲ബനൂഥൿഘഫുഋക൬൨ '
VOCABS['odia'] = 'ଖ୯୬ୋଓଞ୍ଶ୪ଣଥଚରୄତଃେ୮ଆକଵୂନଦ୰ୖୢଜଉଳଅଁଲଯଔପ୭ଷଢଡ଼ଊୟମିୁ୧ଂ଼ୀବଟଭଢ଼୦ଘଠୗ୫ୡାଐ୨ଙହଈୱ୩ୃଛଏୌଗଫସଇଧଡଝୈୣୠଋ-।'
VOCABS['tamil'] = 'ய௴ஷ௫ைெஸஎஈோவ௲ூு௭அ்ஶி௰ஹ௧ௐா௮ஔ௺சீண௩இனஆழ௪௯ஙஊதஜ௷௶மௌள௸ஐபநேற௬டஒ௹ஞஉஏகௗொர௱௵ஃ௨லஓ௳௦-'
VOCABS['telugu'] = '౦ఱకఆఋడత౯౻ిహౌ౭౽ఉ౮్ధఓగ౼మ౫ూౠఔాఇనైఁజీౄుేసశృఃఝఢరఠలోఞౘఅ౹౧ౢఛబ౸ఐయ౩ఖటచెొఊదఈషథభఏౙ౬౾ఎ౪ణఒప౨ఫంఘఙళవ౺-'
VOCABS['urdu'] = 'ٱيأۃدےش‘زعكئںسحٰنؐةقذ؟ؔ۔—ًمھٗپغٖطإؒرڑصټٍگاؤجضْﷺچ‎ۓِّؓٹظىتڈ‍یُه،خو؛آفبؑلہثﺅ‌ژَۂءک‏'



VOCABS['hindi'] = 'ॲऽऐथफएऎह८॥ॉम९ुँ१ं।षघठर॓ॼड़गछिॱटऩॄऑवल५ढ़य़अञसऔयण॑क़॒ौॽशऍ॰ूीऒॊख़उज़ॻॅ३ओऌळनॠ०ेढङ४़ॢग़पऊॐज२डैभझकआदबऋखॾ॔ोइ्धतफ़ईृःा६चऱऴ७-'
VOCABS['sanskrit']='ज़ऋुड़ऍऐक५टय४उः३ॠध९्७ू१वऌौॐॡॢइ६ाै८नृअंथढेखऔघग़०लजोईरञपफँझभषॅॄगतचहसीढ़आशए।म२दठङबिऊडओळछण़ऽ'
VOCABS['devanagari'] = 'रचख़३ॾऍृेञलॻॉऴषॐॢ१य०ॽएा२ई।ग़७टऐय़॥तोदऽभुनओऒ-ठँ.ौ्८ॼझॠविःक़ी॰छॅॊऩऱ़थजशळङअऋखबफउ५फ़६ऊॲॆज़कढ़मूस॓इऔह॑ैगढॣधआड़९ं४डणपॄघऑ'
VOCABS["latin"] = (
    VOCABS["digits"] 
    + VOCABS["ascii_letters"] 
    + VOCABS["punctuation"]
    )
VOCABS["english"] = VOCABS["latin"] + "°" + VOCABS["currency"]
VOCABS["legacy_french"] = VOCABS["latin"] + "°" + "àâéèêëîïôùûçÀÂÉÈËÎÏÔÙÛÇ" + 'oQॐ∗}̭≥Ñࢇu–ा1\'°9śা२+hजষअॣ∘V̤औw`(तū$ऋऐौषचऩ३Cघ[িk”छपs∓aे…‍उOeऽl)य़⊤थḹ⌊র९१ठऱপটṣṃ:g“q!yলय~ल|◌p̂]PTকसz&Uैṝॊ—ẏबখṛळआ×ँ॰’ी॑Kdग०ड़ॄZ६F−ġहṟ4{द̇ऌॡ≤⋆Sᳳ∴\bखবॅ्⌋.>झढ़0ò॥ṭ∵∿एīঃ8?वुङ-IिBiশrnm͟ज़HृW2xYন%७ट6Xॉढ/भ‑=fःधṇṅ‌A∼Rvञ४7ॠ5èুম∾Mḍशइ८D𝜁ऎ÷,ोण;मू†Lস3कडḥjॢEñ∙∻∽GJী५फṉcā*‘़∮ḷ"रऊ<্॒न_√tई।∠ओ' + VOCABS["currency"] #+ VOCABS["sanskrit_transliterated"]
VOCABS["french"] = VOCABS["english"] + "'(-.0123456789:A[abcdeghijklmnoprstuvy|ñāēīōśū̥̄̐।॥ḍḥṁṃṅṇṛṣṭ\u200c\u200d" #"àâéèêëîïôùûüçÀÂÉÈÊËÎÏÔÙÛÜÇ"
VOCABS["portuguese"] = VOCABS["english"] + "áàâãéêíïóôõúüçÁÀÂÃÉÊÍÏÓÔÕÚÜÇ"
VOCABS["spanish"] = VOCABS["english"] + "áéíóúüñÁÉÍÓÚÜÑ" + "¡¿"
VOCABS["german"] = VOCABS["english"] + "äöüßÄÖÜẞ"
VOCABS["arabic"] = (
    VOCABS["digits"]
    + VOCABS["hindi_digits"]
    + VOCABS["arabic_letters"]
    + VOCABS["persian_letters"]
    + VOCABS["arabic_diacritics"]
    + VOCABS["arabic_punctuation"]
    + VOCABS["punctuation"]
)
VOCABS["czech"] = VOCABS["english"] + "áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ"
VOCABS["vietnamese"] = (
    VOCABS["english"]
    + "áàảạãăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổộỗơớờởợỡúùủũụưứừửữựiíìỉĩịýỳỷỹỵ"
    + "ÁÀẢẠÃĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÓÒỎÕỌÔỐỒỔỘỖƠỚỜỞỢỠÚÙỦŨỤƯỨỪỬỮỰIÍÌỈĨỊÝỲỶỸỴ"
)
VOCABS["sanskrit_transliterated"] = VOCABS["english"] + VOCABS["sanskrit_transliterated"]
    


VOCABS["sanskrit_diacritics_training"] = VOCABS["english"] + VOCABS["sanskrit_transliterated_refined"]
    #+VOCABS["devanagari"]
     #  +VOCABS["sanskrit_unicode"]

    

#print("\n\n\n")
#print(VOCABS["sanskrit_transliterated"])
#print("\n\n\n")

