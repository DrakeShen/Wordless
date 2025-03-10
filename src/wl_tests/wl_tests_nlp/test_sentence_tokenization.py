# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Wordless: Tests - NLP - Sentence Tokenization
# Copyright (C) 2018-2022  Ye Lei (叶磊)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import pytest

from wl_nlp import wl_sentence_tokenization
from wl_tests import wl_test_init, wl_test_lang_examples
from wl_utils import wl_conversion

main = wl_test_init.Wl_Test_Main()

test_sentence_tokenizers = []

for lang, sentence_tokenizers in main.settings_global['sentence_tokenizers'].items():
    for sentence_tokenizer in sentence_tokenizers:
        if lang not in ['other']:
            test_sentence_tokenizers.append((lang, sentence_tokenizer))

@pytest.mark.parametrize('lang, sentence_tokenizer', test_sentence_tokenizers)
def test_sentence_tokenize(lang, sentence_tokenizer):
    lang_text = wl_conversion.to_lang_text(main, lang)

    print(f'{lang_text} ({lang}) / {sentence_tokenizer}:')

    sentences = wl_sentence_tokenization.wl_sentence_tokenize(
        main,
        text = getattr(wl_test_lang_examples, f'TEXT_{lang.upper()}'),
        lang = lang,
        sentence_tokenizer = sentence_tokenizer)
    sentences_long_text = wl_sentence_tokenization.wl_sentence_tokenize(
        main,
        text = ''.join([f'{i}\n' for i in range(101)]),
        lang = lang,
        sentence_tokenizer = sentence_tokenizer)

    print(sentences)

    if lang not in ['hye', 'guj', 'isl', 'srp_cyrl', 'srp_latn']:
        # The count of sentences should be more than 1
        assert len(sentences) > 1
        # Test long texts
        assert len(sentences_long_text) > 1
        assert sentences_long_text[0] != '100'
        assert sentences_long_text[-1] == '100'

    if lang == 'afr':
        assert sentences == ["Afrikaans is tipologies beskou 'n Indo-Europese, Wes-Germaanse, Nederfrankiese taal,[2] wat aan die suidpunt van Afrika onder invloed van verskeie ander tale en taalgroepe ontstaan het.", "Afrikaans is op 8 Mei 1925 as 'n amptelike taal van Suid-Afrika erken en is tans die derde jongste Germaanse taal wat amptelike status geniet, naas Faroëes wat in 1948 grondwetlik erken is en Luxemburgs wat hierdie status in 1984 verkry het."]
    elif lang == 'sqi':
        assert sentences == ['Gjuha shqipe (ose thjesht shqipja) është gjuhë dhe degë e veçantë e familjes indo-evropiane që flitet nga më shumë se 6 milionë njerëz,[4] kryesisht në Shqipëri, Kosovë dhe Maqedoninë e Veriut, por edhe në zona të tjera të Evropës Juglindore ku ka një popullsi shqiptare, duke përfshirë Malin e Zi dhe Luginën e Preshevës.', 'Është gjuha zyrtare e Shqipërisë dhe Kosovës, si dhe gjuhë bashkë-zyrtare e Maqedonisë së Veriut.']
    elif lang == 'amh':
        assert sentences == ['አማርኛ[1] ፡ የኢትዮጵያ ፡ መደበኛ ፡ ቋንቋ ፡ ነው ።', 'ከሴማዊ ፡ ቋንቋዎች ፡ እንደ ፡ ዕብራይስጥ ፡ ወይም ፡ ዓረብኛ ፡ አንዱ ፡ ነው።', 'በአፍሪካ ፡ ውስጥ ፡ ደግሞ ፡ ከምዕራብ ፡ አፍሪካው ፡ ሐውሳና ፡ ከምሥራቅ ፡ አፍሪካው ፡ ስዋሂሊ ፡ ቀጥሎ ፡ 3ኛውን ፡ ቦታ ፡ የያዘ ፡ ነው።[1] እንዲያውም ፡ 85.6 ፡ ሚሊዮን ፡ ያህል ፡ ተናጋሪዎች ፡ እያሉት ፣ አማርኛ ፡ ከአረብኛ ፡ ቀጥሎ ፡ ትልቁ ፡ ሴማዊ ፡ ቋንቋ ፡ ነው።', 'የሚጻፈውም ፡ በአማርኛ ፡ ፊደል ፡ ነው።', 'አማርኛ ፡ ከዓረብኛና ፡ ከዕብራይስጥ ፡ ያለው ፡ መሰረታዊ ፡ ልዩነት ፡ እንደ ፡ ላቲን ፡ ከግራ ፡ ወደ ፡ ቀኝ ፡ መጻፉ ፡ ነው።']
    elif lang == 'ara':
        assert sentences == ['اللُّغَة العَرَبِيّة هي أكثر اللغات السامية تحدثاً وإحدى أكثر اللغات انتشاراً في العالم، يتحدثها أكثر من 467 مليون نسمة،(1) ويتوزع متحدثوها في الوطن العربي، بالإضافة إلى العديد من المناطق الأخرى المجاورة كالأهواز وتركيا وتشاد ومالي والسنغال وإرتيريا وإثيوبيا وجنوب السودان وإيران.', 'وبذلك فهي تحتل المركز الرابع أو الخامس من حيث اللغات الأكثر انتشاراً في العالم، واللغة الرابعة من حيث عدد المستخدمين على الإنترنت.', 'اللغةُ العربيةُ ذات أهمية قصوى لدى المسلمين، فهي عندَهم لغةٌ مقدسة إذ أنها لغة القرآن، وهي لغةُ الصلاة وأساسيةٌ في القيام بالعديد من العبادات والشعائرِ الإسلامية.', 'العربيةُ هي أيضاً لغة شعائرية رئيسية لدى عدد من الكنائس المسيحية في الوطن العربي، كما كُتبَت بها كثير من أهمِّ الأعمال الدينية والفكرية اليهودية في العصور الوسطى.', 'ارتفعتْ مكانةُ اللغةِ العربية إثْرَ انتشارِ الإسلام بين الدول إذ أصبحت لغة السياسة والعلم والأدب لقرون طويلة في الأراضي التي حكمها المسلمون.', 'وللغة العربية تأثير مباشر وغير مباشر على كثير من اللغات الأخرى في العالم الإسلامي، كالتركية والفارسية والأمازيغية والكردية والأردية والماليزية والإندونيسية والألبانية وبعض اللغات الإفريقية الأخرى مثل الهاوسا والسواحيلية والتجرية والأمهرية والصومالية، وبعض اللغات الأوروبية وخاصةً المتوسطية كالإسبانية والبرتغالية والمالطية والصقلية؛ ودخلت الكثير من مصطلحاتها في اللغة الإنجليزية واللغات الأخرى، مثل أدميرال والتعريفة والكحول والجبر وأسماء النجوم.', 'كما أنها تُدرَّس بشكل رسمي أو غير رسمي في الدول الإسلامية والدول الإفريقية المحاذية للوطن العربي.']
    elif lang == 'hye':
        assert sentences == ['Հայոց լեզվով ստեղծվել է մեծ գրականություն։ Գրաբարով է ավանդված հայ հին պատմագրությունը, գիտափիլիսոփայական, մաթեմատիկական, բժշկագիտական, աստվածաբանական-դավանաբանական գրականությունը։ Միջին գրական հայերենով են մեզ հասել միջնադարյան հայ քնարերգության գլուխգործոցները, բժշկագիտական, իրավագիտական նշանակալի աշխատություններ։ Գրական նոր հայերենի արևելահայերեն ու արևմտահայերեն գրական տարբերակներով ստեղծվել է գեղարվեստական, հրապարակախոսական ու գիտական բազմատիպ ու բազմաբնույթ հարուստ գրականություն։']
    elif lang == 'aze':
        assert sentences == ['Azərbaycan dili[1][2][3] — Azərbaycan Respublikasının və Rusiya Federasiyasının Dağıstan Respublikasının[4] rəsmi dövlət dilidir.', 'Altay dilləri ailəsinin türk dilləri şöbəsinin Oğuz sinfinin Qərb qrupuna daxildir.']
    elif lang == 'eus':
        assert sentences == ['Euskara Euskal Herriko hizkuntza da.[5] Hizkuntza bakartua da, ez baitzaio ahaidetasunik aurkitu.', 'Morfologiari dagokionez, hizkuntza eranskari eta ergatiboa da.', 'Euskaraz mintzo direnei euskaldun deritze.', 'Gaur egun, Euskal Herrian bertan ere hizkuntza gutxitua da, lurralde horretan gaztelania eta frantsesa nagusitu baitira.']
    elif lang == 'ben':
        assert sentences == ['বাংলা ভাষা (বাঙলা, বাঙ্গলা, তথা বাঙ্গালা নামগুলোতেও পরিচিত) একটি ইন্দো-আর্য ভাষা, যা দক্ষিণ এশিয়ার বাঙালি জাতির প্রধান কথ্য ও লেখ্য ভাষা।', 'মাতৃভাষীর সংখ্যায় বাংলা ইন্দো-ইউরোপীয় ভাষা পরিবারের পঞ্চম[১০] ও মোট ব্যবহারকারীর সংখ্যা অনুসারে বাংলা বিশ্বের ষষ্ঠ বৃহত্তম ভাষা।[১১][১২] বাংলা সার্বভৌম ভাষাভিত্তিক জাতিরাষ্ট্র বাংলাদেশের একমাত্র রাষ্ট্রভাষা তথা সরকারি ভাষা[১৩] এবং ভারতের পশ্চিমবঙ্গ, ত্রিপুরা, আসামের বরাক উপত্যকার সরকারি ভাষা।', 'বঙ্গোপসাগরে অবস্থিত আন্দামান দ্বীপপুঞ্জের প্রধান কথ্য ভাষা বাংলা।', 'এছাড়া ভারতের ঝাড়খণ্ড, বিহার, মেঘালয়, মিজোরাম, উড়িষ্যা রাজ্যগুলোতে উল্লেখযোগ্য পরিমাণে বাংলাভাষী জনগণ রয়েছে।', 'ভারতে হিন্দির পরেই সর্বাধিক প্রচলিত ভাষা বাংলা।[১৪][১৫] এছাড়াও মধ্য প্রাচ্য, আমেরিকা ও ইউরোপে উল্লেখযোগ্য পরিমাণে বাংলাভাষী অভিবাসী রয়েছে।[১৬] সারা বিশ্বে সব মিলিয়ে ২৬ কোটির অধিক লোক দৈনন্দিন জীবনে বাংলা ব্যবহার করে।[২] বাংলাদেশের জাতীয় সঙ্গীত এবং ভারতের জাতীয় সঙ্গীত ও স্তোত্র বাংলাতে রচিত।']
    elif lang == 'bul':
        assert sentences == ['Бъ̀лгарският езѝк е индоевропейски език от групата на южнославянските езици, като образува неговата източна подгрупа.', 'Той е официалният език на Република България и един от 24-те официални езика на Европейския съюз.', 'Българският език е плурицентричен език – има няколко книжовни норми.', 'Наред с използваната в България основна норма, съществуват още македонска норма, която също използва кирилица, и банатска норма, която използва латиница.']
    elif lang == 'cat':
        assert sentences == ["El català (denominació oficial a Catalunya, a les Illes Balears, a Andorra, a la ciutat de l'Alguer i tradicional a Catalunya Nord) o valencià (denominació oficial al País Valencià i tradicional al Carxe) és una llengua romànica parlada a Catalunya, el País Valencià (tret d'algunes comarques i localitats de l'interior), les Illes Balears, Andorra, la Franja de Ponent (a l'Aragó), la ciutat de l'Alguer (a l'illa de Sardenya), la Catalunya del Nord,[8] el Carxe (un petit territori de Múrcia poblat per immigrats valencians),[9][10] i en comunitats arreu del món (entre les quals destaca la de l'Argentina, amb 198.000 parlants).[11] Té deu milions de parlants, dels quals quasi la meitat ho són de llengua materna; el seu domini lingüístic, amb una superfície de 68.730 km² i 13.529.127 d'habitants (2009),[12] inclou 1.687 termes municipals.", "Com a llengua materna, és parlada per quatre milions de persones (29% de la població del territori lingüístic), de les quals 2.263.000 a Catalunya,[13] 1.521.000 al País Valencià[14] i 417.000 a les Illes Balears.[15] Com les altres llengües romàniques, el català prové del llatí vulgar que parlaven els romans que s'establiren a Hispània durant l'edat antiga."]
    elif lang == 'zho_cn':
        if sentence_tokenizer == 'spacy_sentence_recognizer':
            assert sentences == ['汉语，又称中文[3]、唐话[4]、华语[5]，指整个汉语族或者其语族里的一种语言。', '汉语族为分析语的一支家族，属汉藏语系。', '汉语如视为单一语言，为世界使用人数最多的语言，目前世界有五分之一人口做为母语。', '其有多种分支，当中官话最为流行，其衍生而来的现代标准汉语，为中华人民共和国的普通话、以及中华民国的国语。', '此外，汉语还是联合国正式语文[6][3]，并被上海合作组织等国际组织采用为官方语言。', '汉语在以其做为母语的地方会有不同的通称，例如在台湾[7]、香港[8]及澳门[9]通称为“中文”，在马来西亚及新加坡通称为“华语”等（由此衍生华语的定义问题）', '[注 1]。']
        elif sentence_tokenizer == 'wordless_zho':
            assert sentences == ['汉语，又称中文[3]、唐话[4]、华语[5]，指整个汉语族或者其语族里的一种语言。', '汉语族为分析语的一支家族，属汉藏语系。', '汉语如视为单一语言，为世界使用人数最多的语言，目前世界有五分之一人口做为母语。', '其有多种分支，当中官话最为流行，其衍生而来的现代标准汉语，为中华人民共和国的普通话、以及中华民国的国语。', '此外，汉语还是联合国正式语文[6][3]，并被上海合作组织等国际组织采用为官方语言。', '汉语在以其做为母语的地方会有不同的通称，例如在台湾[7]、香港[8]及澳门[9]通称为“中文”，在马来西亚及新加坡通称为“华语”等（由此衍生华语的定义问题）[注 1]。']
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'zho_tw':
        assert sentences == ['漢語，又稱中文[3]、唐話[4]、華語[5]，指整個漢語族或者其語族里的一種語言。', '漢語族為分析語的一支家族，屬漢藏語系。', '漢語如視為單一語言，為世界使用人數最多的語言，目前世界有五分之一人口做為母語。', '其有多種分支，當中官話最為流行，其衍生而來的現代標準漢語，為中華人民共和國的普通話、以及中華民國的國語。', '此外，漢語還是聯合國正式語文[6][3]，並被上海合作組織等國際組織採用為官方語言。', '漢語在以其做為母語的地方會有不同的通稱，例如在臺灣[7]、香港[8]及澳門[9]通稱為「中文」，在馬來西亞及新加坡通稱為「華語」等（由此衍生華語的定義問題）[註 1]。']
    elif lang == 'hrv':
        assert sentences == ['Hrvatski jezik (ISO 639-3: hrv) skupni je naziv za nacionalni standardni jezik Hrvata, te za skup narječja i govora kojima govore ili su nekada govorili Hrvati.', 'Njime govori više od 5,5 milijuna ljudi, poglavito Hrvata u Hrvatskoj (3,980.000; popis iz 2001.)', 'i Bosni i Hercegovini (469.000; 2004.).[2] Hrvatski je materinski jezik za Hrvate u drugim zemljama; Sjedinjenim Američkim Državama (58.400; popis iz 2000.)[1]; Austriji, 19.400 (popis iz 2001.);', 'Srbiji 19.223 popis 2011.;', 'Mađarskoj, (14.300; popis iz 2001.);', 'Italiji (3.500; Vincent 1987.);', 'Crnoj Gori (6.810; 2006.);', 'Slovačkoj, 890; popis iz 2001.).']
    elif lang == 'ces':
        if sentence_tokenizer == 'nltk_punkt':
            assert sentences == ['Čeština neboli český jazyk je západoslovanský jazyk, nejbližší slovenštině, poté lužické srbštině a polštině.', 'Patří mezi slovanské jazyky, do rodiny jazyků indoevropských.', 'Čeština se vyvinula ze západních nářečí praslovanštiny na konci 10. století.', 'Je částečně ovlivněná latinou a němčinou.', 'Česky psaná literatura se objevuje od 14. století.', 'První písemné památky jsou však již z 12. století.']
        elif sentence_tokenizer == 'spacy_sentencizer':
            assert sentences == ['Čeština neboli český jazyk je západoslovanský jazyk, nejbližší slovenštině, poté lužické srbštině a polštině.', 'Patří mezi slovanské jazyky, do rodiny jazyků indoevropských.', 'Čeština se vyvinula ze západních nářečí praslovanštiny na konci 10.', 'století.', 'Je částečně ovlivněná latinou a němčinou.', 'Česky psaná literatura se objevuje od 14.', 'století.', 'První písemné památky jsou však již z 12.', 'století.']
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'dan':
        assert sentences == ['Dansk er et nordgermansk sprog af den østnordiske (kontinentale) gruppe, der tales af ca. seks millioner mennesker.', 'Det er stærkt påvirket af plattysk.', 'Foruden Danmark tales dansk også i Sydslesvig (i Flensborg ca. 20 %) samt på Færøerne og Grønland [1].', 'Dansk er tæt forbundet med norsk.', 'Både dansk, norsk og svensk er skandinaviske sprog og minder meget om hinanden.']
    elif lang == 'nld':
        assert sentences == ['Het Nederlands is een West-Germaanse taal en de officiële taal van Nederland, Suriname en een van de drie officiële talen van België.', 'Binnen het Koninkrijk der Nederlanden is het Nederlands ook een officiële taal van Aruba, Curaçao en Sint-Maarten.', 'Het Nederlands is de derde meest gesproken Germaanse taal.']
    elif lang in ['eng_gb', 'eng_us']:
        if sentence_tokenizer == 'nltk_punkt':
            assert sentences == ['English is a West Germanic language of the Indo-European language family, originally spoken by the inhabitants of early medieval England.', '[3][4][5] It is named after the Angles, one of the ancient Germanic peoples that migrated from Anglia, a peninsula on the Baltic Sea (not to be confused with East Anglia), to the area of Great Britain later named after them: England.', 'Living languages most closely related to English include Scots, followed by the Low Saxon and Frisian languages.', 'While English is geneaologically a Germanic language, its vocabulary has been hugely influenced by Old Norman French and Latin, as well as by Old Norse (a North Germanic language).', '[6][7][8]']
        elif sentence_tokenizer == 'spacy_sentence_recognizer':
            assert sentences == ['English is a West Germanic language of the Indo-European language family, originally spoken by the inhabitants of early medieval England.[3][4][5] It is named after the Angles, one of the ancient Germanic peoples that migrated from Anglia, a peninsula on the Baltic Sea (not to be confused with East Anglia), to the area of Great Britain later named after them: England.', 'Living languages most closely related to English include Scots, followed by the Low Saxon and Frisian languages.', 'While English is geneaologically a Germanic language, its vocabulary has been hugely influenced by Old Norman French and Latin, as well as by Old Norse (a North Germanic language).[6][7][8]']
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'est':
        if sentence_tokenizer == 'nltk_punkt':
            assert sentences == ['2012. aasta seisuga kõneles eesti keelt emakeelena hinnanguliselt 922 000 inimest Eestis ja 160 000 mujal maailmas.', 'Võõrkeelena kõneles 2012. aasta seisuga eesti keelt 168 000 inimest.', '[1]']
        elif sentence_tokenizer == 'spacy_sentencizer':
            assert sentences == ['2012.', 'aasta seisuga kõneles eesti keelt emakeelena hinnanguliselt 922 000 inimest Eestis ja 160 000 mujal maailmas.', 'Võõrkeelena kõneles 2012.', 'aasta seisuga eesti keelt 168 000 inimest.[1]']
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'fin':
        assert sentences == ['Suomen kieli (suomi) on uralilaisten kielten itämerensuomalaiseen ryhmään kuuluva kieli.', 'Sitä puhuu äidinkielenään Suomessa 4,8 miljoonaa ja toisena kielenä 0,5 miljoonaa henkilöä.', 'Suurimmat suomea puhuvat vähemmistöt ovat Ruotsissa, Norjassa ja Venäjällä.']
    elif lang == 'fra':
        assert sentences == ["Le français est parlé, en 2018, sur tous les continents par environ 300 millions de personnes5,2 : 235 millions l'emploient quotidiennement, et 90 millions3 en sont des locuteurs natifs.", "En 2018, 80 millions d'élèves et étudiants s'instruisent en français dans le monde6.", "Selon l'Organisation internationale de la francophonie, il pourrait y avoir 700 millions de francophones sur Terre en 20507."]
    elif lang in ['deu_at', 'deu_de', 'deu_ch']:
        if sentence_tokenizer == 'nltk_punkt':
            assert sentences == ['Das Deutsche ist eine plurizentrische Sprache, enthält also mehrere Standardvarietäten in verschiedenen Regionen.', 'Ihr Sprachgebiet umfasst Deutschland, Österreich, die Deutschschweiz, Liechtenstein, Luxemburg, Ostbelgien, Südtirol, das Elsass und Lothringen sowie Nordschleswig.', 'Außerdem ist Deutsch eine Minderheitensprache in einigen europäischen und außereuropäischen Ländern, z.', 'B. in Rumänien und Südafrika sowie Nationalsprache im afrikanischen Namibia.', 'Deutsch ist die meistgesprochene Muttersprache in der Europäischen Union (EU).', '[27]']
        elif sentence_tokenizer == 'spacy_sentence_recognizer':
            assert sentences == ['Das Deutsche ist eine plurizentrische Sprache, enthält also mehrere Standardvarietäten in verschiedenen Regionen.', 'Ihr Sprachgebiet umfasst Deutschland, Österreich, die Deutschschweiz, Liechtenstein, Luxemburg, Ostbelgien, Südtirol, das Elsass und Lothringen sowie Nordschleswig.', 'Außerdem ist Deutsch eine Minderheitensprache in einigen europäischen und außereuropäischen Ländern, z. B. in Rumänien und Südafrika sowie Nationalsprache im afrikanischen Namibia.', 'Deutsch ist die meistgesprochene Muttersprache in der Europäischen Union (EU).[27]']
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'grc':
        assert sentences == ["Ὅτι μὲν ὑμεῖς, ὦ ἄνδρες Ἀθηναῖοι, πεπόνθατε ὑπὸ τῶν ἐμῶν κατηγόρων, οὐκ οἶδα· ἐγὼ δ' οὖν καὶ αὐτὸς ὑπ' αὐτῶν ὀλίγου ἐμαυτοῦ ἐπελαθόμην, οὕτω πιθανῶς ἔλεγον.", 'Καίτοι ἀληθές γε ὡς ἔπος εἰπεῖν οὐδὲν εἰρήκασιν.']
    elif lang == 'ell':
        if sentence_tokenizer == 'nltk_punkt':
            assert sentences == ['Η ελληνική γλώσσα ανήκει στην ινδοευρωπαϊκή οικογένεια[10] και αποτελεί το μοναδικό μέλος του ελληνικού κλάδου, ενώ είναι η επίσημη γλώσσα της Ελλάδος και της Κύπρου.', 'Ανήκει επίσης στον βαλκανικό γλωσσικό δεσμό.', 'Στην ελληνική γλώσσα, έχουμε γραπτά κείμενα ήδη από τον 15ο αιώνα π.Χ.. Σαν Παγκόσμια Ημέρα Ελληνικής Γλώσσας έχει καθιερωθεί η 9η Φεβρουαρίου.']
        elif sentence_tokenizer == 'spacy_sentence_recognizer':
            assert sentences == ['Η ελληνική γλώσσα ανήκει στην ινδοευρωπαϊκή οικογένεια[10] και αποτελεί το μοναδικό μέλος του ελληνικού κλάδου, ενώ είναι η επίσημη γλώσσα της Ελλάδος και της Κύπρου.', 'Ανήκει επίσης στον βαλκανικό γλωσσικό δεσμό.', 'Στην ελληνική γλώσσα, έχουμε γραπτά κείμενα ήδη από τον 15ο αιώνα π.', 'Χ..', 'Σαν Παγκόσμια Ημέρα Ελληνικής Γλώσσας έχει καθιερωθεί η 9η Φεβρουαρίου.']
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'guj':
        assert sentences == ['ગુજરાતી \u200d(/ɡʊdʒəˈrɑːti/[૭], રોમન લિપિમાં: Gujarātī, ઉચ્ચાર: [ɡudʒəˈɾɑːtiː]) ભારત દેશના ગુજરાત રાજ્યની ઇન્ડો-આર્યન ભાષા છે, અને મુખ્યત્વે ગુજરાતી લોકો દ્વારા બોલાય છે. તે બૃહદ ઇન્ડો-યુરોપિયન ભાષા કુટુંબનો ભાગ છે. ગુજરાતીનો ઉદ્ભવ જૂની ગુજરાતી ભાષા (આશરે ઇ.સ. ૧૧૦૦-૧૫૦૦)માંથી થયો છે. તે ગુજરાત રાજ્ય અને દીવ, દમણ અને દાદરા-નગર હવેલી કેન્દ્રશાસિત પ્રદેશોની અધિકૃત ભાષા છે.']
    elif lang == 'heb':
        assert sentences == ['עִבְרִית היא שפה שמית, ממשפחת השפות האפרו-אסיאתיות, הידועה כשפתם של היהודים ושל השומרונים.', 'העברית היא שפתה הרשמית של מדינת ישראל, מעמד שעוגן בשנת תשע"ח, 2018, בחוק יסוד: ישראל – מדינת הלאום של העם היהודי.']
    elif lang == 'hin':
        assert sentences == ['हिन्दी जिसके मानकीकृत रूप को मानक हिंदी कहा जाता है, विश्व की एक प्रमुख भाषा है एवं भारत की एक राजभाषा है।', 'केन्द्रीय स्तर पर भारत में सह-आधिकारिक भाषा अंग्रेजी है।', 'यह हिन्दुस्तानी भाषा की एक मानकीकृत रूप है जिसमें संस्कृत के तत्सम तथा तद्भव शब्दों का प्रयोग अधिक है और अरबी-फ़ारसी शब्द कम हैं।', 'हिन्दी संवैधानिक रूप से भारत की राजभाषा और भारत की सबसे अधिक बोली और समझी जाने वाली भाषा है।', 'हिन्दी भारत की राष्ट्रभाषा नहीं है क्योंकि भारत के संविधान में किसी भी भाषा को ऐसा दर्जा नहीं दिया गया है।[4][5] एथनोलॉग के अनुसार हिन्दी विश्व की तीसरी सबसे अधिक बोली जाने वाली भाषा है।[6] विश्व आर्थिक मंच की गणना के अनुसार यह विश्व की दस शक्तिशाली भाषाओं में से एक है।[7]']
    elif lang == 'hun':
        assert sentences == ['A magyar nyelv az uráli nyelvcsalád tagja, a finnugor nyelvek közé tartozó ugor nyelvek egyike.', 'Legközelebbi rokonai a manysi és a hanti nyelv, majd utánuk az udmurt, a komi, a mari és a mordvin nyelvek.', 'Vannak olyan vélemények, melyek szerint a moldvai csángó önálló nyelv – különösen annak északi, középkori változata –, így ez volna a magyar legközelebbi rokonnyelve.[1]']
    elif lang == 'isl':
        if sentence_tokenizer == 'spacy_sentencizer':
            assert sentences == ['Íslenska er vesturnorrænt, germanskt og indóevrópskt tungumál sem er einkum talað og ritað á Íslandi og er móðurmál langflestra Íslendinga.[5] Það hefur tekið minni breytingum frá fornnorrænu en önnur norræn mál[5] og er skyldara norsku og færeysku en sænsku og dönsku.[2][3]']
        elif sentence_tokenizer == 'tokenizer_isl':
            assert sentences == ['Íslenska er vesturnorrænt, germanskt og indóevrópskt tungumál sem er einkum talað og ritað á Íslandi og er móðurmál langflestra Íslendinga.', '[5] Það hefur tekið minni breytingum frá fornnorrænu en önnur norræn mál [5] og er skyldara norsku og færeysku en sænsku og dönsku.', '[2] [3]']
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'ind':
        assert sentences == ['Bahasa Indonesia adalah bahasa resmi Republik Indonesia dan bahasa persatuan bangsa Indonesia.[8][9] Bahasa Indonesia adalah salah satu dari banyak varietas bahasa Melayu.[10] Bahasa Indonesia diresmikan penggunaannya setelah Proklamasi Kemerdekaan Indonesia, tepatnya sehari sesudahnya, bersamaan dengan mulai berlakunya konstitusi.', 'Di Timor Leste, bahasa Indonesia berstatus sebagai bahasa kerja.']
    elif lang == 'gle':
        assert sentences == ['Is ceann de na teangacha Ceilteacha í Gaeilge (nó Gaeilge na hÉireann mar a thugtar uirthi corruair), agus ceann den dtrí cinn de theangacha Ceilteacha ar a dtugtar na teangacha Gaelacha (Gaeilge,Gaeilge na hAlban agus Gaeilge Mhanann) go háirithe.', 'Labhraítear in Éirinn go príomha í, ach tá cainteoirí Gaeilge ina gcónaí in áiteanna eile ar fud an domhain.']
    elif lang == 'ita':
        if sentence_tokenizer == 'nltk_punkt':
            assert sentences == ['È classificato al 27º posto tra le lingue per numero di parlanti nel mondo e, in Italia, è utilizzato da circa 58 milioni di residenti.', "[2] Nel 2015 l'italiano era la lingua materna del 90,4% dei residenti in Italia,[3] che spesso lo acquisiscono e lo usano insieme alle varianti regionali dell'italiano, alle lingue regionali e ai dialetti.", "In Italia viene ampiamente usato per tutti i tipi di comunicazione della vita quotidiana ed è largamente prevalente nei mezzi di comunicazione nazionali, nell'amministrazione pubblica dello Stato italiano e nell'editoria."]
        elif sentence_tokenizer == 'spacy_sentence_recognizer':
            assert sentences == ["È classificato al 27º posto tra le lingue per numero di parlanti nel mondo e, in Italia, è utilizzato da circa 58 milioni di residenti.[2] Nel 2015 l'italiano era la lingua materna del 90,4% dei residenti in Italia,[3] che spesso lo acquisiscono e lo usano insieme alle varianti regionali dell'italiano, alle lingue regionali e ai dialetti.", "In Italia viene ampiamente usato per tutti i tipi di comunicazione della vita quotidiana ed è largamente prevalente nei mezzi di comunicazione nazionali, nell'amministrazione pubblica dello Stato italiano e nell'editoria."]
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'jpn':
        assert sentences == ['日本語（にほんご、にっぽんご[注 2]、英: Japanese）は、日本国内や、かつての日本領だった国、そして日本人同士の間で使用されている言語。', '日本は法令によって公用語を規定していないが、法令その他の公用文は全て日本語で記述され、各種法令[10]において日本語を用いることが規定され、学校教育においては「国語」の教科として学習を行う等、事実上、日本国内において唯一の公用語となっている。']
    elif lang == 'kan':
        assert sentences == ['ದ್ರಾವಿಡ ಭಾಷೆಗಳಲ್ಲಿ ಪ್ರಾಮುಖ್ಯವುಳ್ಳ ಭಾಷೆಯೂ ಭಾರತದ ಪುರಾತನವಾದ ಭಾಷೆಗಳಲ್ಲಿ ಒಂದೂ ಆಗಿರುವ ಕನ್ನಡ ಭಾಷೆಯನ್ನು ಅದರ ವಿವಿಧ ರೂಪಗಳಲ್ಲಿ ಸುಮಾರು ೪೫ ದಶಲಕ್ಷ (೪.', '೫ ಕೋಟಿ) ಜನರು ಆಡು ನುಡಿಯಾಗಿ ಬಳಸುತ್ತಲಿದ್ದಾರೆ.', 'ಕನ್ನಡ ಕರ್ನಾಟಕ ರಾಜ್ಯದ ಆಡಳಿತ ಭಾಷೆ.[೧೧] ಜಗತ್ತಿನಲ್ಲಿ ಅತ್ಯಂತ ಹೆಚ್ಚು ಮಂದಿ ಮಾತನಾಡುವ ಭಾಷೆಯೆಂಬ ನೆಲೆಯಲ್ಲಿ ಇಪ್ಪತೊಂಬತ್ತನೆಯ ಸ್ಥಾನ ಕನ್ನಡಕ್ಕಿದೆ.', '೨೦೧೧ರ ಜನಗಣತಿಯ ಪ್ರಕಾರ ಜಗತ್ತಿನಲ್ಲಿ ೬.', '೪ ಕೋಟಿ ಜನರು ಕನ್ನಡ ಮಾತನಾಡುತ್ತಾರೆ ಎಂದು ತಿಳಿದುಬಂದಿದೆ.', 'ಇವರಲ್ಲಿ ೫.', '೫ ಕೋಟಿ ಜನರ ಮಾತೃಭಾಷೆ ಕನ್ನಡವಾಗಿದೆ.', 'ಬ್ರಾಹ್ಮಿ ಲಿಪಿಯಿಂದ ರೂಪುಗೊಂಡ ಕನ್ನಡ ಲಿಪಿಯನ್ನು ಉಪಯೋಗಿಸಿ ಕನ್ನಡ ಭಾಷೆಯನ್ನು ಬರೆಯಲಾಗುತ್ತದೆ.', 'ಕನ್ನಡ ಬರಹದ ಮಾದರಿಗಳಿಗೆ ಸಾವಿರದ ಐನೂರು ವರುಷಗಳ ಚರಿತ್ರೆಯಿದೆ.', 'ಕ್ರಿ.', 'ಶ.', 'ಆರನೆಯ ಶತಮಾನದ ಪಶ್ಚಿಮ ಗಂಗ ಸಾಮ್ರಾಜ್ಯದ ಕಾಲದಲ್ಲಿ [೧೨] ಮತ್ತು ಒಂಬತ್ತನೆಯ ಶತಮಾನದ ರಾಷ್ಟ್ರಕೂಟ ಸಾಮ್ರಾಜ್ಯದ ಕಾಲದಲ್ಲಿ ಹಳಗನ್ನಡ ಸಾಹಿತ್ಯ ಅತ್ಯಂತ ಹೆಚ್ಚಿನ ರಾಜಾಶ್ರಯ ಪಡೆಯಿತು.[೧೩][೧೪] ಅದಲ್ಲದೆ ಸಾವಿರ ವರುಷಗಳ ಸಾಹಿತ್ಯ ಪರಂಪರೆ ಕನ್ನಡಕ್ಕಿದೆ.[೧೫]ವಿನೋಬಾ ಭಾವೆ ಕನ್ನಡ ಲಿಪಿಯನ್ನು ಲಿಪಿಗಳ ರಾಣಿಯೆಂದು ಹೊಗಳಿದ್ದಾರೆ.[ಸೂಕ್ತ ಉಲ್ಲೇಖನ ಬೇಕು]']
    elif lang == 'kir':
        assert sentences == ['Кыргыз тили — Кыргыз Республикасынын мамлекеттик тили, түрк тилдеринин курамына, анын ичинде кыргыз-кыпчак тобуна кирет.', 'Кыргыз Республикасынын түптүү калкынын, Кытайдагы, Өзбекстан, Тажикстан, Республикасында Ооганстан, Түркия, Орусияда жашап жаткан кыргыздардын эне тили.', '2009 ж. өткөн элди жана турак-жай фондун каттоонун жыйынтыгында Кыргыз Республикасында кыргыз тилин 3 830 556 адам өз эне тили катары көрсөтүшкөн жана 271 187 адам кыргыз тилин экинчи тил катары биле тургандыгы аныкталган[1].', 'Бул КРсындагы калктын 76% кыргыз тилинде сүйлөйт дегенди билдирет.', 'Кыргыз тилинде 1 720 693 адам орус тилин дагы билише тургандыгын көргөзүшкөн[2].', 'Бул 2 109 863 адам кыргыз тилинде гана сүйлөй билишет дегенди билдирет.', 'Болжолдуу эсеп менен дүйнө жүзү боюнча кыргыз тилинде 6 700 000 адам сүйлөйт.']
    elif lang == 'lav':
        assert sentences == ['Latviešu valoda ir dzimtā valoda apmēram 1,7 miljoniem cilvēku, galvenokārt Latvijā, kur tā ir vienīgā valsts valoda.[3] Lielākās latviešu valodas pratēju kopienas ārpus Latvijas ir Apvienotajā Karalistē, ASV, Īrijā, Austrālijā, Vācijā, Zviedrijā, Kanādā, Brazīlijā, Krievijas Federācijā.', 'Latviešu valoda pieder pie indoeiropiešu valodu saimes baltu valodu grupas.', 'Senākie rakstu paraugi latviešu valodā — jau no 15.', 'gadsimta — ir atrodami Jāņa ģildes alus nesēju biedrības grāmatās.', 'Tajā lielākoties bija latvieši, un no 1517.', 'gada arī brālības vecākie bija latvieši.', 'Pirmais teksts latviski iespiests 1507.', 'gadā izdotajā baznīcas rokasgrāmatā „AGENDA”.[4]']
    elif lang == 'lij':
        assert sentences == ["O baxin d'influensa di dialetti lìguri o l'é de çirca 2 milioìn de personn-e anche se, specialmente inti ùrtimi çinquant'anni, pe coscì de variante locali se son pèrse e de âtre son a reizego tutt'òua, anche pe córpa da mancansa de 'n pâ de generaçioin inta continoasion da parlâ.", "Coscî, ancheu, a popolaçion ch'a conosce a léngoa a l'é ben ben infeiô e ancón meno son quelli che a pàrlan e a scrîvan."]
    elif lang == 'lit':
        assert sentences == ['Lietuvių kalba – iš baltų prokalbės kilusi lietuvių tautos kalba, kuri Lietuvoje yra valstybinė, o Europos Sąjungoje – viena iš oficialiųjų kalbų.', 'Lietuviškai kalba apie tris milijonus žmonių (dauguma jų gyvena Lietuvoje).', 'Drauge su latvių, mirusiomis prūsų, jotvingių ir kitomis baltų kalbomis, priklauso indoeuropiečių kalbų šeimos baltų kalbų grupei.']
    elif lang == 'ltz':
        assert sentences == ["D'Lëtzebuergesch gëtt an der däitscher Dialektologie als ee westgermaneschen, mëtteldäitschen Dialekt aklasséiert, deen zum Muselfränkesche gehéiert.", 'An der Linguistik gëtt et och alt zu de sougenannten "Ausbausproochen", respektiv "Kultursproochen", gezielt.']
    elif lang == 'mkd':
        assert sentences == ['Македонски јазик — јужнословенски јазик, дел од групата на словенски јазици од јазичното семејство на индоевропски јазици.', 'Македонскиот е службен и национален јазик во Македонија, а воедно е и официјално признат како регионален службен јазик во', 'Горица и Пустец во Албанија каде што живее бројно македонско население, но и во Србија како официјален во општините Јабука и Пландиште, Романија и Косово.', 'Македонски се зборува и во Австралија, Бугарија, Грција, Канада, САД, Црна Гора, Турција, во некои земји−членки на Европската Унија и останатата македонска дијаспора.', 'Вкупниот број на македонски говорници е тешко да се утврди поради несоодветни пописи, но бројката се движи од околу 2,5 до 3 милиони луѓе.']
    elif lang == 'mal':
        assert sentences == ['ഇന്ത്യയിൽ പ്രധാനമായും കേരള സംസ്ഥാനത്തിലും ലക്ഷദ്വീപിലും പുതുച്ചേരിയുടെ ഭാഗമായ മയ്യഴിയിലും സംസാരിക്കപ്പെടുന്ന ഭാഷയാണ് മലയാളം. ഇതു ദ്രാവിഡ ഭാഷാ കുടുംബത്തിൽപ്പെടുന്നു. ഇന്ത്യയിൽ ശ്രേഷ്ഠഭാഷാ പദവി ലഭിക്കുന്ന അഞ്ചാമത്തെ ഭാഷയാണ് മലയാളം[3].', '2013 മേയ് 23-നു ചേർന്ന കേന്ദ്രമന്ത്രിസഭായോഗമാണ് മലയാളത്തെ ശ്രേഷ്ഠഭാഷയായി അംഗീകരിച്ചത് ഇന്ത്യൻ ഭരണഘടനയിലെ എട്ടാം ഷെഡ്യൂളിൽ ഉൾപ്പെടുത്തിയിരിക്കുന്ന ഇന്ത്യയിലെ ഇരുപത്തിരണ്ട് ഔദ്യോഗിക ഭാഷകളിൽ ഒന്നാണ് മലയാളം[4].', 'മലയാള ഭാഷ കൈരളി, മലനാട്ട് ഭാഷ എന്നും അറിയപ്പെടുന്നു. കേരള സംസ്ഥാനത്തിലെ ഭരണഭാഷയും കൂടിയാണ്\u200c മലയാളം. കേരളത്തിനും ലക്ഷദ്വീപിനും പുറമേ തമിഴ്നാട്ടിലെ ചില ഭാഗങ്ങളിലും കന്യാകുമാരി ജില്ല, നീലഗിരി ജില്ല കർണാടകയുടെ ദക്ഷിണ കന്നഡ ജില്ല, കൊടഗ് ഭാഗങ്ങളിലും ഗൾഫ് രാജ്യങ്ങൾ, സിംഗപ്പൂർ, മലേഷ്യ എന്നിവിടങ്ങളിലെ കേരളീയ പൈതൃകമുള്ള അനേകം ജനങ്ങളും മലയാളം ഉപയോഗിച്ചുപോരുന്നു. ദേശീയ ഭാഷയായി ഉൾപ്പെടുത്തിയത് മറ്റ് 21 ഭാഷകളുടേതു പോലെ തനതായ വ്യക്തിത്വം ഉള്ളതിനാലാണ്. മലയാള ഭാഷയുടെ ഉല്പത്തിയും പ്രാചീനതയും സംബന്ധിച്ച കാര്യങ്ങൾ ഇന്നും അവ്യക്തമാണ്. പഴയ തമിഴ് (കൊടുംതമിഴ്) ആണ് മലയാളത്തിന്റെ ആദ്യ രൂപം എന്നു കരുതുന്നു. യു. എ. ഇ.-യിലെ നാല് ഔദ്യോഗിക ഭാഷകളിൽ ഒന്നു മലയാളമാണ്.[അവലംബം ആവശ്യമാണ്]']
    elif lang == 'mar':
        assert sentences == ['मराठी भाषा ही इंडो-युरोपीय भाषाकुळातील एक भाषा आहे.', 'मराठी ही भारताच्या २२ अधिकृत भाषांपैकी एक आहे.', 'मराठी महाराष्ट्र राज्याची अधिकृत तर गोवा राज्याची सहअधिकृत भाषा आहे.', '२०११ च्या जनगणनेनुसार, भारत देशात मराठी भाषकांची एकूण लोकसंख्या सुमारे ९ कोटी आहे.', 'मराठी मातृभाषा असणाऱ्या लोकांच्या संख्येनुसार मराठी ही जगातील दहावी व भारतातील तिसरी भाषा आहे.', 'मराठी भाषा भारताच्या प्राचीन भाषांपैकी एक असून महाराष्ट्री प्राकृतचे आधुनिक रूप आहे.', 'मराठी भाषेचा गौरव ज्ञानेश्वरांनी त्यांच्या साहित्यातून ही केलेला दिसून येतो.', 'महाराष्ट्र हे मराठी भाषिकांचे राज्य म्हणून त्याला वेगळे महत्त्व प्राप्त झालेले आहे.', 'आजतागायत मराठी भाषेतून अनेक श्रेष्ठ साहित्यकृती निर्माण झालेल्या आहेत आणि त्यात सातत्यपूर्ण रीतीने भर पडत आहे.[१]']
    elif lang == 'nep':
        assert sentences == ['नेपाली भाषा नेपालको सम्पर्क भाषा तथा भारत, भुटान र म्यानमारको केही भागमा मातृभाषाको रूपमा बोलिने भाषा हो।', 'यो भाषा भारोपेली भाषा परिवार समूहमा पर्दछ।', 'यो भाषा नेपाल र भारतको आधिकारिक (सरकारी कामकाजको) भाषा पनि हो।[५] खासगरि सन् १९९० पछि लाखौं संख्यामा नेपालीहरू आप्रवासीका रूपमा विदेशिन थालेपछि अस्ट्रेलिया, बेलायत, अमेरिका, क्यानडा, युरोपेली सङ्घ र खाडी मुलुकहरूमा नेपाली भाषीहरू छरिएका छन्।', 'नेपालका करिब आधा जनसङ्ख्याले आफ्नो मातृभाषाको रूपमा यो भाषा बोल्ने गर्दछन्।', 'देवनागरी लिपिमा लेखिने यो भाषामा २ किसिमका वर्णमाला छन्।', 'स्वरवर्णमा १२ र व्यञ्जनवर्णमा ३६ वटा वर्णहरू रहेका छन्।[६]']
    elif lang == 'nob':
        if sentence_tokenizer == 'nltk_punkt':
            assert sentences == ['Bokmål er en varietet av norsk skriftspråk.', 'Bokmål er en av to offisielle målformer av norsk skriftspråk, hvorav den andre er nynorsk.', 'I skrift benyttes bokmål av anslagsvis 90 % av befolkningen i Norge.', '[1][2] Etter skriftreformene av riksmål i 1987 og bokmål i 1981 og 2005 er det lite som skiller bokmål og riksmål i alminnelig bruk.']
        elif sentence_tokenizer == 'spacy_sentence_recognizer':
            assert sentences == ['Bokmål er en varietet av norsk skriftspråk.', 'Bokmål er en av to offisielle målformer av norsk skriftspråk, hvorav den andre er nynorsk.', 'I skrift benyttes bokmål av anslagsvis 90 % av befolkningen i Norge.[1][2]', 'Etter skriftreformene av riksmål i 1987 og bokmål i 1981 og 2005 er det lite som skiller bokmål og riksmål i alminnelig bruk.']
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'nno':
        assert sentences == ['Nynorsk, før 1929 offisielt kalla landsmål, er sidan jamstillingsvedtaket av 12. mai 1885 ei av dei to offisielle målformene av norsk; den andre forma er bokmål.', 'Nynorsk blir i dag nytta av om lag 10–15% av innbyggjarane[1][2] i Noreg.', 'Skriftspråket er basert på nynorsk talemål, det vil seie dei moderne norske dialektane til skilnad frå gamalnorsk og mellomnorsk.', 'Når ein seier at nokon snakkar nynorsk, meiner ein helst at dei snakkar nynorsk normaltalemål.', 'Dei færraste dialekttalande nordmenn seier at dei snakkar nynorsk, men det er ikkje uvanleg i kjerneområda til nynorsken.', 'Dette tilhøvet mellom tale og skrift ligg bak målrørsla sitt slagord sidan 1970-talet: «Snakk dialekt – skriv nynorsk!» Nynorske dialektar blir snakka over heile landet, men det er berre på Vestlandet utanom dei største byene og i dei austlandske fjellbygdene at skriftspråket står sterkt.', 'Det vil seie at dei fleste dialekttalarane har bokmål som det primære skriftspråket sitt.']
    elif lang == 'fas':
        assert sentences == ['فارسی یا پارسی یک زبان ایرانی غربی از زیرگروه ایرانی شاخه هندوایرانی خانواده زبان\u200cهای هندواروپایی است که بیشتر در کشورهای ایران، افغانستان، تاجیکستان و ازبکستان گفتگو می\u200cشود.', 'فارسی یک زبان چندکانونی و زبان رسمی ایران و تاجیکستان و افغانستان به\u200cشمار می\u200cرود.', 'این زبان در ایران و افغانستان به الفبای فارسی، که از خط عربی ریشه گرفته، و در تاجیکستان و ازبکستان به الفبای تاجیکی، که از سیریلیک آمده، نوشته می\u200cشود.', 'زبان فارسی در افغانستان به\u200cطور رسمی دری (از ۱۳۴۳ خورشیدی) و در تاجیکستان تاجیکی (از دوره شوروی) خوانده می\u200cشود.']
    elif lang == 'pol':
        assert sentences == ['Język polski, polszczyzna – język lechicki z grupy zachodniosłowiańskiej (do której należą również czeski, kaszubski, słowacki i języki łużyckie), stanowiącej część rodziny indoeuropejskiej.', 'Jest językiem urzędowym w Polsce oraz należy do oficjalnych języków Unii Europejskiej.', 'Ocenia się, że jest mową ojczystą ok. 44 mln ludzi na świecie[1] (w literaturze naukowej można spotkać szacunki od 39[2][3] do 48 mln[4]).', 'Językiem tym posługują się przede wszystkim mieszkańcy Polski oraz przedstawiciele tak zwanej Polonii, czyli ludność polska zamieszkała za granicą.']
    elif lang in ['por_br', 'por_pt']:
        if sentence_tokenizer == 'nltk_punkt':
            assert sentences == ['A língua portuguesa, também designada português, é uma língua românica flexiva ocidental originada no galego-português falado no Reino da Galiza e no norte de Portugal.', 'Com a criação do Reino de Portugal em 1139 e a expansão para o sul na sequência da Reconquista, deu-se a difusão da língua pelas terras conquistadas e mais tarde, com as descobertas portuguesas, para o Brasil, África e outras partes do mundo.', '[3] O português foi usado, naquela época, não somente nas cidades conquistadas pelos portugueses, mas também por muitos governantes locais nos seus contatos com outros estrangeiros poderosos.', 'Especialmente nessa altura a língua portuguesa também influenciou várias línguas.', '[4]']
        elif sentence_tokenizer == 'spacy_sentence_recognizer':
            assert sentences == ['A língua portuguesa, também designada português, é uma língua românica flexiva ocidental originada no galego-português falado no Reino da Galiza e no norte de Portugal.', 'Com a criação do Reino de Portugal em 1139 e a expansão para o sul na sequência da Reconquista, deu-se a difusão da língua pelas terras conquistadas e mais tarde, com as descobertas portuguesas, para o Brasil, África e outras partes do mundo.[3]', 'O português foi usado, naquela época, não somente nas cidades conquistadas pelos portugueses, mas também por muitos governantes locais nos seus contatos com outros estrangeiros poderosos.', 'Especialmente nessa altura a língua portuguesa também influenciou várias línguas.[4]']
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'ron':
        assert sentences == ['Limba română este o limbă indo-europeană, din grupul italic și din subgrupul oriental al limbilor romanice.', 'Printre limbile romanice, româna este a cincea după numărul de vorbitori, în urma spaniolei, portughezei, francezei și italienei.', 'Din motive de diferențiere tipologică, limba română mai este numită în lingvistica comparată limba dacoromână sau dialectul dacoromân.', 'De asemenea, este înregistrată ca limbă de stat atât în România cât și în Republica Moldova, unde circa 75% din populație o consideră limbă maternă (inclusiv sub denumirea de „limba moldovenească”).']
    elif lang == 'rus':
        assert sentences == ['Ру́сский язы́к ([ˈruskʲɪi̯ jɪˈzɨk] Информация о файле слушать)[~ 3][⇨] — язык восточнославянской группы славянской ветви индоевропейской языковой семьи, национальный язык русского народа.', 'Является одним из наиболее распространённых языков мира — шестым среди всех языков мира по общей численности говорящих и восьмым по численности владеющих им как родным[9].', 'Русский является также самым распространённым славянским языком[10] и самым распространённым языком в Европе — географически и по числу носителей языка как родного[7].']
    elif lang == 'san':
        assert sentences == ['संस्कृतम् (IPA: [ˈsɐ̃skr̩tɐm] ( शृणु)) जगतः एकतमा अतिप्राचीना समृद्धा शास्त्रीया च भाषा वर्तते।', 'संस्कृतं भारतस्य जगत: वा भाषासु एकतमा\u200c प्राचीनतमा।', 'भारती, सुरभारती, अमरभारती, अमरवाणी, सुरवाणी, गीर्वाणवाणी, गीर्वाणी, देववाणी, देवभाषा, संस्कृतावाक्, दैवीवाक्, इत्यादिभिः नामभिः एतद्भाषा प्रसिद्धा।']
    elif lang == 'sin':
        assert sentences == ['ශ්\u200dරී ලංකාවේ ප්\u200dරධාන ජාතිය වන සිංහල ජනයාගේ මව් බස සිංහල වෙයි.', 'අද වන විට මිලියන 20 කට අධික සිංහල සහ මිලියන 3කට අධික සිංහල නොවන ජනගහනයක් සිංහල භාෂාව භාවිත කරති.', 'සිංහල\u200d ඉන්දු-යුරෝපීය භාෂාවල උප ගණයක් වන ඉන්දු-ආර්ය භාෂා ගණයට අයිති වන අතර මාල දිවයින භාවිත කරන දිවෙහි භාෂාව සිංහලයෙන් පැවත එන්නකි.', 'සිංහල ශ්\u200dරී ලංකාවේ නිල භාෂාවයි .']
    elif lang == 'srp_cyrl':
        assert sentences == ['Српски језик је званичан у Србији, Босни и Херцеговини и Црној Гори и говори га око 12 милиона људи.[13] Такође је мањински језик у државама централне и источне Европе.[13]']
    elif lang == 'srp_latn':
        assert sentences == ['Srpski jezik je zvaničan u Srbiji, Bosni i Hercegovini i Crnoj Gori i govori ga oko 12 miliona ljudi.[13] Takođe je manjinski jezik u državama centralne i istočne Evrope.[13]']
    elif lang == 'slk':
        assert sentences == ['ešte Bulharsko, Francúzsko, Nemecko, Belgicko, Škandinávia, Taliansko, Švajčiarsko, Holandsko, Cyprus, Rusko, Izrael, JAR, Argentína, Brazília, Uruguaj, Austrália, Nový Zéland, Spojené kráľovstvo a v ďalších krajinách.', 'Celkový odhadovaný počet osôb slovenského pôvodu v zahraničí roku 2001 je 2 016 000.']
    elif lang == 'slv':
        assert sentences == ['Slovenščina [slovénščina] / [sloˈʋenʃtʃina] je združeni naziv za uradni knjižni jezik Slovencev in skupno ime za narečja in govore, ki jih govorijo ali so jih nekoč govorili Slovenci.', 'Govori ga okoli 2,5 (dva in pol) milijona govorcev po svetu, od katerih jih večina živi v Sloveniji.', 'Glede na število govorcev ima razmeroma veliko narečij.', 'Slovenščina je zahodni južnoslovanski jezik in eden redkih indoevropskih jezikov, ki je ohranil dvojino.', 'Za zapisovanje slovenskega jezika se danes uporablja gajica, pisava imenovana po Ljudevitu Gaju, ki jo je priredil po češkem črkopisu.', 'Slovenska gajica se imenuje slovenica.', 'Pišemo jo od marčne revolucije 1848.', 'Do takrat smo uporabljali bohoričico.']
    elif lang == 'spa':
        assert sentences == ['El español o castellano es una lengua romance procedente del latín hablado, perteneciente a la familia de lenguas indoeuropeas.', 'Pertenece al grupo ibérico y es originaria de Castilla, reino medieval de la península ibérica.', 'Se conoce también informalmente como «castilla»,n.', '1\u200b32\u200b33\u200b en algunas áreas rurales e indígenas de América,34\u200b pues el español se empezó a enseñar poco después de la incorporación de los nuevos territorios a la Corona de Castilla.35\u200b36\u200b37\u200b38\u200b39\u200b40\u200b']
    elif lang == 'swe':
        assert sentences == ['Svenska (svenska\u2009(info)) är ett östnordiskt språk som talas av ungefär tio miljoner personer främst i Sverige där språket har en dominant ställning som huvudspråk, men även som det ena nationalspråket i Finland och som enda officiella språk på Åland.', 'I övriga Finland talas det som modersmål framförallt i de finlandssvenska kustområdena i Österbotten, Åboland och Nyland.', 'En liten minoritet svenskspråkiga finns även i Estland.', 'Svenska är nära besläktat och i hög grad ömsesidigt begripligt med danska och norska.', 'De andra nordiska språken, isländska och färöiska, är mindre ömsesidigt begripliga med svenska.', 'Liksom de övriga nordiska språken härstammar svenskan från en gren av fornnordiska, vilket var det språk som talades av de germanska folken i Skandinavien.']
    elif lang == 'tgl':
        assert sentences == ['Ang wikang Tagalog[1] (Baybayin: ᜏᜒᜃᜆᜄᜎᜓ), o ang Tagalog, ay isa sa mga pinakaginagamit na wika ng Pilipinas.', 'Ito ang nangingibabaw na katutubong wika sa mga lalawigan ng ika-4 na rehiyon ng Pilipinas (CALABARZON at MIMAROPA), sa Bulacan, Nueva Ecija at Kalakhang Maynila.']
    elif lang == 'tam':
        assert sentences == ['தமிழ் மொழி (Tamil language) தமிழர்களினதும், தமிழ் பேசும் பலரதும் தாய்மொழி ஆகும்.', 'தமிழ் திராவிட மொழிக் குடும்பத்தின் முதன்மையான மொழிகளில் ஒன்றும் செம்மொழியும் ஆகும்.', 'இந்தியா, இலங்கை, மலேசியா, சிங்கப்பூர் ஆகிய நாடுகளில் அதிக அளவிலும், ஐக்கிய அரபு அமீரகம், தென்னாப்பிரிக்கா, மொரிசியசு, பிசி, இரீயூனியன், திரினிடாடு போன்ற நாடுகளில் சிறிய அளவிலும் தமிழ் பேசப்படுகிறது.', '1997-ஆம் ஆண்டுப் புள்ளி விவரப்படி உலகம் முழுவதிலும் 8 கோடி (80 மில்லியன்) மக்களால் பேசப்படும் தமிழ்[13], ஒரு மொழியைத் தாய்மொழியாகக் கொண்டு பேசும் மக்களின் எண்ணிக்கை அடிப்படையில் பதினெட்டாவது இடத்தில் உள்ளது.[14] இணையத்தில் அதிகம் பயன்படுத்தப்படும் இந்திய மொழிகளில் தமிழ் முதன்மையாக உள்ளதாக 2017ஆம் ஆண்டு நடைபெற்ற கூகுள் கணக்கெடுப்பில் தெரிய வந்தது.[15]']
    elif lang == 'tat':
        assert sentences == ['Татар теле — татарларның милли теле, Татарстанның дәүләт теле, таралышы буенча Россиядә икенче тел.', 'Төрки телләрнең кыпчак төркеменә керә.', 'ЮНЕСКО игълан иткән 14 иң коммуникатив тел исемлегенә керә.[3]']
    elif lang == 'tel':
        assert sentences == ['తెలుగు అనేది ద్రావిడ భాషల కుటుంబానికి చెందిన భాష.', 'దీనిని మాట్లాడే ప్రజలు ప్రధానంగా ఆంధ్ర ప్రదేశ్, తెలంగాణా లో వున్నారు.', 'ఇది ఆ రాష్ట్రాలలో అధికార భాష.', 'భారత రాష్ట్రాలలో, ఒకటి కంటే ఎక్కువ ప్రాధమిక అధికారిక భాషా హోదా కలిగిన కొద్ది భాషలలో హిందీ, బెంగాలీలతో పాటు ఇది కూడా ఉంది. [', '5] [6] పుదుచ్చేరిలోని యానం జిల్లాలో తెలుగు అధికారిక భాష.', 'ఒడిశా, కర్ణాటక, తమిళనాడు, కేరళ, పంజాబ్, ఛత్తీస్\u200cగఢ్, మహారాష్ట్ర, అండమాన్ మరియు నికోబార్ దీవులలో గుర్తింపబడిన అల్పసంఖ్యాక భాష.', 'దేశ ప్రభుత్వం భారతదేశ ప్రాచీన భాషగా గుర్తించిన ఆరు భాషలలో ఇది ఒకటి. [', '7] [8]']
    elif lang == 'tha':
        assert sentences == ['ภาษาไทย หรือ ภาษาไทยกลาง เป็นภาษาราชการและภาษาประจำชาติของประเทศไทย', 'ภาษาไทยเป็นภาษาในกลุ่มภาษาไทซึ่งเป็นกลุ่มย่อยของตระกูลภาษาขร้า-ไท สันนิษฐานว่า ภาษาในตระกูลนี้มีถิ่นกำเนิดจากทางตอนใต้ของประเทศจีน และนักภาษาศาสตร์บางส่วนเสนอว่า ภาษาไทยน่าจะมีความเชื่อมโยงกับตระกูลภาษาออสโตร-เอเชียติก', 'ตระกูลภาษาออสโตรนีเซียน และตระกูลภาษาจีน-ทิเบต']
    elif lang == 'bod':
        assert sentences == ['བོད་ཀྱི་སྐད་ཡིག་ནི་བོད་ཡུལ་དང་ཉེ་འཁོར་གྱི་ས་ཁུལ་བལ་ཡུལ། འབྲུག་དང་འབྲས་ལྗོངས། ལ་དྭགས་ནས་ལྷོ་མོན་རོང་སོགས་སུ་བེད་སྤྱོད་བྱེད་པའི་སྐད་ཡིག་དེ།', 'ད་ཆར་ཡོངས་གྲགས་སུ་བོད་ཀྱི་ཡུལ་གྲུ་སྟོད་སྨད་བར་གསུམ་ལ་ལྟོས་ཏེ་ནང་གསེས་རིགས་གསུམ་དུ་ཕྱེ་བ་སྟེ།', 'སྟོད་དབུས་གཙང་གི་སྐད་དང་། བར་ཁམས་པའི་སྐད་དང་། སྨད་ཨ་མདོའི་སྐད་རྣམས་སོ།', 'བོད་སྐད་ནི་ཧོར་སོག་ལ་སོགས་པ་གྲངས་ཉུང་མི་རིགས་གཞན་པ་ཁག་ཅིག་གིས་བེད་སྤྱོད་གཏོང་བཞིན་ཡོད་པར་མ་ཟད། བལ་ཡུལ་དང་། འབྲས་ལྗོངས། འབྲུག་ཡུལ་། རྒྱ་གར་ཤར་དང་བྱང་རྒྱུད་མངའ་སྡེ་ཁག་གཅིག་བཅས་ཀྱི་རྒྱལ་ཁབ་རྣམས་སུའང་བེད་སྤྱོད་གཏོང་བཞིན་ཡོད།']
    elif lang == 'tir':
        assert sentences == ['ትግርኛ ኣብ ኤርትራን ኣብ ሰሜናዊ ኢትዮጵያን ኣብ ክልል ትግራይ ዝዝረብ ሴማዊ ቋንቋ እዩ።', 'ፊደላት ትግርኛ ካብ ኣደ ትግርኛ ዝዀነት ቋንቋ ግእዝ ዝተዋጽኡ እዮም።']
    elif lang == 'tsn':
        assert sentences == ['Setswana ke teme e e buiwang mo mafatsheng a Aforika Borwa, Botswana, Namibia le Zimbabwe.', 'Ke nngwe ya diteme tsa Bantu tse di welang kaha tlase ga tsa Niger-Congo, sone Setswana mme se wela mo kaleng ya Sotho-Tswana mo kaleng ya Kgaolo S (S.30), mme se sikana thata le diteme tsa Sesotho le Sepedi, gape le diteme tsa Sekgalagadi le Serotse.']
    elif lang == 'tur':
        if sentence_tokenizer == 'nltk_punkt':
            assert sentences == ["Türkçe ya da Türk dili, Güneydoğu Avrupa ve Batı Asya'da konuşulan, Türk dilleri dil ailesine ait sondan eklemeli bir dil.", '[12] Türk dilleri ailesinin Oğuz dilleri grubundan bir Batı Oğuz dili olan Osmanlı Türkçesinin devamını oluşturur.', "Dil, başta Türkiye olmak üzere Balkanlar, Ege Adaları, Kıbrıs ve Orta Doğu'yu kapsayan eski Osmanlı İmparatorluğu coğrafyasında konuşulur.", "[12] Ethnologue'a göre Türkçe, yaklaşık 83 milyon konuşuru ile dünyada en çok konuşulan 20.", 'dildir.', "[13] Türkçe Türkiye, Kıbrıs Cumhuriyeti ve Kuzey Kıbrıs'ta ulusal resmî dil statüsüne sahiptir.", '[12]']
        elif sentence_tokenizer == 'spacy_sentencizer':
            assert sentences == ["Türkçe ya da Türk dili, Güneydoğu Avrupa ve Batı Asya'da konuşulan, Türk dilleri dil ailesine ait sondan eklemeli bir dil.[12] Türk dilleri ailesinin Oğuz dilleri grubundan bir Batı Oğuz dili olan Osmanlı Türkçesinin devamını oluşturur.", "Dil, başta Türkiye olmak üzere Balkanlar, Ege Adaları, Kıbrıs ve Orta Doğu'yu kapsayan eski Osmanlı İmparatorluğu coğrafyasında konuşulur.[12] Ethnologue'a göre Türkçe, yaklaşık 83 milyon konuşuru ile dünyada en çok konuşulan 20. dildir.[13] Türkçe Türkiye, Kıbrıs Cumhuriyeti ve Kuzey Kıbrıs'ta ulusal resmî dil statüsüne sahiptir.[12]"]
        else:
            raise Exception(f'Error: Tests for sentence tokenizer "{sentence_tokenizer}" is skipped!')
    elif lang == 'ukr':
        assert sentences == ['Украї́нська мо́ва (МФА: [ukrɑ̽ˈjɪnʲsʲkɑ̽ ˈmɔwɑ̽], історичні назви — ру́ська, руси́нська[9][10][11][* 2]) — національна мова українців.', "Належить до слов'янської групи індоєвропейської мовної сім'ї[* 3].", 'Є державною мовою в Україні[12].']
    elif lang == 'urd':
        assert sentences == ['اُردُو (یا جدید معیاری اردو) برصغیر کی معیاری زبانوں میں سے ایک ہے۔', 'یہ پاکستان کی قومی اور رابطہ عامہ کی زبان ہے، جبکہ بھارت کی چھے ریاستوں کی دفتری زبان کا درجہ رکھتی ہے۔', 'آئین ہند کے مطابق اسے 22 دفتری شناخت زبانوں میں شامل کیا جاچکا ہے۔', '2001ء کی مردم شماری کے مطابق اردو کو بطور مادری زبان بھارت میں 5.01% فیصد لوگ بولتے ہیں اور اس لحاظ سے یہ بھارت کی چھٹی بڑی زبان ہے جبکہ پاکستان میں اسے بطور مادری زبان 7.59% فیصد لوگ استعمال کرتے ہیں، یہ پاکستان کی پانچویں بڑی زبان ہے۔', 'اردو تاریخی طور پر ہندوستان کی مسلم آبادی سے جڑی ہے۔[حوالہ درکار] بعض ذخیرہ الفاظ کے علاوہ یہ زبان معیاری ہندی سے قابل فہم ہے جو اس خطے کی ہندوؤں سے منسوب ہے۔[حوالہ درکار] زبانِ اردو کو پہچان و ترقی اس وقت ملی جب برطانوی دور میں انگریز حکمرانوں نے اسے فارسی کی بجائے انگریزی کے ساتھ شمالی ہندوستان کے علاقوں اور جموں و کشمیر میں اسے سنہ 1846ء اور پنجاب میں سنہ 1849ء میں بطور دفتری زبان نافذ کیا۔', 'اس کے علاوہ خلیجی، یورپی، ایشیائی اور امریکی علاقوں میں اردو بولنے والوں کی ایک بڑی تعداد آباد ہے جو بنیادی طور پر جنوبی ایشیاء سے کوچ کرنے والے اہلِ اردو ہیں۔', '1999ء کے اعداد وشمار کے مطابق اردو زبان کے مجموعی متکلمین کی تعداد دس کروڑ ساٹھ لاکھ کے لگ بھگ تھی۔', 'اس لحاظ سے یہ دنیا کی نویں بڑی زبان ہے۔']
    elif lang == 'vie':
        assert sentences == ['Tiếng Việt, cũng gọi là tiếng Việt Nam[5] hay Việt ngữ là ngôn ngữ của người Việt và là ngôn ngữ chính thức tại Việt Nam.', 'Đây là tiếng mẹ đẻ của khoảng 85% dân cư Việt Nam cùng với hơn 4 triệu Việt kiều.', 'Tiếng Việt còn là ngôn ngữ thứ hai của các dân tộc thiểu số tại Việt Nam và là ngôn ngữ dân tộc thiểu số tại Cộng hòa Séc.']
    elif lang == 'yor':
        assert sentences == ['Èdè Yorùbá Ni èdè tí ó ṣàkójọ pọ̀ gbogbo kú oótu o-ò-jíire bí, níapá ìwọ̀ Oòrùn ilẹ̀ Nàìjíríà, tí a bá wo èdè Yorùbá, àwọn onímọ̀ pín èdè náà sábẹ́ ẹ̀yà Kwa nínú ẹbí èdè Niger-Congo.', 'Wọ́n tún fìdí rẹ̀ múlẹ̀ pé ẹ̀yà Kwa yìí ló wọ́pọ̀ jùlọ ní sísọ, ní ìwọ̀ oòrùn aláwọ̀ dúdú fún ẹgbẹẹgbẹ̀rún ọdún.', 'Àwọn onímọ̀ èdè kan tilẹ̀ ti fi ìdí ọ̀rọ̀ múlẹ̀ pé láti orírun kan náà ni àwọn èdè bí Yorùbá, Kru, Banle, Twi, Ga, Ewe, Fon, Edo, Nupe, Igbo, Idoma, Efik àti Ijaw ti bẹ̀rẹ̀ sí yapa gẹ́gẹ́ bi èdè ọ̀tọ̀ọ̀tọ̀ tó dúró láti bí ẹgbẹ̀rún mẹ́ta ọ̀dún sẹ́yìn. [', '1] Ọ̀kan pàtàkì lára àwọn èdè orílẹ̀ èdè Nàìjíríà ni èdè Yorùbá.', 'Àwọn ìpínlẹ̀ tí a ti lè rí àwọn olùsọ èdè Yorùbá nílẹ̀ Nàìjíríà ni ìpínlẹ̀ Ẹdó, ìpínlẹ̀ Òndó, ìpínlẹ̀ Ọ̀ṣun, ìpínlẹ̀ Ọ̀yọ́, ìpínlẹ̀ Èkó, àti ìpínlẹ̀ Ògùn.', 'Ẹ̀wẹ̀ a tún rí àwọn orílẹ̀-èdè míràn bí Tógò apá kan ní Gúúsù ilẹ̀ Amẹ́ríkà bí i Cuba, Brasil, Haiti, Ghana, Sierra Leone,United Kingdom àti Trinidad, gbogbo orílẹ̀-èdè tí a dárúkọ wọ̀nyí, yàtọ̀ sí orílẹ̀-èdè Nàìjíríà, òwò ẹrú ni ó gbé àwọn ẹ̀yà Yorùbá dé ibẹ.[2]']
    else:
        raise Exception(f'Error: Tests for language "{lang}" is skipped!')

if __name__ == '__main__':
    for lang, sentence_tokenizer in test_sentence_tokenizers:
        test_sentence_tokenize(lang, sentence_tokenizer)
