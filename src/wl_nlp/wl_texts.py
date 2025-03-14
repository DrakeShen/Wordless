# ----------------------------------------------------------------------
# Wordless: NLP - Texts
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

import os
import re

import bs4
from PyQt5.QtCore import QCoreApplication

from wl_nlp import wl_matching, wl_sentence_tokenization, wl_word_tokenization
from wl_utils import wl_misc

_tr = QCoreApplication.translate

class Wl_Token(str):
    def __new__(cls, string, *args, **kwargs):
        return super().__new__(cls, string)

    def __init__(self, string, boundary = '', sentence_ending = False):
        self.boundary = boundary
        self.sentence_ending = sentence_ending

class Wl_Text_Blank:
    pass

class Wl_Text:
    def __init__(self, main, file):
        self.main = main
        self.lang = file['lang']
        self.tokenized = file['tokenized']
        self.tagged = file['tagged']

        self.offsets_paras = []
        self.offsets_sentences = []

        self.tokens_multilevel = []
        self.tokens_flat = []
        self.tags = []

        file_ext = os.path.splitext(file['path'])[1].lower()
        re_tags = re.compile(wl_matching.get_re_tags(self.main, tag_type = 'body'))
        re_tags_start = re.compile(fr"\s*({wl_matching.get_re_tags(self.main, tag_type = 'body')})")

        if (
            file_ext == '.txt'
            # Treat untagged XML files as untagged text files
            or file_ext == '.xml' and not self.tagged
        ):
            with open(file['path'], 'r', encoding = file['encoding'], errors = 'replace') as f:
                text = f.read()

            # Untokenized & Untagged
            if not self.tokenized and not self.tagged:
                tokens = wl_word_tokenization.wl_word_tokenize(self.main, text, lang = self.lang)

                self.tokens_multilevel.extend(tokens)
            # Untokenized & Tagged
            elif not self.tokenized and self.tagged:
                # Replace all tags with a whitespace to ensure no words run together
                text_no_tags = re.sub(re_tags, ' ', text)

                tokens = wl_word_tokenization.wl_word_tokenize(self.main, text_no_tags, lang = self.lang)

                self.tokens_multilevel.extend(tokens)

                # Check if the first token in the text is a tag
                if re.match(re_tags_start, text):
                    # Check if the first paragraph is empty
                    if not self.tokens_multilevel[0]:
                        self.tokens_multilevel[0].append([])

                    self.tokens_multilevel[0][0].insert(0, '')
                    self.tags.append([])

                # Extract tags
                tag_end = 0

                for tag in re.finditer(re_tags, text):
                    self.add_tags_tokenization(text[tag_end:tag.start()])
                    self.tags[-1].append(tag.group())

                    tag_end = tag.end()

                # The last part of the text
                if (text := text[tag_end:]):
                    self.add_tags_tokenization(text)
            # Tokenized & Untagged
            elif self.tokenized and not self.tagged:
                for para in text.splitlines():
                    self.tokens_multilevel.append([])

                    if para:
                        for sentence in wl_sentence_tokenization.wl_sentence_split(self.main, para):
                            self.tokens_multilevel[-1].append(sentence.split())
            # Tokenized & Tagged
            elif self.tokenized and self.tagged:
                for i, para in enumerate(text.splitlines()):
                    self.tokens_multilevel.append([])

                    if para:
                        # Replace all tags with a whitespace to ensure no words run together
                        text_no_tags = re.sub(re_tags, ' ', para)

                        for sentence in wl_sentence_tokenization.wl_sentence_split(self.main, text_no_tags):
                            self.tokens_multilevel[-1].append(sentence.split())

                        # Check if the first token in the text is a tag
                        if i == 0 and re.match(re_tags_start, para):
                            # Check if the first paragraph is empty
                            if not self.tokens_multilevel[0]:
                                self.tokens_multilevel[0].append([])

                            self.tokens_multilevel[0][0].insert(0, '')

                            self.tags.append([])

                        # Extract tags
                        tag_end = 0

                        for tag in re.finditer(re_tags, para):
                            self.add_tags_splitting(para[tag_end:tag.start()])
                            self.tags[-1].append(tag.group())

                            tag_end = tag.end()

                        # The last part of the text
                        if (para := para[tag_end:]):
                            self.add_tags_splitting(para)

            # Add empty tags for untagged files
            if not self.tagged:
                self.tags.extend([[] for _ in wl_misc.flatten_list(self.tokens_multilevel)])
        elif file_ext == '.xml':
            # Treat untagged XML files as untagged TXT files
            if self.tagged:
                tags_para = []
                tags_sentence = []
                tags_word = []

                for _, level, opening_tag, _ in self.main.settings_custom['tags']['tags_xml']:
                    if level == _tr('Wl_Text', 'Paragraph'):
                        tags_para.append(opening_tag[1:-1])
                    elif level == _tr('Wl_Text', 'Sentence'):
                        tags_sentence.append(opening_tag[1:-1])
                    elif level == _tr('Wl_Text', 'Word'):
                        tags_word.append(opening_tag[1:-1])

                css_para = ','.join(tags_para)
                css_sentence = ','.join(tags_sentence)
                css_word = ','.join(tags_word)

                with open(file['path'], 'r', encoding = file['encoding'], errors = 'replace') as f:
                    soup = bs4.BeautifulSoup(f.read(), features = 'lxml-xml')

                if (
                    (css_para and tags_sentence and tags_word)
                    and (soup.select_one(css_para) and soup.select_one(css_sentence) and soup.select_one(css_word))
                ):
                    for para in soup.select(css_para):
                        self.tokens_multilevel.append([])

                        for sentence in para.select(css_sentence):
                            self.tokens_multilevel[-1].append([])

                            for word in sentence.select(css_word):
                                self.tokens_multilevel[-1][-1].append(word.get_text().strip())
                # XML tags unfound or unspecified
                else:
                    text = soup.get_text()
                    tokens = wl_word_tokenization.wl_word_tokenize(self.main, text, lang = self.lang)

                    self.tokens_multilevel.extend(tokens)

            # Add empty tags
            self.tags.extend([[] for _ in wl_misc.flatten_list(self.tokens_multilevel)])

        # Paragraph and sentence offsets
        for para in self.tokens_multilevel:
            self.offsets_paras.append(len(self.tokens_flat))

            for sentence in para:
                self.offsets_sentences.append(len(self.tokens_flat))

                self.tokens_flat.extend(sentence)

        # Remove whitespace around all tags
        self.tags = [[tag.strip() for tag in tags] for tags in self.tags]

        # Remove Wl_Main object from the text since it cannot be pickled
        del self.main

    def add_tags_tokenization(self, text):
        if (text := text.strip()):
            tokens = wl_word_tokenization.wl_word_tokenize_flat(
                self.main, text,
                lang = self.lang
            )

            self.tags.extend([[] for _ in tokens])

    def add_tags_splitting(self, text):
        if (text := text.strip()):
            tokens = text.split()

            self.tags.extend([[] for _ in tokens])

