# ----------------------------------------------------------------------
# Wordless: Settings - Global Settings
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

from PyQt5.QtCore import QCoreApplication

from wl_measures import (
    wl_measures_adjusted_freq,
    wl_measures_dispersion,
    wl_measures_effect_size,
    wl_measures_statistical_significance
)

_tr = QCoreApplication.translate

def init_settings_global():
    return {
        'langs': {
            _tr('init_settings_global', 'Afrikaans'): ['afr', 'af', 'Indo-European'],
            _tr('init_settings_global', 'Akkadian'): ['akk', 'akk', 'Afro-Asiatic'],
            _tr('init_settings_global', 'Albanian'): ['sqi', 'sq', 'Indo-European'],
            _tr('init_settings_global', 'Amharic'): ['amh', 'am', 'Afro-Asiatic'],
            _tr('init_settings_global', 'Arabic'): ['ara', 'ar', 'Afro-Asiatic'],
            _tr('init_settings_global', 'Arabic (Standard)'): ['arb', 'arb', 'Afro-Asiatic'],
            _tr('init_settings_global', 'Armenian'): ['hye', 'hy', 'Indo-European'],
            _tr('init_settings_global', 'Assamese'): ['asm', 'as', 'Indo-European'],
            _tr('init_settings_global', 'Asturian'): ['ast', 'ast', 'Indo-European'],
            _tr('init_settings_global', 'Azerbaijani'): ['aze', 'az', 'Turkic'],
            _tr('init_settings_global', 'Basque'): ['eus', 'eu', 'Language isolate'],
            _tr('init_settings_global', 'Belarusian'): ['bel', 'be', 'Indo-European'],
            _tr('init_settings_global', 'Bengali'): ['ben', 'bn', 'Indo-European'],
            _tr('init_settings_global', 'Breton'): ['bre', 'br', 'Indo-European'],
            _tr('init_settings_global', 'Bulgarian'): ['bul', 'bg', 'Indo-European'],
            _tr('init_settings_global', 'Catalan'): ['cat', 'ca', 'Indo-European'],
            _tr('init_settings_global', 'Chinese (Simplified)'): ['zho_cn', 'zh_cn', 'Sino-Tibetan'],
            _tr('init_settings_global', 'Chinese (Traditional)'): ['zho_tw', 'zh_tw', 'Sino-Tibetan'],
            _tr('init_settings_global', 'Coptic'): ['cop', 'cop', 'Unclassified'],
            _tr('init_settings_global', 'Croatian'): ['hrv', 'hr', 'Indo-European'],
            _tr('init_settings_global', 'Czech'): ['ces', 'cs', 'Indo-European'],
            _tr('init_settings_global', 'Danish'): ['dan', 'da', 'Indo-European'],
            _tr('init_settings_global', 'Dutch'): ['nld', 'nl', 'Indo-European'],
            _tr('init_settings_global', 'English (Middle)'): ['enm', 'enm', 'Indo-European'],
            _tr('init_settings_global', 'English (Old)'): ['ang', 'ang', 'Indo-European'],
            _tr('init_settings_global', 'English (United Kingdom)'): ['eng_gb', 'en_gb', 'Indo-European'],
            _tr('init_settings_global', 'English (United States)'): ['eng_us', 'en_us', 'Indo-European'],
            _tr('init_settings_global', 'Esperanto'): ['epo', 'eo', 'Constructed'],
            _tr('init_settings_global', 'Estonian'): ['est', 'et', 'Uralic'],
            _tr('init_settings_global', 'Finnish'): ['fin', 'fi', 'Uralic'],
            _tr('init_settings_global', 'French'): ['fra', 'fr', 'Indo-European'],
            _tr('init_settings_global', 'French (Old)'): ['fro', 'fro', 'Indo-European'],
            _tr('init_settings_global', 'Galician'): ['glg', 'gl', 'Indo-European'],
            _tr('init_settings_global', 'German (Austria)'): ['deu_at', 'de_at', 'Indo-European'],
            _tr('init_settings_global', 'German (Germany)'): ['deu_de', 'de_de', 'Indo-European'],
            _tr('init_settings_global', 'German (Middle High)'): ['gmh', 'gmh', 'Unclassified'],
            _tr('init_settings_global', 'German (Switzerland)'): ['deu_ch', 'de_ch', 'Indo-European'],
            _tr('init_settings_global', 'Greek (Ancient)'): ['grc', 'grc', 'Unclassified'],
            _tr('init_settings_global', 'Greek (Modern)'): ['ell', 'el', 'Indo-European'],
            _tr('init_settings_global', 'Gujarati'): ['guj', 'gu', 'Indo-European'],
            _tr('init_settings_global', 'Hausa'): ['hau', 'ha', 'Afro-Asiatic'],
            _tr('init_settings_global', 'Hebrew'): ['heb', 'he', 'Afro-Asiatic'],
            _tr('init_settings_global', 'Hindi'): ['hin', 'hi', 'Indo-European'],
            _tr('init_settings_global', 'Hungarian'): ['hun', 'hu', 'Uralic'],
            _tr('init_settings_global', 'Icelandic'): ['isl', 'is', 'Indo-European'],
            _tr('init_settings_global', 'Indonesian'): ['ind', 'id', 'Austronesian'],
            _tr('init_settings_global', 'Irish'): ['gle', 'ga', 'Indo-European'],
            _tr('init_settings_global', 'Italian'): ['ita', 'it', 'Indo-European'],
            _tr('init_settings_global', 'Japanese'): ['jpn', 'ja', 'Japonic'],
            _tr('init_settings_global', 'Kannada'): ['kan', 'kn', 'Dravidian'],
            _tr('init_settings_global', 'Kazakh'): ['kaz', 'kk', 'Turkic'],
            _tr('init_settings_global', 'Korean'): ['kor', 'ko', 'Koreanic'],
            _tr('init_settings_global', 'Kurdish'): ['kur', 'ku', 'Indo-European'],
            _tr('init_settings_global', 'Kyrgyz'): ['kir', 'ky', 'Turkic'],
            _tr('init_settings_global', 'Latin'): ['lat', 'la', 'Indo-European'],
            _tr('init_settings_global', 'Latvian'): ['lav', 'lv', 'Indo-European'],
            _tr('init_settings_global', 'Ligurian'): ['lij', 'lij', 'Unclassified'],
            _tr('init_settings_global', 'Lithuanian'): ['lit', 'lt', 'Indo-European'],
            _tr('init_settings_global', 'Luxembourgish'): ['ltz', 'lb', 'Indo-European'],
            _tr('init_settings_global', 'Macedonian'): ['mkd', 'mk', 'Indo-European'],
            _tr('init_settings_global', 'Malay'): ['msa', 'ms', 'Austronesian'],
            _tr('init_settings_global', 'Malayalam'): ['mal', 'ml', 'Dravidian'],
            _tr('init_settings_global', 'Manx'): ['glv', 'gv', 'Indo-European'],
            _tr('init_settings_global', 'Marathi'): ['mar', 'mr', 'Indo-European'],
            _tr('init_settings_global', 'Marathi (Old)'): ['omr', 'omr', 'Unclassified'],
            _tr('init_settings_global', 'Meitei'): ['mni', 'mni', 'Sino-Tibetan'],
            _tr('init_settings_global', 'Mongolian'): ['mon', 'mn', 'Mongolic'],
            _tr('init_settings_global', 'Nepali'): ['nep', 'ne', 'Indo-European'],
            _tr('init_settings_global', 'Norse (Old)'): ['non', 'non', 'Indo-European'],
            _tr('init_settings_global', 'Norwegian Bokmål'): ['nob', 'nb', 'Indo-European'],
            _tr('init_settings_global', 'Norwegian Nynorsk'): ['nno', 'nn', 'Indo-European'],
            _tr('init_settings_global', 'Oriya'): ['ori', 'or', 'Indo-European'],
            _tr('init_settings_global', 'Persian'): ['fas', 'fa', 'Indo-European'],
            _tr('init_settings_global', 'Polish'): ['pol', 'pl', 'Indo-European'],
            _tr('init_settings_global', 'Portuguese (Brazil)'): ['por_br', 'pt_br', 'Indo-European'],
            _tr('init_settings_global', 'Portuguese (Portugal)'): ['por_pt', 'pt_pt', 'Indo-European'],
            _tr('init_settings_global', 'Punjabi'): ['pan', 'pa', 'Indo-European'],
            _tr('init_settings_global', 'Romanian'): ['ron', 'ro', 'Indo-European'],
            _tr('init_settings_global', 'Russian'): ['rus', 'ru', 'Indo-European'],
            _tr('init_settings_global', 'Sanskrit'): ['san', 'sa', 'Indo-European'],
            _tr('init_settings_global', 'Scottish Gaelic'): ['gla', 'gd', 'Indo-European'],
            _tr('init_settings_global', 'Serbian (Cyrillic)'): ['srp_cyrl', 'sr_cyrl', 'Indo-European'],
            _tr('init_settings_global', 'Serbian (Latin)'): ['srp_latn', 'sr_latn', 'Indo-European'],
            _tr('init_settings_global', 'Sinhala'): ['sin', 'si', 'Indo-European'],
            _tr('init_settings_global', 'Slovak'): ['slk', 'sk', 'Indo-European'],
            _tr('init_settings_global', 'Slovenian'): ['slv', 'sl', 'Indo-European'],
            _tr('init_settings_global', 'Somali'): ['som', 'so', 'Afro-Asiatic'],
            _tr('init_settings_global', 'Sotho (Southern)'): ['sot', 'st', 'Niger-Congo'],
            _tr('init_settings_global', 'Spanish'): ['spa', 'es', 'Indo-European'],
            _tr('init_settings_global', 'Swahili'): ['swa', 'sw', 'Niger-Congo'],
            _tr('init_settings_global', 'Swedish'): ['swe', 'sv', 'Indo-European'],
            _tr('init_settings_global', 'Tagalog'): ['tgl', 'tl', 'Austronesian'],
            _tr('init_settings_global', 'Tajik'): ['tgk', 'tg', 'Indo-European'],
            _tr('init_settings_global', 'Tamil'): ['tam', 'ta', 'Dravidian'],
            _tr('init_settings_global', 'Tatar'): ['tat', 'tt', 'Turkic'],
            _tr('init_settings_global', 'Telugu'): ['tel', 'te', 'Dravidian'],
            _tr('init_settings_global', 'Tetun Dili'): ['tdt', 'tdt', 'Unclassified'],
            _tr('init_settings_global', 'Thai'): ['tha', 'th', 'Tai-Kadai'],
            _tr('init_settings_global', 'Tibetan'): ['bod', 'bo', 'Sino-Tibetan'],
            _tr('init_settings_global', 'Tigrinya'): ['tir', 'ti', 'Afro-Asiatic'],
            _tr('init_settings_global', 'Tswana'): ['tsn', 'tn', 'Niger-Congo'],
            _tr('init_settings_global', 'Turkish'): ['tur', 'tr', 'Turkic'],
            _tr('init_settings_global', 'Ukrainian'): ['ukr', 'uk', 'Indo-European'],
            _tr('init_settings_global', 'Urdu'): ['urd', 'ur', 'Indo-European'],
            _tr('init_settings_global', 'Vietnamese'): ['vie', 'vi', 'Austroasiatic'],
            _tr('init_settings_global', 'Welsh'): ['cym', 'cy', 'Indo-European'],
            _tr('init_settings_global', 'Yoruba'): ['yor', 'yo', 'Niger-Congo'],
            _tr('init_settings_global', 'Zulu'): ['zul', 'zu', 'Niger-Congo'],

            _tr('init_settings_global', 'Other Languages'): ['other', 'other', 'Unclassified']
        },

        'encodings': {
            _tr('init_settings_global', 'All Languages (UTF-8 without BOM)'): 'utf_8',
            _tr('init_settings_global', 'All Languages (UTF-8 with BOM)'): 'utf_8_sig',
            _tr('init_settings_global', 'All Languages (UTF-16 with BOM)'): 'utf_16',
            _tr('init_settings_global', 'All Languages (UTF-16BE without BOM)'): 'utf_16_be',
            _tr('init_settings_global', 'All Languages (UTF-16LE without BOM)'): 'utf_16_le',
            _tr('init_settings_global', 'All Languages (UTF-32 with BOM)'): 'utf_32',
            _tr('init_settings_global', 'All Languages (UTF-32BE without BOM)'): 'utf_32_be',
            _tr('init_settings_global', 'All Languages (UTF-32LE without BOM)'): 'utf_32_le',
            _tr('init_settings_global', 'All Languages (UTF-7)'): 'utf_7',

            _tr('init_settings_global', 'Arabic (CP720)'): 'cp720',
            _tr('init_settings_global', 'Arabic (CP864)'): 'cp864',
            _tr('init_settings_global', 'Arabic (ISO-8859-6)'): 'iso8859_6',
            _tr('init_settings_global', 'Arabic (Mac OS Arabic)'): 'mac_arabic',
            _tr('init_settings_global', 'Arabic (Windows-1256)'): 'cp1256',

            _tr('init_settings_global', 'Baltic Languages (CP775)'): 'cp775',
            _tr('init_settings_global', 'Baltic Languages (ISO-8859-13)'): 'iso8859_13',
            _tr('init_settings_global', 'Baltic Languages (Windows-1257)'): 'cp1257',

            _tr('init_settings_global', 'Celtic Languages (ISO-8859-14)'): 'iso8859_14',

            _tr('init_settings_global', 'Chinese (GB18030)'): 'gb18030',
            _tr('init_settings_global', 'Chinese (GBK)'): 'gbk',

            _tr('init_settings_global', 'Chinese (Simplified) (GB2312)'): 'gb2312',
            _tr('init_settings_global', 'Chinese (Simplified) (HZ)'): 'hz_gb_2312',

            _tr('init_settings_global', 'Chinese (Traditional) (Big-5)'): 'big5',
            _tr('init_settings_global', 'Chinese (Traditional) (Big5-HKSCS)'): 'big5hkscs',
            _tr('init_settings_global', 'Chinese (Traditional) (CP950)'): 'cp950',

            _tr('init_settings_global', 'Croatian (Mac OS Croatian)'): 'mac_croatian',

            _tr('init_settings_global', 'Cyrillic (CP855)'): 'cp855',
            _tr('init_settings_global', 'Cyrillic (CP866)'): 'cp866',
            _tr('init_settings_global', 'Cyrillic (ISO-8859-5)'): 'iso8859_5',
            _tr('init_settings_global', 'Cyrillic (Mac OS Cyrillic)'): 'mac_cyrillic',
            _tr('init_settings_global', 'Cyrillic (Windows-1251)'): 'cp1251',

            _tr('init_settings_global', 'English (ASCII)'): 'ascii',
            _tr('init_settings_global', 'English (EBCDIC 037)'): 'cp037',
            _tr('init_settings_global', 'English (CP437)'): 'cp437',

            _tr('init_settings_global', 'European (HP Roman-8)'): 'hp_roman8',

            _tr('init_settings_global', 'European (Central) (CP852)'): 'cp852',
            _tr('init_settings_global', 'European (Central) (ISO-8859-2)'): 'iso8859_2',
            _tr('init_settings_global', 'European (Central) (Mac OS Central European)'): 'mac_latin2',
            _tr('init_settings_global', 'European (Central) (Windows-1250)'): 'cp1250',

            _tr('init_settings_global', 'European (Northern) (ISO-8859-4)'): 'iso8859_4',

            _tr('init_settings_global', 'European (Southern) (ISO-8859-3)'): 'iso8859_3',
            _tr('init_settings_global', 'European (South-Eastern) (ISO-8859-16)'): 'iso8859_16',

            _tr('init_settings_global', 'European (Western) (EBCDIC 500)'): 'cp500',
            _tr('init_settings_global', 'European (Western) (CP850)'): 'cp850',
            _tr('init_settings_global', 'European (Western) (CP858)'): 'cp858',
            _tr('init_settings_global', 'European (Western) (CP1140)'): 'cp1140',
            _tr('init_settings_global', 'European (Western) (ISO-8859-1)'): 'latin_1',
            _tr('init_settings_global', 'European (Western) (ISO-8859-15)'): 'iso8859_15',
            _tr('init_settings_global', 'European (Western) (Mac OS Roman)'): 'mac_roman',
            _tr('init_settings_global', 'European (Western) (Windows-1252)'): 'windows_1252',

            _tr('init_settings_global', 'French (CP863)'): 'cp863',

            _tr('init_settings_global', 'German (EBCDIC 273)'): 'cp273',

            _tr('init_settings_global', 'Greek (CP737)'): 'cp737',
            _tr('init_settings_global', 'Greek (CP869)'): 'cp869',
            _tr('init_settings_global', 'Greek (CP875)'): 'cp875',
            _tr('init_settings_global', 'Greek (ISO-8859-7)'): 'iso8859_7',
            _tr('init_settings_global', 'Greek (Mac OS Greek)'): 'mac_greek',
            _tr('init_settings_global', 'Greek (Windows-1253)'): 'windows_1253',

            _tr('init_settings_global', 'Hebrew (CP856)'): 'cp856',
            _tr('init_settings_global', 'Hebrew (CP862)'): 'cp862',
            _tr('init_settings_global', 'Hebrew (EBCDIC 424)'): 'cp424',
            _tr('init_settings_global', 'Hebrew (ISO-8859-8)'): 'iso8859_8',
            _tr('init_settings_global', 'Hebrew (Windows-1255)'): 'windows_1255',

            _tr('init_settings_global', 'Icelandic (CP861)'): 'cp861',
            _tr('init_settings_global', 'Icelandic (Mac OS Icelandic)'): 'mac_iceland',

            _tr('init_settings_global', 'Japanese (CP932)'): 'cp932',
            _tr('init_settings_global', 'Japanese (EUC-JP)'): 'euc_jp',
            _tr('init_settings_global', 'Japanese (EUC-JIS-2004)'): 'euc_jis_2004',
            _tr('init_settings_global', 'Japanese (EUC-JISx0213)'): 'euc_jisx0213',
            _tr('init_settings_global', 'Japanese (ISO-2022-JP)'): 'iso2022_jp',
            _tr('init_settings_global', 'Japanese (ISO-2022-JP-1)'): 'iso2022_jp_1',
            _tr('init_settings_global', 'Japanese (ISO-2022-JP-2)'): 'iso2022_jp_2',
            _tr('init_settings_global', 'Japanese (ISO-2022-JP-2004)'): 'iso2022_jp_2004',
            _tr('init_settings_global', 'Japanese (ISO-2022-JP-3)'): 'iso2022_jp_3',
            _tr('init_settings_global', 'Japanese (ISO-2022-JP-EXT)'): 'iso2022_jp_ext',
            _tr('init_settings_global', 'Japanese (Shift_JIS)'): 'shift_jis',
            _tr('init_settings_global', 'Japanese (Shift_JIS-2004)'): 'shift_jis_2004',
            _tr('init_settings_global', 'Japanese (Shift_JISx0213)'): 'shift_jisx0213',

            _tr('init_settings_global', 'Kazakh (KZ-1048)'): 'kz1048',
            _tr('init_settings_global', 'Kazakh (PTCP154)'): 'ptcp154',

            _tr('init_settings_global', 'Korean (EUC-KR)'): 'euc_kr',
            _tr('init_settings_global', 'Korean (ISO-2022-KR)'): 'iso2022_kr',
            _tr('init_settings_global', 'Korean (JOHAB)'): 'johab',
            _tr('init_settings_global', 'Korean (UHC)'): 'cp949',

            _tr('init_settings_global', 'Nordic Languages (CP865)'): 'cp865',
            _tr('init_settings_global', 'Nordic Languages (ISO-8859-10)'): 'iso8859_10',

            _tr('init_settings_global', 'Persian/Urdu (Mac OS Farsi)'): 'mac_farsi',

            _tr('init_settings_global', 'Portuguese (CP860)'): 'cp860',

            _tr('init_settings_global', 'Romanian (Mac OS Romanian)'): 'mac_romanian',

            _tr('init_settings_global', 'Russian (KOI8-R)'): 'koi8_r',

            _tr('init_settings_global', 'Tajik (KOI8-T)'): 'koi8_t',

            _tr('init_settings_global', 'Thai (CP874)'): 'cp874',
            _tr('init_settings_global', 'Thai (ISO-8859-11)'): 'iso8859_11',

            _tr('init_settings_global', 'Turkish (CP857)'): 'cp857',
            _tr('init_settings_global', 'Turkish (EBCDIC 1026)'): 'cp1026',
            _tr('init_settings_global', 'Turkish (ISO-8859-9)'): 'iso8859_9',
            _tr('init_settings_global', 'Turkish (Mac OS Turkish)'): 'mac_turkish',
            _tr('init_settings_global', 'Turkish (Windows-1254)'): 'cp1254',

            _tr('init_settings_global', 'Ukrainian (CP1125)'): 'cp1125',
            _tr('init_settings_global', 'Ukrainian (KOI8-U)'): 'koi8_u',

            _tr('init_settings_global', 'Urdu (CP1006)'): 'cp1006',

            _tr('init_settings_global', 'Vietnamese (CP1258)'): 'cp1258',
        },

        'file_types': {
            'files': [
                _tr('init_settings_global', 'CSV File (*.csv)'),
                _tr('init_settings_global', 'Excel Workbook (*.xlsx)'),
                _tr('init_settings_global', 'HTML Page (*.htm; *.html)'),
                _tr('init_settings_global', 'Text File (*.txt)'),
                _tr('init_settings_global', 'Translation Memory File (*.tmx)'),
                _tr('init_settings_global', 'Word Document (*.docx)'),
                _tr('init_settings_global', 'XML File (*.xml)'),
                _tr('init_settings_global', 'All Files (*.*)')
            ],

            'exp_tables': [
                _tr('init_settings_global', 'CSV File (*.csv)'),
                _tr('init_settings_global', 'Excel Workbook (*.xlsx)')
            ],

            'exp_tables_concordancer': [
                _tr('init_settings_global', 'CSV File (*.csv)'),
                _tr('init_settings_global', 'Excel Workbook (*.xlsx)'),
                _tr('init_settings_global', 'Word Document (*.docx)')
            ]
        },

        'lang_util_mappings': {
            'sentence_tokenizers': {
                _tr('init_settings_global', 'botok - Tibetan Sentence Tokenizer'): 'botok_bod',
                _tr('init_settings_global', 'NLTK - Punkt Sentence Tokenizer'): 'nltk_punkt',
                _tr('init_settings_global', 'PyThaiNLP - CRFCut'): 'pythainlp_crfcut',

                _tr('init_settings_global', 'spaCy - Sentence Recognizer'): 'spacy_sentence_recognizer',
                _tr('init_settings_global', 'spaCy - Sentencizer'): 'spacy_sentencizer',

                _tr('init_settings_global', 'Tokenizer - Icelandic Sentence Tokenizer'): 'tokenizer_isl',
                _tr('init_settings_global', 'Underthesea - Vietnamese Sentence Tokenizer'): 'underthesea_vie',

                _tr('init_settings_global', 'Wordless - Chinese Sentence Tokenizer'): 'wordless_zho',
                _tr('init_settings_global', 'Wordless - Japanese Sentence Tokenizer'): 'wordless_jpn'
            },

            'word_tokenizers': {
                _tr('init_settings_global', 'botok - Tibetan Word Tokenizer'): 'botok_bod',
                _tr('init_settings_global', 'jieba - Chinese Word Tokenizer'): 'jieba_zho',
                _tr('init_settings_global', 'nagisa - Japanese Word Tokenizer'): 'nagisa_jpn',

                _tr('init_settings_global', 'NLTK - NIST Tokenizer'): 'nltk_nist',
                _tr('init_settings_global', 'NLTK - NLTK Tokenizer'): 'nltk_nltk',
                _tr('init_settings_global', 'NLTK - Penn Treebank Tokenizer'): 'nltk_penn_treebank',
                _tr('init_settings_global', 'NLTK - Tok-tok Tokenizer'): 'nltk_tok_tok',
                _tr('init_settings_global', 'NLTK - Twitter Tokenizer'): 'nltk_twitter',

                _tr('init_settings_global', 'pkuseg - Chinese Word Tokenizer'): 'pkuseg_zho',

                _tr('init_settings_global', 'PyThaiNLP - Longest Matching'): 'pythainlp_longest_matching',
                _tr('init_settings_global', 'PyThaiNLP - Maximum Matching'): 'pythainlp_max_matching',
                _tr('init_settings_global', 'PyThaiNLP - Maximum Matching + TCC'): 'pythainlp_max_matching_tcc',
                _tr('init_settings_global', 'PyThaiNLP - Maximum Matching + TCC (Safe Mode)'): 'pythainlp_max_matching_tcc_safe_mode',
                _tr('init_settings_global', 'PyThaiNLP - NERCut'): 'pythainlp_nercut',

                _tr('init_settings_global', 'Sacremoses - Moses Tokenizer'): 'sacremoses_moses',

                _tr('init_settings_global', 'spaCy - Afrikaans Word Tokenizer'): 'spacy_afr',
                _tr('init_settings_global', 'spaCy - Albanian Word Tokenizer'): 'spacy_sqi',
                _tr('init_settings_global', 'spaCy - Amharic Word Tokenizer'): 'spacy_amh',
                _tr('init_settings_global', 'spaCy - Arabic Word Tokenizer'): 'spacy_ara',
                _tr('init_settings_global', 'spaCy - Armenian Word Tokenizer'): 'spacy_hye',
                _tr('init_settings_global', 'spaCy - Azerbaijani Word Tokenizer'): 'spacy_aze',
                _tr('init_settings_global', 'spaCy - Basque Word Tokenizer'): 'spacy_eus',
                _tr('init_settings_global', 'spaCy - Bengali Word Tokenizer'): 'spacy_ben',
                _tr('init_settings_global', 'spaCy - Bulgarian Word Tokenizer'): 'spacy_bul',
                _tr('init_settings_global', 'spaCy - Catalan Word Tokenizer'): 'spacy_cat',
                _tr('init_settings_global', 'spaCy - Chinese Word Tokenizer'): 'spacy_zho',
                _tr('init_settings_global', 'spaCy - Croatian Word Tokenizer'): 'spacy_hrv',
                _tr('init_settings_global', 'spaCy - Czech Word Tokenizer'): 'spacy_ces',
                _tr('init_settings_global', 'spaCy - Danish Word Tokenizer'): 'spacy_dan',
                _tr('init_settings_global', 'spaCy - Dutch Word Tokenizer'): 'spacy_nld',
                _tr('init_settings_global', 'spaCy - English Word Tokenizer'): 'spacy_eng',
                _tr('init_settings_global', 'spaCy - Estonian Word Tokenizer'): 'spacy_est',
                _tr('init_settings_global', 'spaCy - Finnish Word Tokenizer'): 'spacy_fin',
                _tr('init_settings_global', 'spaCy - French Word Tokenizer'): 'spacy_fra',
                _tr('init_settings_global', 'spaCy - German Word Tokenizer'): 'spacy_deu',
                _tr('init_settings_global', 'spaCy - Greek (Ancient) Word Tokenizer'): 'spacy_grc',
                _tr('init_settings_global', 'spaCy - Greek (Modern) Word Tokenizer'): 'spacy_ell',
                _tr('init_settings_global', 'spaCy - Gujarati Word Tokenizer'): 'spacy_guj',
                _tr('init_settings_global', 'spaCy - Hebrew Word Tokenizer'): 'spacy_heb',
                _tr('init_settings_global', 'spaCy - Hindi Word Tokenizer'): 'spacy_hin',
                _tr('init_settings_global', 'spaCy - Hungarian Word Tokenizer'): 'spacy_hun',
                _tr('init_settings_global', 'spaCy - Icelandic Word Tokenizer'): 'spacy_isl',
                _tr('init_settings_global', 'spaCy - Indonesian Word Tokenizer'): 'spacy_ind',
                _tr('init_settings_global', 'spaCy - Irish Word Tokenizer'): 'spacy_gle',
                _tr('init_settings_global', 'spaCy - Italian Word Tokenizer'): 'spacy_ita',
                _tr('init_settings_global', 'spaCy - Japanese Word Tokenizer'): 'spacy_jpn',
                _tr('init_settings_global', 'spaCy - Kannada Word Tokenizer'): 'spacy_kan',
                _tr('init_settings_global', 'spaCy - Kyrgyz Word Tokenizer'): 'spacy_kir',
                _tr('init_settings_global', 'spaCy - Latvian Word Tokenizer'): 'spacy_lav',
                _tr('init_settings_global', 'spaCy - Ligurian Word Tokenizer'): 'spacy_lij',
                _tr('init_settings_global', 'spaCy - Lithuanian Word Tokenizer'): 'spacy_lit',
                _tr('init_settings_global', 'spaCy - Luxembourgish Word Tokenizer'): 'spacy_ltz',
                _tr('init_settings_global', 'spaCy - Macedonian Word Tokenizer'): 'spacy_mkd',
                _tr('init_settings_global', 'spaCy - Malayalam Word Tokenizer'): 'spacy_mal',
                _tr('init_settings_global', 'spaCy - Marathi Word Tokenizer'): 'spacy_mar',
                _tr('init_settings_global', 'spaCy - Nepali Word Tokenizer'): 'spacy_nep',
                _tr('init_settings_global', 'spaCy - Norwegian Word Tokenizer'): 'spacy_nob',
                _tr('init_settings_global', 'spaCy - Persian Word Tokenizer'): 'spacy_fas',
                _tr('init_settings_global', 'spaCy - Polish Word Tokenizer'): 'spacy_pol',
                _tr('init_settings_global', 'spaCy - Portuguese Word Tokenizer'): 'spacy_por',
                _tr('init_settings_global', 'spaCy - Romanian Word Tokenizer'): 'spacy_ron',
                _tr('init_settings_global', 'spaCy - Russian Word Tokenizer'): 'spacy_rus',
                _tr('init_settings_global', 'spaCy - Sanskrit Word Tokenizer'): 'spacy_san',
                _tr('init_settings_global', 'spaCy - Serbian Word Tokenizer'): 'spacy_srp',
                _tr('init_settings_global', 'spaCy - Sinhala Word Tokenizer'): 'spacy_sin',
                _tr('init_settings_global', 'spaCy - Slovak Word Tokenizer'): 'spacy_slk',
                _tr('init_settings_global', 'spaCy - Slovenian Word Tokenizer'): 'spacy_slv',
                _tr('init_settings_global', 'spaCy - Spanish Word Tokenizer'): 'spacy_spa',
                _tr('init_settings_global', 'spaCy - Swedish Word Tokenizer'): 'spacy_swe',
                _tr('init_settings_global', 'spaCy - Tagalog Word Tokenizer'): 'spacy_tgl',
                _tr('init_settings_global', 'spaCy - Tamil Word Tokenizer'): 'spacy_tam',
                _tr('init_settings_global', 'spaCy - Tatar Word Tokenizer'): 'spacy_tat',
                _tr('init_settings_global', 'spaCy - Telugu Word Tokenizer'): 'spacy_tel',
                _tr('init_settings_global', 'spaCy - Tigrinya Word Tokenizer'): 'spacy_tir',
                _tr('init_settings_global', 'spaCy - Tswana Word Tokenizer'): 'spacy_tsn',
                _tr('init_settings_global', 'spaCy - Turkish Word Tokenizer'): 'spacy_tur',
                _tr('init_settings_global', 'spaCy - Ukrainian Word Tokenizer'): 'spacy_ukr',
                _tr('init_settings_global', 'spaCy - Urdu Word Tokenizer'): 'spacy_urd',
                _tr('init_settings_global', 'spaCy - Yoruba Word Tokenizer'): 'spacy_yor',

                _tr('init_settings_global', 'SudachiPy - Japanese Word Tokenizer (Split Mode A)'): 'sudachipy_jpn_split_mode_a',
                _tr('init_settings_global', 'SudachiPy - Japanese Word Tokenizer (Split Mode B)'): 'sudachipy_jpn_split_mode_b',
                _tr('init_settings_global', 'SudachiPy - Japanese Word Tokenizer (Split Mode C)'): 'sudachipy_jpn_split_mode_c',

                _tr('init_settings_global', 'Tokenizer - Icelandic Word Tokenizer'): 'tokenizer_isl',
                _tr('init_settings_global', 'Underthesea - Vietnamese Word Tokenizer'): 'underthesea_vie',

                _tr('init_settings_global', 'Wordless - Chinese Character Tokenizer'): 'wordless_zho_char',
                _tr('init_settings_global', 'Wordless - Japanese Kanji Tokenizer'): 'wordless_jpn_kanji'
            },

            'syl_tokenizers': {
                _tr('init_settings_global', 'Pyphen - Afrikaans Syllable Tokenizer'): 'pyphen_afr',
                _tr('init_settings_global', 'Pyphen - Albanian Syllable Tokenizer'): 'pyphen_sqi',
                _tr('init_settings_global', 'Pyphen - Belarusian Syllable Tokenizer'): 'pyphen_bel',
                _tr('init_settings_global', 'Pyphen - Bulgarian Syllable Tokenizer'): 'pyphen_bul',
                _tr('init_settings_global', 'Pyphen - Croatian Syllable Tokenizer'): 'pyphen_hrv',
                _tr('init_settings_global', 'Pyphen - Czech Syllable Tokenizer'): 'pyphen_ces',
                _tr('init_settings_global', 'Pyphen - Danish Syllable Tokenizer'): 'pyphen_dan',
                _tr('init_settings_global', 'Pyphen - Dutch Syllable Tokenizer'): 'pyphen_nld',
                _tr('init_settings_global', 'Pyphen - English (United Kingdom) Syllable Tokenizer'): 'pyphen_eng_gb',
                _tr('init_settings_global', 'Pyphen - English (United States) Syllable Tokenizer'): 'pyphen_eng_us',
                _tr('init_settings_global', 'Pyphen - Esperanto Syllable Tokenizer'): 'pyphen_epo',
                _tr('init_settings_global', 'Pyphen - Estonian Syllable Tokenizer'): 'pyphen_est',
                _tr('init_settings_global', 'Pyphen - French Syllable Tokenizer'): 'pyphen_fra',
                _tr('init_settings_global', 'Pyphen - Galician Syllable Tokenizer'): 'pyphen_glg',
                _tr('init_settings_global', 'Pyphen - German (Austria) Syllable Tokenizer'): 'pyphen_deu_at',
                _tr('init_settings_global', 'Pyphen - German (Germany) Syllable Tokenizer'): 'pyphen_deu_de',
                _tr('init_settings_global', 'Pyphen - German (Switzerland) Syllable Tokenizer'): 'pyphen_deu_ch',
                _tr('init_settings_global', 'Pyphen - Greek (Modern) Syllable Tokenizer'): 'pyphen_ell',
                _tr('init_settings_global', 'Pyphen - Hungarian Syllable Tokenizer'): 'pyphen_hun',
                _tr('init_settings_global', 'Pyphen - Icelandic Syllable Tokenizer'): 'pyphen_isl',
                _tr('init_settings_global', 'Pyphen - Indonesian Syllable Tokenizer'): 'pyphen_ind',
                _tr('init_settings_global', 'Pyphen - Italian Syllable Tokenizer'): 'pyphen_ita',
                _tr('init_settings_global', 'Pyphen - Lithuanian Syllable Tokenizer'): 'pyphen_lit',
                _tr('init_settings_global', 'Pyphen - Latvian Syllable Tokenizer'): 'pyphen_lav',
                _tr('init_settings_global', 'Pyphen - Mongolian Syllable Tokenizer'): 'pyphen_mon',
                _tr('init_settings_global', 'Pyphen - Norwegian Bokmål Syllable Tokenizer'): 'pyphen_nob',
                _tr('init_settings_global', 'Pyphen - Norwegian Nynorsk Syllable Tokenizer'): 'pyphen_nno',
                _tr('init_settings_global', 'Pyphen - Polish Syllable Tokenizer'): 'pyphen_pol',
                _tr('init_settings_global', 'Pyphen - Portuguese (Brazil) Syllable Tokenizer'): 'pyphen_por_br',
                _tr('init_settings_global', 'Pyphen - Portuguese (Portugal) Syllable Tokenizer'): 'pyphen_por_pt',
                _tr('init_settings_global', 'Pyphen - Romanian Syllable Tokenizer'): 'pyphen_ron',
                _tr('init_settings_global', 'Pyphen - Russian Syllable Tokenizer'): 'pyphen_rus',
                _tr('init_settings_global', 'Pyphen - Serbian (Cyrillic) Syllable Tokenizer'): 'pyphen_srp_cyrl',
                _tr('init_settings_global', 'Pyphen - Serbian (Latin) Syllable Tokenizer'): 'pyphen_srp_latn',
                _tr('init_settings_global', 'Pyphen - Slovak Syllable Tokenizer'): 'pyphen_slk',
                _tr('init_settings_global', 'Pyphen - Slovenian Syllable Tokenizer'): 'pyphen_slv',
                _tr('init_settings_global', 'Pyphen - Spanish Syllable Tokenizer'): 'pyphen_spa',
                _tr('init_settings_global', 'Pyphen - Swedish Syllable Tokenizer'): 'pyphen_swe',
                _tr('init_settings_global', 'Pyphen - Telugu Syllable Tokenizer'): 'pyphen_tel',
                _tr('init_settings_global', 'Pyphen - Ukrainian Syllable Tokenizer'): 'pyphen_ukr',
                _tr('init_settings_global', 'Pyphen - Zulu Syllable Tokenizer'): 'pyphen_zul',

                _tr('init_settings_global', 'PyThaiNLP - Thai Syllable Tokenizer'): 'pythainlp_tha',
                _tr('init_settings_global', 'ssg - Thai Syllable Tokenizer'): 'ssg_tha'
            },

            'pos_taggers': {
                _tr('init_settings_global', 'botok - Tibetan POS Tagger'): 'botok_bod',
                _tr('init_settings_global', 'jieba - Chinese POS Tagger'): 'jieba_zho',
                _tr('init_settings_global', 'nagisa - Japanese POS Tagger'): 'nagisa_jpn',
                _tr('init_settings_global', 'NLTK - Perceptron POS Tagger'): 'nltk_perceptron',
                _tr('init_settings_global', 'pymorphy2 - Morphological Analyzer'): 'pymorphy2_morphological_analyzer',

                _tr('init_settings_global', 'PyThaiNLP - Perceptron POS Tagger (LST20)'): 'pythainlp_perceptron_lst20',
                _tr('init_settings_global', 'PyThaiNLP - Perceptron POS Tagger (ORCHID)'): 'pythainlp_perceptron_orchid',
                _tr('init_settings_global', 'PyThaiNLP - Perceptron POS Tagger (PUD)'): 'pythainlp_perceptron_pud',

                _tr('init_settings_global', 'spaCy - Catalan POS Tagger'): 'spacy_cat',
                _tr('init_settings_global', 'spaCy - Chinese POS Tagger'): 'spacy_zho',
                _tr('init_settings_global', 'spaCy - Danish POS Tagger'): 'spacy_dan',
                _tr('init_settings_global', 'spaCy - Dutch POS Tagger'): 'spacy_nld',
                _tr('init_settings_global', 'spaCy - English POS Tagger'): 'spacy_eng',
                _tr('init_settings_global', 'spaCy - French POS Tagger'): 'spacy_fra',
                _tr('init_settings_global', 'spaCy - German POS Tagger'): 'spacy_deu',
                _tr('init_settings_global', 'spaCy - Greek (Modern) POS Tagger'): 'spacy_ell',
                _tr('init_settings_global', 'spaCy - Italian POS Tagger'): 'spacy_ita',
                _tr('init_settings_global', 'spaCy - Japanese POS Tagger'): 'spacy_jpn',
                _tr('init_settings_global', 'spaCy - Lithuanian POS Tagger'): 'spacy_lit',
                _tr('init_settings_global', 'spaCy - Macedonian POS Tagger'): 'spacy_mkd',
                _tr('init_settings_global', 'spaCy - Norwegian Bokmål POS Tagger'): 'spacy_nob',
                _tr('init_settings_global', 'spaCy - Polish POS Tagger'): 'spacy_pol',
                _tr('init_settings_global', 'spaCy - Portuguese POS Tagger'): 'spacy_por',
                _tr('init_settings_global', 'spaCy - Romanian POS Tagger'): 'spacy_ron',
                _tr('init_settings_global', 'spaCy - Russian POS Tagger'): 'spacy_rus',
                _tr('init_settings_global', 'spaCy - Spanish POS Tagger'): 'spacy_spa',

                _tr('init_settings_global', 'SudachiPy - Japanese POS Tagger'): 'sudachipy_jpn',

                _tr('init_settings_global', 'Underthesea - Vietnamese POS Tagger'): 'underthesea_vie'
            },

            'lemmatizers': {
                _tr('init_settings_global', 'botok - Tibetan Lemmatizer'): 'botok_bod',

                _tr('init_settings_global', 'Lemmatization Lists - Asturian Lemma List'): 'lemmatization_lists_ast',
                _tr('init_settings_global', 'Lemmatization Lists - Bulgarian Lemma List'): 'lemmatization_lists_bul',
                _tr('init_settings_global', 'Lemmatization Lists - Catalan Lemma List'): 'lemmatization_lists_cat',
                _tr('init_settings_global', 'Lemmatization Lists - Czech Lemma List'): 'lemmatization_lists_ces',
                _tr('init_settings_global', 'Lemmatization Lists - English Lemma List'): 'lemmatization_lists_eng',
                _tr('init_settings_global', 'Lemmatization Lists - Estonian Lemma List'): 'lemmatization_lists_est',
                _tr('init_settings_global', 'Lemmatization Lists - French Lemma List'): 'lemmatization_lists_fra',
                _tr('init_settings_global', 'Lemmatization Lists - Galician Lemma List'): 'lemmatization_lists_glg',
                _tr('init_settings_global', 'Lemmatization Lists - German Lemma List'): 'lemmatization_lists_deu',
                _tr('init_settings_global', 'Lemmatization Lists - Hungarian Lemma List'): 'lemmatization_lists_hun',
                _tr('init_settings_global', 'Lemmatization Lists - Irish Lemma List'): 'lemmatization_lists_gle',
                _tr('init_settings_global', 'Lemmatization Lists - Italian Lemma List'): 'lemmatization_lists_ita',
                _tr('init_settings_global', 'Lemmatization Lists - Manx Lemma List'): 'lemmatization_lists_glv',
                _tr('init_settings_global', 'Lemmatization Lists - Persian Lemma List'): 'lemmatization_lists_fas',
                _tr('init_settings_global', 'Lemmatization Lists - Portuguese Lemma List'): 'lemmatization_lists_por',
                _tr('init_settings_global', 'Lemmatization Lists - Romanian Lemma List'): 'lemmatization_lists_ron',
                _tr('init_settings_global', 'Lemmatization Lists - Russian Lemma List'): 'lemmatization_lists_rus',
                _tr('init_settings_global', 'Lemmatization Lists - Scottish Gaelic Lemma List'): 'lemmatization_lists_gla',
                _tr('init_settings_global', 'Lemmatization Lists - Slovak Lemma List'): 'lemmatization_lists_slk',
                _tr('init_settings_global', 'Lemmatization Lists - Slovenian Lemma List'): 'lemmatization_lists_slv',
                _tr('init_settings_global', 'Lemmatization Lists - Spanish Lemma List'): 'lemmatization_lists_spa',
                _tr('init_settings_global', 'Lemmatization Lists - Swedish Lemma List'): 'lemmatization_lists_swe',
                _tr('init_settings_global', 'Lemmatization Lists - Ukrainian Lemma List'): 'lemmatization_lists_ukr',
                _tr('init_settings_global', 'Lemmatization Lists - Welsh Lemma List'): 'lemmatization_lists_cym',

                _tr('init_settings_global', 'NLTK - WordNet Lemmatizer'): 'nltk_wordnet',
                _tr('init_settings_global', 'pymorphy2 - Morphological Analyzer'): 'pymorphy2_morphological_analyzer',

                _tr('init_settings_global', 'spaCy - Bengali Lemmatizer'): 'spacy_ben',
                _tr('init_settings_global', 'spaCy - Catalan Lemmatizer'): 'spacy_cat',
                _tr('init_settings_global', 'spaCy - Croatian Lemmatizer'): 'spacy_hrv',
                _tr('init_settings_global', 'spaCy - Czech Lemmatizer'): 'spacy_ces',
                _tr('init_settings_global', 'spaCy - Danish Lemmatizer'): 'spacy_dan',
                _tr('init_settings_global', 'spaCy - Dutch Lemmatizer'): 'spacy_nld',
                _tr('init_settings_global', 'spaCy - English Lemmatizer'): 'spacy_eng',
                _tr('init_settings_global', 'spaCy - French Lemmatizer'): 'spacy_fra',
                _tr('init_settings_global', 'spaCy - German Lemmatizer'): 'spacy_deu',
                _tr('init_settings_global', 'spaCy - Greek (Ancient) Lemmatizer'): 'spacy_grc',
                _tr('init_settings_global', 'spaCy - Greek (Modern) Lemmatizer'): 'spacy_ell',
                _tr('init_settings_global', 'spaCy - Hungarian Lemmatizer'): 'spacy_hun',
                _tr('init_settings_global', 'spaCy - Indonesian Lemmatizer'): 'spacy_ind',
                _tr('init_settings_global', 'spaCy - Irish Lemmatizer'): 'spacy_gle',
                _tr('init_settings_global', 'spaCy - Italian Lemmatizer'): 'spacy_ita',
                _tr('init_settings_global', 'spaCy - Japanese Lemmatizer'): 'spacy_jpn',
                _tr('init_settings_global', 'spaCy - Lithuanian Lemmatizer'): 'spacy_lit',
                _tr('init_settings_global', 'spaCy - Luxembourgish Lemmatizer'): 'spacy_ltz',
                _tr('init_settings_global', 'spaCy - Macedonian Lemmatizer'): 'spacy_mkd',
                _tr('init_settings_global', 'spaCy - Norwegian Bokmål Lemmatizer'): 'spacy_nob',
                _tr('init_settings_global', 'spaCy - Persian Lemmatizer'): 'spacy_fas',
                _tr('init_settings_global', 'spaCy - Polish Lemmatizer'): 'spacy_pol',
                _tr('init_settings_global', 'spaCy - Portuguese Lemmatizer'): 'spacy_por',
                _tr('init_settings_global', 'spaCy - Romanian Lemmatizer'): 'spacy_ron',
                _tr('init_settings_global', 'spaCy - Russian Lemmatizer'): 'spacy_rus',
                _tr('init_settings_global', 'spaCy - Serbian (Cyrillic) Lemmatizer'): 'spacy_srp_cyrl',
                _tr('init_settings_global', 'spaCy - Spanish Lemmatizer'): 'spacy_spa',
                _tr('init_settings_global', 'spaCy - Swedish Lemmatizer'): 'spacy_swe',
                _tr('init_settings_global', 'spaCy - Tagalog Lemmatizer'): 'spacy_tgl',
                _tr('init_settings_global', 'spaCy - Turkish Lemmatizer'): 'spacy_tur',
                _tr('init_settings_global', 'spaCy - Urdu Lemmatizer'): 'spacy_urd',

                _tr('init_settings_global', 'SudachiPy - Japanese Lemmatizer'): 'sudachipy_jpn'
            },

            'stop_word_lists': {
                _tr('init_settings_global', 'Custom List'): 'custom',
                _tr('init_settings_global', 'CLTK - Akkadian Stop Word List'): 'cltk_akk',
                _tr('init_settings_global', 'CLTK - Arabic (Standard) Stop Word List'): 'cltk_arb',
                _tr('init_settings_global', 'CLTK - Coptic Stop Word List'): 'cltk_cop',
                _tr('init_settings_global', 'CLTK - English (Middle) Stop Word List'): 'cltk_enm',
                _tr('init_settings_global', 'CLTK - English (Old) Stop Word List'): 'cltk_ang',
                _tr('init_settings_global', 'CLTK - French (Old) Stop Word List'): 'cltk_fro',
                _tr('init_settings_global', 'CLTK - German (Middle High) Stop Word List'): 'cltk_gmh',
                _tr('init_settings_global', 'CLTK - Greek (Ancient) Stop Word List'): 'cltk_grc',
                _tr('init_settings_global', 'CLTK - Hindi Stop Word List'): 'cltk_hin',
                _tr('init_settings_global', 'CLTK - Latin Stop Word List'): 'cltk_lat',
                _tr('init_settings_global', 'CLTK - Marathi (Old) Stop Word List'): 'cltk_omr',
                _tr('init_settings_global', 'CLTK - Norse (Old) Stop Word List'): 'cltk_non',
                _tr('init_settings_global', 'CLTK - Punjabi Stop Word List'): 'cltk_pan',
                _tr('init_settings_global', 'CLTK - Sanskrit Stop Word List'): 'cltk_san',

                _tr('init_settings_global', 'extra-stopwords - Albanian Stop Word List'): 'extra_stopwords_sqi',
                _tr('init_settings_global', 'extra-stopwords - Arabic Stop Word List'): 'extra_stopwords_ara',
                _tr('init_settings_global', 'extra-stopwords - Armenian Stop Word List'): 'extra_stopwords_hye',
                _tr('init_settings_global', 'extra-stopwords - Basque Stop Word List'): 'extra_stopwords_eus',
                _tr('init_settings_global', 'extra-stopwords - Belarusian Stop Word List'): 'extra_stopwords_bel',
                _tr('init_settings_global', 'extra-stopwords - Bengali Stop Word List'): 'extra_stopwords_ben',
                _tr('init_settings_global', 'extra-stopwords - Bulgarian Stop Word List'): 'extra_stopwords_bul',
                _tr('init_settings_global', 'extra-stopwords - Catalan Stop Word List'): 'extra_stopwords_cat',
                _tr('init_settings_global', 'extra-stopwords - Chinese (Simplified) Stop Word List'): 'extra_stopwords_zho_cn',
                _tr('init_settings_global', 'extra-stopwords - Chinese (Traditional) Stop Word List'): 'extra_stopwords_zho_tw',
                _tr('init_settings_global', 'extra-stopwords - Croatian Stop Word List'): 'extra_stopwords_hrv',
                _tr('init_settings_global', 'extra-stopwords - Czech Stop Word List'): 'extra_stopwords_ces',
                _tr('init_settings_global', 'extra-stopwords - Danish Stop Word List'): 'extra_stopwords_dan',
                _tr('init_settings_global', 'extra-stopwords - Dutch Stop Word List'): 'extra_stopwords_nld',
                _tr('init_settings_global', 'extra-stopwords - English Stop Word List'): 'extra_stopwords_eng',
                _tr('init_settings_global', 'extra-stopwords - Estonian Stop Word List'): 'extra_stopwords_est',
                _tr('init_settings_global', 'extra-stopwords - Finnish Stop Word List'): 'extra_stopwords_fin',
                _tr('init_settings_global', 'extra-stopwords - French Stop Word List'): 'extra_stopwords_fra',
                _tr('init_settings_global', 'extra-stopwords - Galician Stop Word List'): 'extra_stopwords_glg',
                _tr('init_settings_global', 'extra-stopwords - German Stop Word List'): 'extra_stopwords_deu',
                _tr('init_settings_global', 'extra-stopwords - Greek (Modern) Stop Word List'): 'extra_stopwords_ell',
                _tr('init_settings_global', 'extra-stopwords - Hausa Stop Word List'): 'extra_stopwords_hau',
                _tr('init_settings_global', 'extra-stopwords - Hebrew Stop Word List'): 'extra_stopwords_heb',
                _tr('init_settings_global', 'extra-stopwords - Hindi Stop Word List'): 'extra_stopwords_hin',
                _tr('init_settings_global', 'extra-stopwords - Hungarian Stop Word List'): 'extra_stopwords_hun',
                _tr('init_settings_global', 'extra-stopwords - Icelandic Stop Word List'): 'extra_stopwords_isl',
                _tr('init_settings_global', 'extra-stopwords - Indonesian Stop Word List'): 'extra_stopwords_ind',
                _tr('init_settings_global', 'extra-stopwords - Irish Stop Word List'): 'extra_stopwords_gle',
                _tr('init_settings_global', 'extra-stopwords - Italian Stop Word List'): 'extra_stopwords_ita',
                _tr('init_settings_global', 'extra-stopwords - Japanese Stop Word List'): 'extra_stopwords_jpn',
                _tr('init_settings_global', 'extra-stopwords - Korean Stop Word List'): 'extra_stopwords_kor',
                _tr('init_settings_global', 'extra-stopwords - Kurdish Stop Word List'): 'extra_stopwords_kur',
                _tr('init_settings_global', 'extra-stopwords - Latvian Stop Word List'): 'extra_stopwords_lav',
                _tr('init_settings_global', 'extra-stopwords - Lithuanian Stop Word List'): 'extra_stopwords_lit',
                _tr('init_settings_global', 'extra-stopwords - Malay Stop Word List'): 'extra_stopwords_msa',
                _tr('init_settings_global', 'extra-stopwords - Marathi Stop Word List'): 'extra_stopwords_mar',
                _tr('init_settings_global', 'extra-stopwords - Mongolian Stop Word List'): 'extra_stopwords_mon',
                _tr('init_settings_global', 'extra-stopwords - Nepali Stop Word List'): 'extra_stopwords_nep',
                _tr('init_settings_global', 'extra-stopwords - Norwegian Bokmål Stop Word List'): 'extra_stopwords_nob',
                _tr('init_settings_global', 'extra-stopwords - Norwegian Bokmål Stop Word List'): 'extra_stopwords_nno',
                _tr('init_settings_global', 'extra-stopwords - Persian Stop Word List'): 'extra_stopwords_fas',
                _tr('init_settings_global', 'extra-stopwords - Polish Stop Word List'): 'extra_stopwords_pol',
                _tr('init_settings_global', 'extra-stopwords - Portuguese Stop Word List'): 'extra_stopwords_por',
                _tr('init_settings_global', 'extra-stopwords - Romanian Stop Word List'): 'extra_stopwords_ron',
                _tr('init_settings_global', 'extra-stopwords - Russian Stop Word List'): 'extra_stopwords_rus',
                _tr('init_settings_global', 'extra-stopwords - Serbian (Cyrillic) Stop Word List'): 'extra_stopwords_srp_cyrl',
                _tr('init_settings_global', 'extra-stopwords - Serbian (Latin) Stop Word List'): 'extra_stopwords_srp_latn',
                _tr('init_settings_global', 'extra-stopwords - Slovak Stop Word List'): 'extra_stopwords_slk',
                _tr('init_settings_global', 'extra-stopwords - Slovenian Stop Word List'): 'extra_stopwords_slv',
                _tr('init_settings_global', 'extra-stopwords - Spanish Stop Word List'): 'extra_stopwords_spa',
                _tr('init_settings_global', 'extra-stopwords - Swahili Stop Word List'): 'extra_stopwords_swa',
                _tr('init_settings_global', 'extra-stopwords - Swedish Stop Word List'): 'extra_stopwords_swe',
                _tr('init_settings_global', 'extra-stopwords - Tagalog Stop Word List'): 'extra_stopwords_tgl',
                _tr('init_settings_global', 'extra-stopwords - Telugu Stop Word List'): 'extra_stopwords_tel',
                _tr('init_settings_global', 'extra-stopwords - Thai Stop Word List'): 'extra_stopwords_tha',
                _tr('init_settings_global', 'extra-stopwords - Turkish Stop Word List'): 'extra_stopwords_tur',
                _tr('init_settings_global', 'extra-stopwords - Ukrainian Stop Word List'): 'extra_stopwords_ukr',
                _tr('init_settings_global', 'extra-stopwords - Urdu Stop Word List'): 'extra_stopwords_urd',
                _tr('init_settings_global', 'extra-stopwords - Vietnamese Stop Word List'): 'extra_stopwords_vie',
                _tr('init_settings_global', 'extra-stopwords - Yoruba Stop Word List'): 'extra_stopwords_yor',

                _tr('init_settings_global', 'NLTK - Arabic Stop Word List'): 'nltk_ara',
                _tr('init_settings_global', 'NLTK - Azerbaijani Stop Word List'): 'nltk_aze',
                _tr('init_settings_global', 'NLTK - Danish Stop Word List'): 'nltk_dan',
                _tr('init_settings_global', 'NLTK - Dutch Stop Word List'): 'nltk_nld',
                _tr('init_settings_global', 'NLTK - English Stop Word List'): 'nltk_eng',
                _tr('init_settings_global', 'NLTK - Finnish Stop Word List'): 'nltk_fin',
                _tr('init_settings_global', 'NLTK - French Stop Word List'): 'nltk_fra',
                _tr('init_settings_global', 'NLTK - German Stop Word List'): 'nltk_deu',
                _tr('init_settings_global', 'NLTK - Greek (Modern) Stop Word List'): 'nltk_ell',
                _tr('init_settings_global', 'NLTK - Hungarian Stop Word List'): 'nltk_hun',
                _tr('init_settings_global', 'NLTK - Indonesian Stop Word List'): 'nltk_ind',
                _tr('init_settings_global', 'NLTK - Italian Stop Word List'): 'nltk_ita',
                _tr('init_settings_global', 'NLTK - Kazakh Stop Word List'): 'nltk_kaz',
                _tr('init_settings_global', 'NLTK - Nepali Stop Word List'): 'nltk_nep',
                _tr('init_settings_global', 'NLTK - Norwegian Bokmål Stop Word List'): 'nltk_nob',
                _tr('init_settings_global', 'NLTK - Norwegian Nynorsk Stop Word List'): 'nltk_nno',
                _tr('init_settings_global', 'NLTK - Portuguese Stop Word List'): 'nltk_por',
                _tr('init_settings_global', 'NLTK - Romanian Stop Word List'): 'nltk_ron',
                _tr('init_settings_global', 'NLTK - Russian Stop Word List'): 'nltk_rus',
                _tr('init_settings_global', 'NLTK - Slovenian Stop Word List'): 'nltk_slv',
                _tr('init_settings_global', 'NLTK - Spanish Stop Word List'): 'nltk_spa',
                _tr('init_settings_global', 'NLTK - Swedish Stop Word List'): 'nltk_swe',
                _tr('init_settings_global', 'NLTK - Tajik Stop Word List'): 'nltk_tgk',
                _tr('init_settings_global', 'NLTK - Turkish Stop Word List'): 'nltk_tur',

                _tr('init_settings_global', 'PyThaiNLP - Thai Stop Word List'): 'pythainlp_tha',

                _tr('init_settings_global', 'spaCy - Afrikaans Stop Word List'): 'spacy_afr',
                _tr('init_settings_global', 'spaCy - Albanian Stop Word List'): 'spacy_sqi',
                _tr('init_settings_global', 'spaCy - Amharic Stop Word List'): 'spacy_amh',
                _tr('init_settings_global', 'spaCy - Arabic Stop Word List'): 'spacy_ara',
                _tr('init_settings_global', 'spaCy - Armenian Stop Word List'): 'spacy_hye',
                _tr('init_settings_global', 'spaCy - Azerbaijani Stop Word List'): 'spacy_aze',
                _tr('init_settings_global', 'spaCy - Basque Stop Word List'): 'spacy_eus',
                _tr('init_settings_global', 'spaCy - Bengali Stop Word List'): 'spacy_ben',
                _tr('init_settings_global', 'spaCy - Bulgarian Stop Word List'): 'spacy_bul',
                _tr('init_settings_global', 'spaCy - Catalan Stop Word List'): 'spacy_cat',
                _tr('init_settings_global', 'spaCy - Chinese (Simplified) Stop Word List'): 'spacy_zho_cn',
                _tr('init_settings_global', 'spaCy - Chinese (Traditional) Stop Word List'): 'spacy_zho_tw',
                _tr('init_settings_global', 'spaCy - Croatian Stop Word List'): 'spacy_hrv',
                _tr('init_settings_global', 'spaCy - Czech Stop Word List'): 'spacy_ces',
                _tr('init_settings_global', 'spaCy - Danish Stop Word List'): 'spacy_dan',
                _tr('init_settings_global', 'spaCy - Dutch Stop Word List'): 'spacy_nld',
                _tr('init_settings_global', 'spaCy - English Stop Word List'): 'spacy_eng',
                _tr('init_settings_global', 'spaCy - Estonian Stop Word List'): 'spacy_est',
                _tr('init_settings_global', 'spaCy - Finnish Stop Word List'): 'spacy_fin',
                _tr('init_settings_global', 'spaCy - French Stop Word List'): 'spacy_fra',
                _tr('init_settings_global', 'spaCy - German Stop Word List'): 'spacy_deu',
                _tr('init_settings_global', 'spaCy - Greek (Ancient) Stop Word List'): 'spacy_grc',
                _tr('init_settings_global', 'spaCy - Greek (Modern) Stop Word List'): 'spacy_ell',
                _tr('init_settings_global', 'spaCy - Gujarati Stop Word List'): 'spacy_guj',
                _tr('init_settings_global', 'spaCy - Hebrew Stop Word List'): 'spacy_heb',
                _tr('init_settings_global', 'spaCy - Hindi Stop Word List'): 'spacy_hin',
                _tr('init_settings_global', 'spaCy - Hungarian Stop Word List'): 'spacy_hun',
                _tr('init_settings_global', 'spaCy - Icelandic Stop Word List'): 'spacy_isl',
                _tr('init_settings_global', 'spaCy - Indonesian Stop Word List'): 'spacy_ind',
                _tr('init_settings_global', 'spaCy - Irish Stop Word List'): 'spacy_gle',
                _tr('init_settings_global', 'spaCy - Italian Stop Word List'): 'spacy_ita',
                _tr('init_settings_global', 'spaCy - Japanese Stop Word List'): 'spacy_jpn',
                _tr('init_settings_global', 'spaCy - Kannada Stop Word List'): 'spacy_kan',
                _tr('init_settings_global', 'spaCy - Korean Stop Word List'): 'spacy_kor',
                _tr('init_settings_global', 'spaCy - Kyrgyz Stop Word List'): 'spacy_kir',
                _tr('init_settings_global', 'spaCy - Latvian Stop Word List'): 'spacy_lav',
                _tr('init_settings_global', 'spaCy - Ligurian Stop Word List'): 'spacy_lij',
                _tr('init_settings_global', 'spaCy - Lithuanian Stop Word List'): 'spacy_lit',
                _tr('init_settings_global', 'spaCy - Luxembourgish Stop Word List'): 'spacy_ltz',
                _tr('init_settings_global', 'spaCy - Macedonian Stop Word List'): 'spacy_mkd',
                _tr('init_settings_global', 'spaCy - Malayalam Stop Word List'): 'spacy_mal',
                _tr('init_settings_global', 'spaCy - Marathi Stop Word List'): 'spacy_mar',
                _tr('init_settings_global', 'spaCy - Nepali Stop Word List'): 'spacy_nep',
                _tr('init_settings_global', 'spaCy - Norwegian Bokmål Stop Word List'): 'spacy_nob',
                _tr('init_settings_global', 'spaCy - Persian Stop Word List'): 'spacy_fas',
                _tr('init_settings_global', 'spaCy - Polish Stop Word List'): 'spacy_pol',
                _tr('init_settings_global', 'spaCy - Portuguese Stop Word List'): 'spacy_por',
                _tr('init_settings_global', 'spaCy - Romanian Stop Word List'): 'spacy_ron',
                _tr('init_settings_global', 'spaCy - Russian Stop Word List'): 'spacy_rus',
                _tr('init_settings_global', 'spaCy - Sanskrit Stop Word List'): 'spacy_san',
                _tr('init_settings_global', 'spaCy - Serbian (Cyrillic) Stop Word List'): 'spacy_srp_cyrl',
                _tr('init_settings_global', 'spaCy - Serbian (Latin) Stop Word List'): 'spacy_srp_latn',
                _tr('init_settings_global', 'spaCy - Sinhala Stop Word List'): 'spacy_sin',
                _tr('init_settings_global', 'spaCy - Slovak Stop Word List'): 'spacy_slk',
                _tr('init_settings_global', 'spaCy - Slovenian Stop Word List'): 'spacy_slv',
                _tr('init_settings_global', 'spaCy - Spanish Stop Word List'): 'spacy_spa',
                _tr('init_settings_global', 'spaCy - Swedish Stop Word List'): 'spacy_swe',
                _tr('init_settings_global', 'spaCy - Tagalog Stop Word List'): 'spacy_tgl',
                _tr('init_settings_global', 'spaCy - Tamil Stop Word List'): 'spacy_tam',
                _tr('init_settings_global', 'spaCy - Tatar Stop Word List'): 'spacy_tat',
                _tr('init_settings_global', 'spaCy - Telugu Stop Word List'): 'spacy_tel',
                _tr('init_settings_global', 'spaCy - Thai Stop Word List'): 'spacy_tha',
                _tr('init_settings_global', 'spaCy - Tigrinya Stop Word List'): 'spacy_tir',
                _tr('init_settings_global', 'spaCy - Tswana Stop Word List'): 'spacy_tsn',
                _tr('init_settings_global', 'spaCy - Turkish Stop Word List'): 'spacy_tur',
                _tr('init_settings_global', 'spaCy - Ukrainian Stop Word List'): 'spacy_ukr',
                _tr('init_settings_global', 'spaCy - Urdu Stop Word List'): 'spacy_urd',
                _tr('init_settings_global', 'spaCy - Vietnamese Stop Word List'): 'spacy_vie',
                _tr('init_settings_global', 'spaCy - Yoruba Stop Word List'): 'spacy_yor',

                _tr('init_settings_global', 'Stopwords ISO - Afrikaans Stop Word List'): 'stopwords_iso_afr',
                _tr('init_settings_global', 'Stopwords ISO - Arabic Stop Word List'): 'stopwords_iso_ara',
                _tr('init_settings_global', 'Stopwords ISO - Armenian Stop Word List'): 'stopwords_iso_hye',
                _tr('init_settings_global', 'Stopwords ISO - Basque Stop Word List'): 'stopwords_iso_eus',
                _tr('init_settings_global', 'Stopwords ISO - Bengali Stop Word List'): 'stopwords_iso_ben',
                _tr('init_settings_global', 'Stopwords ISO - Breton Stop Word List'): 'stopwords_iso_bre',
                _tr('init_settings_global', 'Stopwords ISO - Bulgarian Stop Word List'): 'stopwords_iso_bul',
                _tr('init_settings_global', 'Stopwords ISO - Catalan Stop Word List'): 'stopwords_iso_cat',
                _tr('init_settings_global', 'Stopwords ISO - Chinese (Simplified) Stop Word List'): 'stopwords_iso_zho_cn',
                _tr('init_settings_global', 'Stopwords ISO - Chinese (Traditional) Stop Word List'): 'stopwords_iso_zho_tw',
                _tr('init_settings_global', 'Stopwords ISO - Croatian Stop Word List'): 'stopwords_iso_hrv',
                _tr('init_settings_global', 'Stopwords ISO - Czech Stop Word List'): 'stopwords_iso_ces',
                _tr('init_settings_global', 'Stopwords ISO - Danish Stop Word List'): 'stopwords_iso_dan',
                _tr('init_settings_global', 'Stopwords ISO - Dutch Stop Word List'): 'stopwords_iso_nld',
                _tr('init_settings_global', 'Stopwords ISO - English Stop Word List'): 'stopwords_iso_eng',
                _tr('init_settings_global', 'Stopwords ISO - Esperanto Stop Word List'): 'stopwords_iso_epo',
                _tr('init_settings_global', 'Stopwords ISO - Estonian Stop Word List'): 'stopwords_iso_est',
                _tr('init_settings_global', 'Stopwords ISO - Finnish Stop Word List'): 'stopwords_iso_fin',
                _tr('init_settings_global', 'Stopwords ISO - French Stop Word List'): 'stopwords_iso_fra',
                _tr('init_settings_global', 'Stopwords ISO - Galician Stop Word List'): 'stopwords_iso_glg',
                _tr('init_settings_global', 'Stopwords ISO - German Stop Word List'): 'stopwords_iso_deu',
                _tr('init_settings_global', 'Stopwords ISO - Greek (Modern) Stop Word List'): 'stopwords_iso_ell',
                _tr('init_settings_global', 'Stopwords ISO - Gujarati Stop Word List'): 'stopwords_iso_guj',
                _tr('init_settings_global', 'Stopwords ISO - Hausa Stop Word List'): 'stopwords_iso_hau',
                _tr('init_settings_global', 'Stopwords ISO - Hebrew Stop Word List'): 'stopwords_iso_heb',
                _tr('init_settings_global', 'Stopwords ISO - Hindi Stop Word List'): 'stopwords_iso_hin',
                _tr('init_settings_global', 'Stopwords ISO - Hungarian Stop Word List'): 'stopwords_iso_hun',
                _tr('init_settings_global', 'Stopwords ISO - Indonesian Stop Word List'): 'stopwords_iso_ind',
                _tr('init_settings_global', 'Stopwords ISO - Irish Stop Word List'): 'stopwords_iso_gle',
                _tr('init_settings_global', 'Stopwords ISO - Italian Stop Word List'): 'stopwords_iso_ita',
                _tr('init_settings_global', 'Stopwords ISO - Japanese Stop Word List'): 'stopwords_iso_jpn',
                _tr('init_settings_global', 'Stopwords ISO - Korean Stop Word List'): 'stopwords_iso_kor',
                _tr('init_settings_global', 'Stopwords ISO - Kurdish Stop Word List'): 'stopwords_iso_kur',
                _tr('init_settings_global', 'Stopwords ISO - Latin Stop Word List'): 'stopwords_iso_lat',
                _tr('init_settings_global', 'Stopwords ISO - Latvian Stop Word List'): 'stopwords_iso_lav',
                _tr('init_settings_global', 'Stopwords ISO - Lithuanian Stop Word List'): 'stopwords_iso_lit',
                _tr('init_settings_global', 'Stopwords ISO - Malay Stop Word List'): 'stopwords_iso_msa',
                _tr('init_settings_global', 'Stopwords ISO - Marathi Stop Word List'): 'stopwords_iso_mar',
                _tr('init_settings_global', 'Stopwords ISO - Norwegian Stop Word List'): 'stopwords_iso_nob',
                _tr('init_settings_global', 'Stopwords ISO - Norwegian Stop Word List'): 'stopwords_iso_nno',
                _tr('init_settings_global', 'Stopwords ISO - Persian Stop Word List'): 'stopwords_iso_fas',
                _tr('init_settings_global', 'Stopwords ISO - Polish Stop Word List'): 'stopwords_iso_pol',
                _tr('init_settings_global', 'Stopwords ISO - Portuguese Stop Word List'): 'stopwords_iso_por',
                _tr('init_settings_global', 'Stopwords ISO - Romanian Stop Word List'): 'stopwords_iso_ron',
                _tr('init_settings_global', 'Stopwords ISO - Russian Stop Word List'): 'stopwords_iso_rus',
                _tr('init_settings_global', 'Stopwords ISO - Slovak Stop Word List'): 'stopwords_iso_slk',
                _tr('init_settings_global', 'Stopwords ISO - Slovenian Stop Word List'): 'stopwords_iso_slv',
                _tr('init_settings_global', 'Stopwords ISO - Somali Stop Word List'): 'stopwords_iso_som',
                _tr('init_settings_global', 'Stopwords ISO - Sotho (Southern) Stop Word List'): 'stopwords_iso_sot',
                _tr('init_settings_global', 'Stopwords ISO - Spanish Stop Word List'): 'stopwords_iso_spa',
                _tr('init_settings_global', 'Stopwords ISO - Swahili Stop Word List'): 'stopwords_iso_swa',
                _tr('init_settings_global', 'Stopwords ISO - Swedish Stop Word List'): 'stopwords_iso_swe',
                _tr('init_settings_global', 'Stopwords ISO - Tagalog Stop Word List'): 'stopwords_iso_tgl',
                _tr('init_settings_global', 'Stopwords ISO - Thai Stop Word List'): 'stopwords_iso_tha',
                _tr('init_settings_global', 'Stopwords ISO - Turkish Stop Word List'): 'stopwords_iso_tur',
                _tr('init_settings_global', 'Stopwords ISO - Ukrainian Stop Word List'): 'stopwords_iso_ukr',
                _tr('init_settings_global', 'Stopwords ISO - Urdu Stop Word List'): 'stopwords_iso_urd',
                _tr('init_settings_global', 'Stopwords ISO - Vietnamese Stop Word List'): 'stopwords_iso_vie',
                _tr('init_settings_global', 'Stopwords ISO - Yoruba Stop Word List'): 'stopwords_iso_yor',
                _tr('init_settings_global', 'Stopwords ISO - Zulu Stop Word List'): 'stopwords_iso_zul'
            }
        },

        'sentence_tokenizers': {
            'afr': [
                'spacy_sentencizer'
            ],

            'sqi': [
                'spacy_sentencizer'
            ],

            'amh': [
                'spacy_sentencizer'
            ],

            'ara': [
                'spacy_sentencizer'
            ],

            'hye': [
                'spacy_sentencizer'
            ],

            'aze': [
                'spacy_sentencizer'
            ],

            'eus': [
                'spacy_sentencizer'
            ],

            'ben': [
                'spacy_sentencizer'
            ],

            'bul': [
                'spacy_sentencizer'
            ],

            'cat': [
                'spacy_sentencizer'
            ],

            'zho_cn': [
                'spacy_sentence_recognizer',
                'wordless_zho'
            ],
            'zho_tw': [
                'spacy_sentence_recognizer',
                'wordless_zho'
            ],

            'hrv': [
                'spacy_sentencizer'
            ],

            'ces': [
                'nltk_punkt',
                'spacy_sentencizer'
            ],

            'dan': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'nld': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'eng_gb': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],
            'eng_us': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'est': [
                'nltk_punkt',
                'spacy_sentencizer'
            ],

            'fin': [
                'nltk_punkt',
                'spacy_sentencizer'
            ],

            'fra': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'deu_at': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],
            'deu_de': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],
            'deu_ch': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'grc': [
                'spacy_sentencizer'
            ],
            'ell': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'guj': [
                'spacy_sentencizer'
            ],

            'heb': [
                'spacy_sentencizer'
            ],

            'hin': [
                'spacy_sentencizer'
            ],

            'hun': [
                'spacy_sentencizer'
            ],

            'isl': [
                'spacy_sentencizer',
                'tokenizer_isl'
            ],

            'ind': [
                'spacy_sentencizer'
            ],

            'gle': [
                'spacy_sentencizer'
            ],

            'ita': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'jpn': [
                'spacy_sentence_recognizer',
                'wordless_jpn'
            ],

            'kan': [
                'spacy_sentencizer'
            ],

            'kir': [
                'spacy_sentencizer'
            ],

            'lav': [
                'spacy_sentencizer'
            ],

            'lij': [
                'spacy_sentencizer'
            ],

            'lit': [
                'spacy_sentence_recognizer'
            ],

            'ltz': [
                'spacy_sentencizer'
            ],

            'mkd': [
                'spacy_sentencizer'
            ],

            'mal': [
                'spacy_sentencizer'
            ],

            'mar': [
                'spacy_sentencizer'
            ],

            'nep': [
                'spacy_sentencizer'
            ],

            'nob': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'nno': [
                'nltk_punkt'
            ],

            'fas': [
                'spacy_sentencizer'
            ],

            'pol': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'por_br': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],
            'por_pt': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'ron': [
                'spacy_sentence_recognizer'
            ],

            'rus': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'san': [
                'spacy_sentencizer'
            ],

            'srp_cyrl': [
                'spacy_sentencizer'
            ],
            'srp_latn': [
                'spacy_sentencizer'
            ],

            'sin': [
                'spacy_sentencizer'
            ],

            'slk': [
                'spacy_sentencizer'
            ],

            'slv': [
                'nltk_punkt',
                'spacy_sentencizer'
            ],

            'spa': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ],

            'swe': [
                'nltk_punkt',
                'spacy_sentencizer'
            ],

            'tgl': [
                'spacy_sentencizer'
            ],

            'tam': [
                'spacy_sentencizer'
            ],

            'tat': [
                'spacy_sentencizer'
            ],

            'tel': [
                'spacy_sentencizer'
            ],

            'tha': [
                'pythainlp_crfcut'
            ],

            'bod': [
                'botok_bod'
            ],

            'tir': [
                'spacy_sentencizer'
            ],

            'tsn': [
                'spacy_sentencizer'
            ],

            'tur': [
                'nltk_punkt',
                'spacy_sentencizer'
            ],

            'ukr': [
                'spacy_sentencizer'
            ],

            'urd': [
                'spacy_sentencizer'
            ],

            'vie': [
                'underthesea_vie'
            ],

            'yor': [
                'spacy_sentencizer'
            ],

            'other': [
                'nltk_punkt',
                'spacy_sentence_recognizer'
            ]
        },

        'word_tokenizers': {
            'afr': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_afr'
            ],

            'sqi': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_sqi'
            ],

            'amh': [
                'spacy_amh'
            ],

            'ara': [
                'spacy_ara'
            ],

            'hye': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_hye'
            ],

            'asm': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses'
            ],

            'aze': [
                'spacy_aze'
            ],

            'eus': [
                'spacy_eus'
            ],

            'ben': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_ben'
            ],

            'bul': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_bul'
            ],

            'cat': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_cat'
            ],

            'zho_cn': [
                'jieba_zho',
                'pkuseg_zho',
                'spacy_zho',
                'wordless_zho_char'
            ],
            'zho_tw': [
                'jieba_zho',
                'pkuseg_zho',
                'spacy_zho',
                'wordless_zho_char'
            ],

            'hrv': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_hrv'
            ],

            'ces': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_ces'
            ],

            'dan': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_dan'
            ],

            'nld': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_nld'
            ],

            'eng_gb': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_eng'
            ],
            'eng_us': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_eng'
            ],

            'est': [
                'sacremoses_moses',
                'spacy_est'
            ],

            'fin': [
                'sacremoses_moses',
                'spacy_fin'
            ],

            'fra': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_fra'
            ],

            'deu_at': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_deu'
            ],
            'deu_de': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_deu'
            ],
            'deu_ch': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_deu'
            ],

            'grc': [
                'spacy_grc'
            ],
            'ell': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_ell'
            ],

            'guj': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_guj'
            ],

            'heb': [
                'spacy_heb'
            ],

            'hin': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_hin'
            ],

            'hun': [
                'sacremoses_moses',
                'spacy_hun'
            ],

            'isl': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_isl',
                'tokenizer_isl'
            ],

            'ind': [
                'spacy_ind'
            ],

            'gle': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_gle'
            ],

            'ita': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_ita'
            ],

            'jpn': [
                'nagisa_jpn',
                'spacy_jpn',
                'sudachipy_jpn_split_mode_a',
                'sudachipy_jpn_split_mode_b',
                'sudachipy_jpn_split_mode_c',
                'wordless_jpn_kanji'
            ],

            'kan': [
                'sacremoses_moses',
                'spacy_kan'
            ],

            'kir': [
                'spacy_kir'
            ],

            'lav': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_lav'
            ],

            'lij': [
                'spacy_lij'
            ],

            'lit': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_lit'
            ],

            'ltz': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_ltz'
            ],

            'mkd': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_mkd'
            ],

            'mal': [
                'sacremoses_moses',
                'spacy_mal'
            ],

            'mar': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_mar'
            ],

            'mni': [
                'sacremoses_moses'
            ],

            'nep': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_nep'
            ],

            'nob': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_nob'
            ],

            'ori': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses'
            ],

            'fas': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'spacy_fas'
            ],

            'pol': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_pol'
            ],

            'por_br': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_por'
            ],
            'por_pt': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_por'
            ],

            'pan': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses'
            ],

            'ron': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_ron'
            ],

            'rus': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_rus'
            ],

            'san': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_san'
            ],

            'srp_cyrl': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_srp'
            ],
            'srp_latn': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_srp'
            ],

            'sin': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_sin'
            ],

            'slk': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_slk'
            ],

            'slv': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_slv'
            ],

            'spa': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_spa'
            ],

            'swe': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_swe'
            ],

            'tgl': [
                'spacy_tgl'
            ],

            'tgk': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
            ],

            'tam': [
                'sacremoses_moses',
                'spacy_tam'
            ],

            'tat': [
                'spacy_tat'
            ],

            'tel': [
                'sacremoses_moses',
                'spacy_tel'
            ],

            'tdt': [
                'sacremoses_moses'
            ],

            'tha': [
                'pythainlp_longest_matching',
                'pythainlp_max_matching',
                'pythainlp_max_matching_tcc',
                'pythainlp_max_matching_tcc_safe_mode',
                'pythainlp_nercut'
            ],

            'bod': [
                'botok_bod'
            ],

            'tir': [
                'spacy_tir'
            ],

            'tsn': [
                'spacy_tsn'
            ],

            'tur': [
                'spacy_tur'
            ],

            'ukr': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_ukr'
            ],

            'urd': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_twitter',
                'spacy_urd'
            ],

            'vie': [
                'nltk_tok_tok',
                'underthesea_vie'
            ],

            'yor': [
                'spacy_yor'
            ],

            'other': [
                'nltk_nist', 'nltk_nltk', 'nltk_penn_treebank', 'nltk_tok_tok', 'nltk_twitter',
                'sacremoses_moses',
                'spacy_eng'
            ]
        },

        'syl_tokenizers': {
            'afr': [
                'pyphen_afr'
            ],

            'sqi': [
                'pyphen_sqi'
            ],

            'bel': [
                'pyphen_bel'
            ],

            'bul': [
                'pyphen_bul'
            ],

            'hrv': [
                'pyphen_hrv'
            ],

            'ces': [
                'pyphen_ces'
            ],

            'dan': [
                'pyphen_dan'
            ],

            'nld': [
                'pyphen_nld'
            ],

            'eng_gb': [
                'pyphen_eng_gb'
            ],
            'eng_us': [
                'pyphen_eng_us'
            ],

            'epo': [
                'pyphen_epo'
            ],

            'est': [
                'pyphen_est'
            ],

            'fra': [
                'pyphen_fra'
            ],

            'glg': [
                'pyphen_glg'
            ],

            'deu_at': [
                'pyphen_deu_at'
            ],
            'deu_de': [
                'pyphen_deu_de'
            ],
            'deu_ch': [
                'pyphen_deu_ch'
            ],

            'ell': [
                'pyphen_ell'
            ],

            'hun': [
                'pyphen_hun'
            ],

            'isl': [
                'pyphen_isl'
            ],

            'ind': [
                'pyphen_ind'
            ],

            'ita': [
                'pyphen_ita'
            ],

            'lit': [
                'pyphen_lit'
            ],

            'lav': [
                'pyphen_lav'
            ],

            'mon': [
                'pyphen_mon'
            ],

            'nob': [
                'pyphen_nob'
            ],
            'nno': [
                'pyphen_nno'
            ],

            'pol': [
                'pyphen_pol'
            ],

            'por_br': [
                'pyphen_por_br'
            ],
            'por_pt': [
                'pyphen_por_pt'
            ],

            'ron': [
                'pyphen_ron'
            ],

            'rus': [
                'pyphen_rus'
            ],

            'srp_cyrl': [
                'pyphen_srp_cyrl'
            ],
            'srp_latn': [
                'pyphen_srp_latn'
            ],

            'slk': [
                'pyphen_slk'
            ],

            'slv': [
                'pyphen_slv'
            ],

            'spa': [
                'pyphen_spa'
            ],

            'swe': [
                'pyphen_swe'
            ],

            'tel': [
                'pyphen_tel'
            ],

            'tha': [
                'pythainlp_tha',
                'ssg_tha'
            ],

            'ukr': [
                'pyphen_ukr'
            ],

            'zul': [
                'pyphen_zul'
            ]
        },

        'pos_taggers': {
            'cat': [
                'spacy_cat'
            ],

            'zho_cn': [
                'jieba_zho',
                'spacy_zho'
            ],
            'zho_tw': [
                'jieba_zho',
                'spacy_zho'
            ],

            'dan': [
                'spacy_dan',
            ],

            'nld': [
                'spacy_nld'
            ],

            'eng_gb': [
                'nltk_perceptron',
                'spacy_eng'
            ],
            'eng_us': [
                'nltk_perceptron',
                'spacy_eng'
            ],

            'fra': [
                'spacy_fra'
            ],

            'deu_at': [
                'spacy_deu'
            ],
            'deu_de': [
                'spacy_deu'
            ],
            'deu_ch': [
                'spacy_deu'
            ],

            'ell': [
                'spacy_ell'
            ],

            'ita': [
                'spacy_ita'
            ],

            'jpn': [
                'nagisa_jpn',
                'spacy_jpn',
                'sudachipy_jpn'
            ],

            'lit': [
                'spacy_lit'
            ],

            'mkd': [
                'spacy_mkd'
            ],

            'nob': [
                'spacy_nob'
            ],

            'pol': [
                'spacy_pol'
            ],

            'por_br': [
                'spacy_por'
            ],
            'por_pt': [
                'spacy_por'
            ],

            'ron': [
                'spacy_ron'
            ],

            'rus': [
                'nltk_perceptron',
                'pymorphy2_morphological_analyzer',
                'spacy_rus'
            ],

            'spa': [
                'spacy_spa'
            ],

            'tha': [
                'pythainlp_perceptron_lst20',
                'pythainlp_perceptron_orchid',
                'pythainlp_perceptron_pud'
            ],

            'bod': [
                'botok_bod'
            ],

            'ukr': [
                'pymorphy2_morphological_analyzer'
            ],

            'vie': [
                'underthesea_vie'
            ]
        },

        'lemmatizers': {
            'ast': [
                'lemmatization_lists_ast'
            ],

            'ben': [
                'spacy_ben'
            ],

            'bul': [
                'lemmatization_lists_bul'
            ],

            'cat': [
                'lemmatization_lists_cat',
                'spacy_cat'
            ],

            'hrv': [
                'spacy_hrv'
            ],

            'ces': [
                'lemmatization_lists_ces',
                'spacy_ces'
            ],

            'dan': [
                'spacy_dan'
            ],

            'nld': [
                'spacy_nld'
            ],

            'eng_gb': [
                'lemmatization_lists_eng',
                'nltk_wordnet',
                'spacy_eng'
            ],
            'eng_us': [
                'lemmatization_lists_eng',
                'nltk_wordnet',
                'spacy_eng'
            ],

            'est': [
                'lemmatization_lists_est'
            ],

            'fra': [
                'lemmatization_lists_fra',
                'spacy_fra'
            ],

            'glg': [
                'lemmatization_lists_glg'
            ],

            'deu_at': [
                'lemmatization_lists_deu',
                'spacy_deu'
            ],
            'deu_de': [
                'lemmatization_lists_deu',
                'spacy_deu'
            ],
            'deu_ch': [
                'lemmatization_lists_deu',
                'spacy_deu'
            ],

            'grc': [
                'spacy_grc'
            ],
            'ell': [
                'spacy_ell'
            ],

            'hun': [
                'lemmatization_lists_hun',
                'spacy_hun'
            ],

            'ind': [
                'spacy_ind'
            ],

            'gle': [
                'lemmatization_lists_gle',
                'spacy_gle'
            ],

            'ita': [
                'lemmatization_lists_ita',
                'spacy_ita'
            ],

            'jpn': [
                'spacy_jpn',
                'sudachipy_jpn'
            ],

            'lit': [
                'spacy_lit'
            ],

            'ltz': [
                'spacy_ltz'
            ],

            'mkd': [
                'spacy_mkd'
            ],

            'glv': [
                'lemmatization_lists_glv'
            ],

            'nob': [
                'spacy_nob'
            ],

            'fas': [
                'lemmatization_lists_fas',
                'spacy_fas'
            ],

            'pol': [
                'spacy_pol'
            ],

            'por_br': [
                'lemmatization_lists_por',
                'spacy_por'
            ],
            'por_pt': [
                'lemmatization_lists_por',
                'spacy_por'
            ],

            'ron': [
                'lemmatization_lists_ron',
                'spacy_ron'
            ],

            'rus': [
                'lemmatization_lists_rus',
                'pymorphy2_morphological_analyzer',
                'spacy_rus'
            ],

            'gla': [
                'lemmatization_lists_gla'
            ],

            'srp_cyrl': [
                'spacy_srp_cyrl'
            ],

            'slk': [
                'lemmatization_lists_slk'
            ],

            'slv': [
                'lemmatization_lists_slv'
            ],

            'spa': [
                'lemmatization_lists_spa',
                'spacy_spa'
            ],

            'swe': [
                'lemmatization_lists_swe',
                'spacy_swe'
            ],

            'tgl': [
                'spacy_tgl'
            ],

            'bod': [
                'botok_bod'
            ],

            'tur': [
                'spacy_tur'
            ],

            'ukr': [
                'lemmatization_lists_ukr',
                'pymorphy2_morphological_analyzer'
            ],

            'urd': [
                'spacy_urd'
            ],

            'cym': [
                'lemmatization_lists_cym'
            ]
        },

        'stop_word_lists': {
            'afr': [
                'spacy_afr',
                'stopwords_iso_afr',
                'custom'
            ],

            'akk': [
                'cltk_akk',
                'custom'
            ],

            'sqi': [
                'extra_stopwords_sqi',
                'spacy_sqi',
                'custom'
            ],

            'amh': [
                'spacy_amh',
                'custom'
            ],

            'ara': [
                'extra_stopwords_ara',
                'nltk_ara',
                'spacy_ara',
                'stopwords_iso_ara',
                'custom'
            ],

            'arb': [
                'cltk_arb',
                'custom'
            ],

            'hye': [
                'extra_stopwords_hye',
                'spacy_hye',
                'stopwords_iso_hye',
                'custom'
            ],

            'aze': [
                'nltk_aze',
                'spacy_aze',
                'custom'
            ],

            'eus': [
                'extra_stopwords_eus',
                'spacy_eus',
                'stopwords_iso_eus',
                'custom'
            ],

            'bel': [
                'extra_stopwords_bel',
                'custom'
            ],

            'ben': [
                'extra_stopwords_ben',
                'spacy_ben',
                'stopwords_iso_ben',
                'custom'
            ],

            'bre': [
                'stopwords_iso_bre',
                'custom'
            ],

            'bul': [
                'extra_stopwords_bul',
                'spacy_bul',
                'stopwords_iso_bul',
                'custom'
            ],

            'cat': [
                'extra_stopwords_cat',
                'spacy_cat',
                'stopwords_iso_cat',
                'custom'
            ],

            'zho_cn': [
                'extra_stopwords_zho_cn',
                'spacy_zho_cn',
                'stopwords_iso_zho_cn',
                'custom'
            ],
            'zho_tw': [
                'extra_stopwords_zho_tw',
                'spacy_zho_tw',
                'stopwords_iso_zho_tw',
                'custom'
            ],

            'cop': [
                'cltk_cop',
                'custom'
            ],

            'hrv': [
                'extra_stopwords_hrv',
                'spacy_hrv',
                'stopwords_iso_hrv',
                'custom'
            ],

            'ces': [
                'extra_stopwords_ces',
                'spacy_ces',
                'stopwords_iso_ces',
                'custom'
            ],

            'dan': [
                'extra_stopwords_dan',
                'nltk_dan',
                'spacy_dan',
                'stopwords_iso_dan',
                'custom'
            ],

            'nld': [
                'extra_stopwords_nld',
                'nltk_nld',
                'spacy_nld',
                'stopwords_iso_nld',
                'custom'
            ],

            'enm': [
                'cltk_enm',
                'custom'
            ],
            'ang': [
                'cltk_ang',
                'custom'
            ],
            'eng_gb': [
                'extra_stopwords_eng',
                'nltk_eng',
                'spacy_eng',
                'stopwords_iso_eng',
                'custom'
            ],
            'eng_us': [
                'extra_stopwords_eng',
                'nltk_eng',
                'spacy_eng',
                'stopwords_iso_eng',
                'custom'
            ],

            'epo': [
                'stopwords_iso_epo',
                'custom'
            ],

            'est': [
                'extra_stopwords_est',
                'spacy_est',
                'stopwords_iso_est',
                'custom'
            ],

            'fin': [
                'extra_stopwords_fin',
                'nltk_fin',
                'spacy_fin',
                'stopwords_iso_fin',
                'custom'
            ],

            'fra': [
                'extra_stopwords_fra',
                'nltk_fra',
                'spacy_fra',
                'stopwords_iso_fra',
                'custom'
            ],
            'fro': [
                'cltk_fro',
                'custom'
            ],

            'glg': [
                'extra_stopwords_glg',
                'stopwords_iso_glg',
                'custom'
            ],

            'deu_at': [
                'extra_stopwords_deu',
                'nltk_deu',
                'spacy_deu',
                'stopwords_iso_deu',
                'custom'
            ],
            'deu_de': [
                'extra_stopwords_deu',
                'nltk_deu',
                'spacy_deu',
                'stopwords_iso_deu',
                'custom'
            ],
            'gmh': [
                'cltk_gmh',
                'custom'
            ],
            'deu_ch': [
                'extra_stopwords_deu',
                'nltk_deu',
                'spacy_deu',
                'stopwords_iso_deu',
                'custom'
            ],

            'grc': [
                'cltk_grc',
                'spacy_grc',
                'custom'
            ],
            'ell': [
                'extra_stopwords_ell',
                'nltk_ell',
                'spacy_ell',
                'stopwords_iso_ell',
                'custom'
            ],

            'guj': [
                'spacy_guj',
                'stopwords_iso_guj',
                'custom'
            ],

            'hau': [
                'extra_stopwords_hau',
                'stopwords_iso_hau',
                'custom'
            ],

            'heb': [
                'extra_stopwords_heb',
                'spacy_heb',
                'stopwords_iso_heb',
                'custom'
            ],

            'hin': [
                'cltk_hin',
                'extra_stopwords_hin',
                'spacy_hin',
                'stopwords_iso_hin',
                'custom'
            ],

            'hun': [
                'extra_stopwords_hun',
                'nltk_hun',
                'spacy_hun',
                'stopwords_iso_hun',
                'custom'
            ],

            'isl': [
                'extra_stopwords_isl',
                'spacy_isl',
                'custom'
            ],

            'ind': [
                'extra_stopwords_ind',
                'nltk_ind',
                'spacy_ind',
                'stopwords_iso_ind',
                'custom'
            ],

            'gle': [
                'extra_stopwords_gle',
                'spacy_gle',
                'stopwords_iso_gle',
                'custom'
            ],

            'ita': [
                'extra_stopwords_ita',
                'nltk_ita',
                'spacy_ita',
                'stopwords_iso_ita',
                'custom'
            ],

            'jpn': [
                'extra_stopwords_jpn',
                'spacy_jpn',
                'stopwords_iso_jpn',
                'custom'
            ],

            'kan': [
                'spacy_kan',
                'custom'
            ],

            'kaz': [
                'nltk_kaz',
                'custom'
            ],

            'kor': [
                'extra_stopwords_kor',
                'spacy_kor',
                'stopwords_iso_kor',
                'custom'
            ],

            'kur': [
                'extra_stopwords_kur',
                'stopwords_iso_kur',
                'custom'
            ],

            'kir': [
                'spacy_kir',
                'custom'
            ],

            'lat': [
                'cltk_lat',
                'stopwords_iso_lat',
                'custom'
            ],

            'lav': [
                'extra_stopwords_lav',
                'spacy_lav',
                'stopwords_iso_lav',
                'custom'
            ],

            'lij': [
                'spacy_lij',
                'custom'
            ],

            'lit': [
                'extra_stopwords_lit',
                'spacy_lit',
                'stopwords_iso_lit',
                'custom'
            ],

            'ltz': [
                'spacy_ltz',
                'custom'
            ],

            'mkd': [
                'spacy_mkd',
                'custom'
            ],

            'msa': [
                'extra_stopwords_msa',
                'stopwords_iso_msa',
                'custom'
            ],

            'mal': [
                'spacy_mal',
                'custom'
            ],

            'mar': [
                'extra_stopwords_mar',
                'spacy_mar',
                'stopwords_iso_mar',
                'custom'
            ],

            'omr': [
                'cltk_omr',
                'custom'
            ],

            'mon': [
                'extra_stopwords_mon',
                'custom'
            ],

            'nep': [
                'extra_stopwords_nep',
                'nltk_nep',
                'spacy_nep',
                'custom'
            ],

            'non': [
                'cltk_non',
                'custom'
            ],
            'nob': [
                'extra_stopwords_nob',
                'nltk_nob',
                'spacy_nob',
                'stopwords_iso_nob',
                'custom'
            ],
            'nno': [
                'extra_stopwords_nno',
                'nltk_nno',
                'stopwords_iso_nno',
                'custom'
            ],

            'fas': [
                'extra_stopwords_fas',
                'spacy_fas',
                'stopwords_iso_fas',
                'custom'
            ],

            'pol': [
                'extra_stopwords_pol',
                'spacy_pol',
                'stopwords_iso_pol',
                'custom'
            ],

            'por_br': [
                'extra_stopwords_por',
                'nltk_por',
                'spacy_por',
                'stopwords_iso_por',
                'custom'
            ],
            'por_pt': [
                'extra_stopwords_por',
                'nltk_por',
                'spacy_por',
                'stopwords_iso_por',
                'custom'
            ],

            'pan': [
                'cltk_pan',
                'custom'
            ],

            'ron': [
                'extra_stopwords_ron',
                'nltk_ron',
                'spacy_ron',
                'stopwords_iso_ron',
                'custom'
            ],

            'rus': [
                'extra_stopwords_rus',
                'nltk_rus',
                'spacy_rus',
                'stopwords_iso_rus',
                'custom'
            ],

            'san': [
                'cltk_san',
                'spacy_san',
                'custom'
            ],

            'srp_cyrl': [
                'extra_stopwords_srp_cyrl',
                'spacy_srp_cyrl',
                'custom'
            ],
            'srp_latn': [
                'extra_stopwords_srp_latn',
                'spacy_srp_latn',
                'custom'
            ],

            'sin': [
                'spacy_sin',
                'custom'
            ],

            'slk': [
                'extra_stopwords_slk',
                'spacy_slk',
                'stopwords_iso_slk',
                'custom'
            ],

            'slv': [
                'extra_stopwords_slv',
                'nltk_slv',
                'spacy_slv',
                'stopwords_iso_slv',
                'custom'
            ],

            'som': [
                'stopwords_iso_som',
                'custom'
            ],

            'sot': [
                'stopwords_iso_sot',
                'custom'
            ],

            'spa': [
                'extra_stopwords_spa',
                'nltk_spa',
                'spacy_spa',
                'stopwords_iso_spa',
                'custom'
            ],

            'swa': [
                'extra_stopwords_swa',
                'stopwords_iso_swa',
                'custom'
            ],

            'swe': [
                'extra_stopwords_swe',
                'nltk_swe',
                'spacy_swe',
                'stopwords_iso_swe',
                'custom'
            ],

            'tgl': [
                'extra_stopwords_tgl',
                'spacy_tgl',
                'stopwords_iso_tgl',
                'custom'
            ],

            'tgk': [
                'nltk_tgk',
                'custom'
            ],

            'tam': [
                'spacy_tam',
                'custom'
            ],

            'tat': [
                'spacy_tat',
                'custom'
            ],

            'tel': [
                'extra_stopwords_tel',
                'spacy_tel',
                'custom'
            ],

            'tha': [
                'extra_stopwords_tha',
                'pythainlp_tha',
                'spacy_tha',
                'stopwords_iso_tha',
                'custom'
            ],

            'tir': [
                'spacy_tir',
                'custom'
            ],

            'tsn': [
                'spacy_tsn',
                'custom'
            ],

            'tur': [
                'extra_stopwords_tur',
                'nltk_tur',
                'spacy_tur',
                'stopwords_iso_tur',
                'custom'
            ],

            'ukr': [
                'extra_stopwords_ukr',
                'spacy_ukr',
                'stopwords_iso_ukr',
                'custom'
            ],

            'urd': [
                'extra_stopwords_urd',
                'spacy_urd',
                'stopwords_iso_urd',
                'custom'
            ],

            'vie': [
                'extra_stopwords_vie',
                'spacy_vie',
                'stopwords_iso_vie',
                'custom'
            ],

            'yor': [
                'extra_stopwords_yor',
                'spacy_yor',
                'stopwords_iso_yor',
                'custom'
            ],

            'zul': [
                'stopwords_iso_zul',
                'custom'
            ],

            'other': [
                'custom'
            ]
        },

        'measures_dispersion': {
            _tr('init_settings_global', "Carroll's D₂"): {
                'col': _tr('init_settings_global', "Carroll's D₂"),
                'func': wl_measures_dispersion.carrolls_d2
            },

            _tr('init_settings_global', "Gries's DP"): {
                'col': _tr('init_settings_global', "Gries's DP"),
                'func': wl_measures_dispersion.griess_dp
            },

            _tr('init_settings_global', "Gries's DPnorm"): {
                'col': _tr('init_settings_global', "Gries's DPnorm"),
                'func': wl_measures_dispersion.griess_dp_norm
            },

            _tr('init_settings_global', "Juilland's D"): {
                'col': _tr('init_settings_global', "Juilland's D"),
                'func': wl_measures_dispersion.juillands_d
            },

            _tr('init_settings_global', "Lyne's D₃"): {
                'col': _tr('init_settings_global', "Lyne's D₃"),
                'func': wl_measures_dispersion.lynes_d3
            },

            _tr('init_settings_global', "Rosengren's S"): {
                'col': _tr('init_settings_global', "Rosengren's S"),
                'func': wl_measures_dispersion.rosengrens_s
            },

            _tr('init_settings_global', "Zhang's Distributional Consistency"): {
                'col': _tr('init_settings_global', "Zhang's DC"),
                'func': wl_measures_dispersion.zhangs_distributional_consistency
            }
        },

        'measures_adjusted_freq': {
            _tr('init_settings_global', "Carroll's Um"): {
                'col': _tr('init_settings_global', "Carroll's Um"),
                'func': wl_measures_adjusted_freq.carrolls_um
            },

            _tr('init_settings_global', "Engwall's FM"): {
                'col': _tr('init_settings_global', "Engwall's FM"),
                'func': wl_measures_adjusted_freq.engwalls_fm
            },

            _tr('init_settings_global', "Juilland's U"): {
                'col': _tr('init_settings_global', "Juilland's U"),
                'func': wl_measures_adjusted_freq.juillands_u
            },

            _tr('init_settings_global', "Kromer's UR"): {
                'col': _tr('init_settings_global', "Kromer's UR"),
                'func': wl_measures_adjusted_freq.kromers_ur
            },

            _tr('init_settings_global', "Rosengren's KF"): {
                'col': _tr('init_settings_global', "Rosengren's KF"),
                'func': wl_measures_adjusted_freq.rosengrens_kf
            }
        },

        'tests_significance': {
            'collocation_extractor': {
                _tr('init_settings_global', "Berry-Rogghe's z-score"): {
                    'cols': [
                        _tr('init_settings_global', "Berry-Rogghe's z-score"),
                        _tr('init_settings_global', 'p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.berry_rogghes_z_score
                },

                _tr('init_settings_global', "Fisher's Exact Test"): {
                    'cols': [
                        None,
                        _tr('init_settings_global', 'p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.fishers_exact_test
                },

                _tr('init_settings_global', 'Log-likelihood Ratio Test'): {
                    'cols': [
                        _tr('init_settings_global', 'Log-likelihood Ratio'),
                        _tr('init_settings_global', 'p-value'),
                        _tr('init_settings_global', 'Bayes Factor')
                    ],

                    'func': wl_measures_statistical_significance.log_likehood_ratio_test
                },

                _tr('init_settings_global', "Pearson's Chi-squared Test"): {
                    'cols': [
                        _tr('init_settings_global', 'χ2'),
                        _tr('init_settings_global', 'p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.pearsons_chi_squared_test
                },

                _tr('init_settings_global', "Student's t-test (1-sample)"): {
                    'cols': [
                        _tr('init_settings_global', 't-statistic'),
                        _tr('init_settings_global', 'p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.students_t_test_1_sample
                },

                _tr('init_settings_global', 'z-score'): {
                    'cols': [
                        _tr('init_settings_global', 'z-score'),
                        _tr('init_settings_global', 'p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.z_score
                }
            },

            'keyword_extractor': {
                _tr('init_settings_global', "Fisher's Exact Test"): {
                    'cols': [
                        None,
                        _tr('init_settings_global', 'p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.fishers_exact_test
                },

                _tr('init_settings_global', 'Log-likelihood Ratio Test'): {
                    'cols': [
                        _tr('init_settings_global', 'Log-likelihood Ratio'),
                        _tr('init_settings_global', 'p-value'),
                        _tr('init_settings_global', 'Bayes Factor')
                    ],

                    'func': wl_measures_statistical_significance.log_likehood_ratio_test
                },

                _tr('init_settings_global', 'Mann-Whitney U Test'): {
                    'cols': [
                        _tr('init_settings_global', 'U Statistic'),
                        _tr('init_settings_global', 'p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.mann_whitney_u_test
                },

                _tr('init_settings_global', "Pearson's Chi-squared Test"): {
                    'cols': [
                        _tr('init_settings_global', 'χ2'),
                        _tr('init_settings_global', 'p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.pearsons_chi_squared_test
                },

                _tr('init_settings_global', "Student's t-test (2-sample)"): {
                    'cols': [
                        _tr('init_settings_global', 't-statistic'),
                        _tr('init_settings_global', 'p-value'),
                        _tr('init_settings_global', 'Bayes Factor')
                    ],

                    'func': wl_measures_statistical_significance.students_t_test_2_sample
                }
            }
        },

        'measures_effect_size': {
            'collocation_extractor': {
                _tr('init_settings_global', 'Cubic Association Ratio'): {
                    'col': _tr('init_settings_global', 'IM³'),
                    'func': wl_measures_effect_size.im3
                },

                _tr('init_settings_global', "Dice's Coefficient"): {
                    'col': _tr('init_settings_global', "Dice's Coefficient"),
                    'func': wl_measures_effect_size.dices_coeff
                },

                _tr('init_settings_global', 'Jaccard Index'): {
                    'col': _tr('init_settings_global', 'Jaccard Index'),
                    'func': wl_measures_effect_size.jaccard_index
                },

                _tr('init_settings_global', 'Log-Frequency Biased MD'): {
                    'col': _tr('init_settings_global', 'LFMD'),
                    'func': wl_measures_effect_size.lfmd
                },

                _tr('init_settings_global', 'logDice'): {
                    'col': _tr('init_settings_global', 'logDice'),
                    'func': wl_measures_effect_size.log_dice
                },

                _tr('init_settings_global', 'MI.log-f'): {
                    'col': _tr('init_settings_global', 'MI.log-f'),
                    'func': wl_measures_effect_size.mi_log_f
                },

                _tr('init_settings_global', 'Minimum Sensitivity'): {
                    'col': _tr('init_settings_global', 'Minimum Sensitivity'),
                    'func': wl_measures_effect_size.min_sensitivity
                },

                _tr('init_settings_global', 'Mutual Dependency'): {
                    'col': _tr('init_settings_global', 'MD'),
                    'func': wl_measures_effect_size.md
                },

                _tr('init_settings_global', 'Mutual Expectation'): {
                    'col': _tr('init_settings_global', 'ME'),
                    'func': wl_measures_effect_size.me
                },

                _tr('init_settings_global', 'Mutual Information'): {
                    'col': _tr('init_settings_global', 'MI'),
                    'func': wl_measures_effect_size.mi
                },

                _tr('init_settings_global', 'Pointwise Mutual Information'): {
                    'col': _tr('init_settings_global', 'PMI'),
                    'func': wl_measures_effect_size.pmi
                },

                _tr('init_settings_global', 'Poisson Collocation Measure'): {
                    'col': _tr('init_settings_global', 'Poisson Collocation Measure'),
                    'func': wl_measures_effect_size.poisson_collocation_measure
                },

                _tr('init_settings_global', 'Squared Phi Coefficient'): {
                    'col': _tr('init_settings_global', 'φ2'),
                    'func': wl_measures_effect_size.squared_phi_coeff
                }
            },

            'keyword_extractor': {
                _tr('init_settings_global', '%DIFF'): {
                    'col': _tr('init_settings_global', '%DIFF'),
                    'func': wl_measures_effect_size.pct_diff
                },

                _tr('init_settings_global', 'Difference Coefficient'): {
                    'col': _tr('init_settings_global', 'Difference Coefficient'),
                    'func': wl_measures_effect_size.diff_coeff
                },

                _tr('init_settings_global', "Kilgarriff's Ratio"): {
                    'col': _tr('init_settings_global', "Kilgarriff's Ratio"),
                    'func': wl_measures_effect_size.kilgarriffs_ratio
                },

                _tr('init_settings_global', 'Log Ratio'): {
                    'col': _tr('init_settings_global', 'Log Ratio'),
                    'func': wl_measures_effect_size.log_ratio
                },

                _tr('init_settings_global', 'Odds Ratio'): {
                    'col': _tr('init_settings_global', 'Odds Ratio'),
                    'func': wl_measures_effect_size.odds_ratio
                }
            }
        },

        'styles': {
            'style_dialog': '''
                <head>
                    <style>
                        * {
                            outline: none;
                            margin: 0;
                            border: 0;
                            padding: 0;

                            line-height: 120%;
                            text-align: justify;
                        }

                        div {
                            margin-bottom: 3px;
                        }
                        div:last-child {
                            margin-bottom: 0;
                        }

                        ul {
                            margin-bottom: 3px;
                        }
                        ul:last-child {
                            margin-bottom: 0;
                        }

                        li {
                            margin-left: -30px;
                        }
                    </style>
                </head>
            '''
        }
    }
