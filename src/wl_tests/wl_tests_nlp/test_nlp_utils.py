# ----------------------------------------------------------------------
# Wordless: Tests - NLP - NLP Utilities
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

from wl_nlp import wl_nlp_utils
from wl_tests import wl_test_init

main = wl_test_init.Wl_Test_Main()

settings_lang_utils = main.settings_global['lang_util_mappings']

SENTENCE_SRP_CYRL = 'Српски језик припада словенској групи језика породице индоевропских језика.[12]'
SENTENCE_SRP_LATN = 'Srpski jezik pripada slovenskoj grupi jezika porodice indoevropskih jezika.[12]'

def test_to_lang_util_code():
    for util_type in settings_lang_utils:
        for util_text in settings_lang_utils[util_type]:
            lang_util_code = wl_nlp_utils.to_lang_util_code(main, util_type, util_text)

            assert lang_util_code == settings_lang_utils[util_type][util_text]

def test_to_lang_util_codes():
    for util_type in settings_lang_utils:
        lang_util_codes = wl_nlp_utils.to_lang_util_codes(main, util_type, settings_lang_utils[util_type].keys())

        assert list(lang_util_codes) == list(settings_lang_utils[util_type].values())

def test_to_lang_util_text():
    for util_type in settings_lang_utils:
        TO_LANG_UTIL_TEXT = {
            util_code: util_text
            for util_text, util_code in settings_lang_utils[util_type].items()
        }

        for util_code in settings_lang_utils[util_type].values():
            util_text = wl_nlp_utils.to_lang_util_text(main, util_type, util_code)

            assert util_text == TO_LANG_UTIL_TEXT[util_code]

def test_to_lang_util_texts():
    for util_type in settings_lang_utils:
        TO_LANG_UTIL_TEXT = {
            util_code: util_text
            for util_text, util_code in settings_lang_utils[util_type].items()
        }

        util_texts = wl_nlp_utils.to_lang_util_texts(main, util_type, settings_lang_utils[util_type].values())

        assert list(util_texts) == list(TO_LANG_UTIL_TEXT.values())

def test_to_sections():
    tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    token_sections = wl_nlp_utils.to_sections(tokens, num_sections = 5)

    assert token_sections == [[1, 2, 3], [4, 5, 6], [7, 8], [9, 10], [11, 12]]

def test_to_sections_unequal():
    tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    token_sections = list(wl_nlp_utils.to_sections_unequal(tokens, section_size = 5))

    assert token_sections == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12]]

def test_split_into_chunks_text():
    text = '\n\n \n 1\n2 \n\n 3 \n \n\n'

    sections_1 = list(wl_nlp_utils.split_into_chunks_text(text, section_size = 1))
    sections_2 = list(wl_nlp_utils.split_into_chunks_text(text, section_size = 2))
    sections_3 = list(wl_nlp_utils.split_into_chunks_text(text, section_size = 3))

    assert sections_1 == ['\n', '\n', ' \n', ' 1\n', '2 \n', '\n', ' 3 \n', ' \n', '\n']
    assert sections_2 == ['\n\n', ' \n 1\n', '2 \n\n', ' 3 \n \n', '\n']
    assert sections_3 == ['\n\n \n', ' 1\n2 \n\n', ' 3 \n \n\n']

def test_srp_cyrl_to_latn():
    tokens_srp_cyrl = SENTENCE_SRP_CYRL.split()

    assert ' '.join(wl_nlp_utils.to_srp_latn(tokens_srp_cyrl)) == SENTENCE_SRP_LATN

def test_srp_latn_to_cyrl():
    tokens_srp_latn = SENTENCE_SRP_LATN.split()

    assert ' '.join(wl_nlp_utils.to_srp_cyrl(tokens_srp_latn)) == SENTENCE_SRP_CYRL

def test_escape_text():
    assert wl_nlp_utils.escape_text('<test test="test">') == '&lt;test test=&quot;test&quot;&gt;'

def test_escape_tokens():
    assert wl_nlp_utils.escape_tokens(['<test test="test">'] * 10) == ['&lt;test test=&quot;test&quot;&gt;'] * 10

def test_html_to_text():
    assert wl_nlp_utils.html_to_text('<test>&lt;test test=&quot;test&quot;&gt;</test>') == '<test test="test">'

if __name__ == '__main__':
    test_to_lang_util_code()
    test_to_lang_util_codes()
    test_to_lang_util_text()
    test_to_lang_util_texts()

    test_to_sections()
    test_to_sections_unequal()
    test_split_into_chunks_text()

    test_srp_cyrl_to_latn()
    test_srp_latn_to_cyrl()

    test_escape_text()
    test_escape_tokens()
    test_html_to_text()