class Wl_Text_Ref:
    def __init__(self, main, file):
        self.main = main
        self.lang = file['lang']
        self.tokenized = file['tokenized']
        self.tagged = file['tagged']

        self.tokens_multilevel = [[]]

        file_ext = os.path.splitext(file['path'])[1].lower()

        if (
            file_ext == '.txt'
            # Treat untagged XML files as untagged text files
            or file_ext == '.xml' and not self.tagged
        ):
            with open(file['path'], 'r', encoding = file['encoding'], errors = 'replace') as f:
                text = f.read()

            re_tags = re.compile(wl_matching.get_re_tags(self.main, tag_type = 'body'))

            # Untokenized & Untagged
            if not self.tokenized and not self.tagged:
                self.tokens_multilevel = wl_word_tokenization.wl_word_tokenize(self.main, text, lang = self.lang)
            # Untokenized & Tagged
            elif not self.tokenized and self.tagged:
                # Replace all tags with a whitespace to ensure no words run together
                text_no_tags = re.sub(re_tags, ' ', text)

                self.tokens_multilevel = wl_word_tokenization.wl_word_tokenize(self.main, text_no_tags, lang = self.lang)
            # Tokenized & Untagged
            elif self.tokenized and not self.tagged:
                self.tokens_multilevel[0].append(text.split())
            # Tokenized & Tagged
            elif self.tokenized and self.tagged:
                # Replace all tags with a whitespace to ensure no words run together
                text_no_tags = re.sub(re_tags, ' ', text)

                self.tokens_multilevel[0].append(text.split())
        elif file_ext == '.xml':
            if self.tagged and self.tokenized:
                tags_word = []

                for _, level, opening_tag, _ in self.main.settings_custom['tags']['tags_xml']:
                    if level == _tr('Wl_Text', 'Word'):
                        tags_word.append(opening_tag[1:-1])

                with open(file['path'], 'r', encoding = file['encoding'], errors = 'replace') as f:
                    soup = bs4.BeautifulSoup(f.read(), features = 'lxml-xml')

                css_word = ','.join(tags_word)

                if css_word:
                    for word in soup.select(css_word):
                        self.tokens_multilevel[0].append(word.get_text())

                # XML tags unfound or unspecified
                if not css_word or not self.tokens_multilevel[0]:
                    text = soup.get_text()

                    self.tokens_multilevel = wl_word_tokenization.wl_word_tokenize(self.main, text, lang = self.lang)
            elif self.tagged and not self.tokenized:
                text = soup.get_text()

                self.tokens_multilevel = wl_word_tokenization.wl_word_tokenize(self.main, text, lang = self.lang)

        # No need to calculate paragraph and sentence offsets
        self.offsets_paras = [0]
        self.offsets_sentences = [0]

        # Remove whitespace around tokens and empty tokens
        self.tokens_multilevel[0][0] = [
            token_clean
            for token in self.tokens_multilevel[0][0]
            if (token_clean := token.strip())
        ]
        self.tokens_flat = list(wl_misc.flatten_list(self.tokens_multilevel))

        # No need to extract tags
        self.tags = [[] for _ in self.tokens_flat]

        # Remove Wl_Main object from the text since it cannot be pickled
        del self.main
