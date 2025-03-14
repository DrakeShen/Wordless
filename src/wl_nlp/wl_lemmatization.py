# ----------------------------------------------------------------------
# Wordless: NLP - Lemmatization
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

import re

import nltk
from PyQt5.QtCore import QCoreApplication
import spacy

from wl_nlp import wl_matching, wl_nlp_utils, wl_pos_tagging, wl_word_tokenization
from wl_utils import wl_conversion, wl_misc

_tr = QCoreApplication.translate

def wl_lemmatize(
    main, inputs, lang,
    tokenized = _tr('wl_lemmatize', 'No'),
    tagged = _tr('wl_lemmatize', 'No'),
    lemmatizer = 'default'
):
    if inputs and lang in main.settings_global['lemmatizers']:
        lemmas = []

        if lemmatizer == 'default':
            lemmatizer = main.settings_custom['lemmatization']['lemmatizers'][lang]

        wl_nlp_utils.init_word_tokenizers(
            main,
            lang = lang
        )
        wl_nlp_utils.init_lemmatizers(
            main,
            lang = lang,
            lemmatizer = lemmatizer
        )

        section_size = main.settings_custom['files']['misc']['read_files_in_chunks']

        if type(inputs) == str:
            # Input of SudachiPy cannot be more than 49149 BYTES
            if lemmatizer in ['spacy_jpn', 'sudachipy_jpn'] and len(inputs) > 49149 // 4:
                # Around 300 tokens per line 4 characters per token and 4 bytes per character (≈ 49149 / 4 / 4 / 300)
                sections = wl_nlp_utils.split_into_chunks_text(inputs, section_size = 10)
            else:
                sections = wl_nlp_utils.split_into_chunks_text(inputs, section_size = section_size)

            for section in sections:
                lemmas.extend(wl_lemmatize_text(main, section, lang, tokenized, tagged, lemmatizer))
        else:
            # Input of SudachiPy cannot be more than 49149 BYTES
            if lemmatizer in ['spacy_jpn', 'sudachipy_jpn'] and sum([len(token) for token in inputs]) > 49149 // 4:
                # Around 4 characters per token and 4 bytes per character (≈ 49149 / 4 / 4)
                texts = wl_nlp_utils.to_sections_unequal(inputs, section_size = 3000)
            else:
                texts = wl_nlp_utils.to_sections_unequal(inputs, section_size = section_size * 50)

            for tokens in texts:
                lemmas.extend(wl_lemmatize_tokens(main, tokens, lang, tokenized, tagged, lemmatizer))
    else:
        if type(inputs) == str:
            lemmas = wl_word_tokenization.wl_word_tokenize_flat(main, inputs, lang = lang)
        else:
            lemmas = inputs.copy()

    return lemmas

def wl_lemmatize_text(main, text, lang, tokenized, tagged, lemmatizer):
    lemmas = []

    # spaCy
    if lemmatizer.startswith('spacy_'):
        if not lang.startswith('srp_'):
            lang = wl_conversion.remove_lang_code_suffixes(main, lang)

        nlp = main.__dict__[f'spacy_nlp_{lang}']
        doc = nlp(text)

        lemmas = [token.lemma_ for token in doc]
    # English
    elif lemmatizer == 'nltk_wordnet':
        word_net_lemmatizer = nltk.WordNetLemmatizer()

        for token, pos in wl_pos_tagging.wl_pos_tag(
            main, text,
            lang = 'eng_us',
            pos_tagger = 'nltk_perceptron',
            tagset = 'universal'
        ):
            if pos == 'ADJ':
                lemmas.append(word_net_lemmatizer.lemmatize(token, pos = nltk.corpus.wordnet.ADJ))
            elif pos in ['NOUN', 'PROPN']:
                lemmas.append(word_net_lemmatizer.lemmatize(token, pos = nltk.corpus.wordnet.NOUN))
            elif pos == 'ADV':
                lemmas.append(word_net_lemmatizer.lemmatize(token, pos = nltk.corpus.wordnet.ADV))
            elif pos in ['VERB', 'AUX']:
                lemmas.append(word_net_lemmatizer.lemmatize(token, pos = nltk.corpus.wordnet.VERB))
            else:
                lemmas.append(word_net_lemmatizer.lemmatize(token))
    # Japanese
    elif lemmatizer == 'sudachipy_jpn':
        lemmas = [
            token.dictionary_form()
            for token in main.sudachipy_word_tokenizer.tokenize(text)
        ]
    # Russian & Ukrainian
    elif lemmatizer == 'pymorphy2_morphological_analyzer':
        if lang == 'rus':
            morphological_analyzer = main.pymorphy2_morphological_analyzer_rus
        elif lang == 'ukr':
            morphological_analyzer = main.pymorphy2_morphological_analyzer_ukr

        tokens = wl_word_tokenization.wl_word_tokenize_flat(main, text, lang = lang)

        for token in tokens:
            lemmas.append(morphological_analyzer.parse(token)[0].normal_form)
    # Tibetan
    elif lemmatizer == 'botok_bod':
        tokens = main.botok_word_tokenizer.tokenize(text)

        for token in tokens:
            if token.lemma:
                lemmas.append(token.lemma)
            else:
                lemmas.append(token.text)
    # Lemmatization Lists
    elif lemmatizer.startswith('lemmatization_lists_'):
        mapping_lemmas = {}

        lang = wl_conversion.to_iso_639_1(main, lang)
        lang = wl_conversion.remove_lang_code_suffixes(main, lang)

        with open(wl_misc.get_normalized_path(f'lemmatization/Lemmatization Lists/lemmatization-{lang}.txt'), 'r', encoding = 'utf_8_sig') as f:
            for line in f:
                try:
                    lemma, word = line.rstrip().split('\t')

                    mapping_lemmas[word] = lemma
                except ValueError:
                    pass

        tokens = wl_word_tokenization.wl_word_tokenize_flat(main, text, lang = lang)
        lemmas = [mapping_lemmas.get(token, token) for token in tokens]

    # Remove empty lemmas and strip whitespace in tokens
    lemmas = [
        str(lemma).strip()
        for lemma in lemmas
        if str(lemma).strip()
    ]

    return lemmas

def wl_lemmatize_tokens(main, tokens, lang, tokenized, tagged, lemmatizer):
    empty_offsets = []
    lemmas = []

    tokens = [str(token) for token in tokens]

    re_tags = wl_matching.get_re_tags(main, tag_type = 'body')

    if tagged == _tr('wl_lemmatize_tokens', 'Yes'):
        tags = [''.join(re.findall(re_tags, token)) for token in tokens]
        tokens = [re.sub(re_tags, '', token) for token in tokens]
    else:
        tags = [''] * len(tokens)

    # Record empty tokens with their tags
    for i, token in reversed(list(enumerate(tokens))):
        if not token.strip():
            empty_offsets.append(i)

            del tokens[i]
            del tags[i]

    # spaCy
    if 'spacy' in lemmatizer:
        if not lang.startswith('srp_'):
            lang = wl_conversion.remove_lang_code_suffixes(main, lang)

        nlp = main.__dict__[f'spacy_nlp_{lang}']

        if lang != 'jpn':
            doc = spacy.tokens.Doc(nlp.vocab, words = tokens, spaces = [False] * len(tokens))

            for pipe_name in nlp.pipe_names:
                nlp.get_pipe(pipe_name)(doc)
        # The Japanese model do not have a lemmatizer component and Japanese lemmas are taken directly from SudachiPy
        # See: https://github.com/explosion/spaCy/discussions/9983#discussioncomment-1923647
        else:
            doc = nlp(''.join(tokens))

        lemma_tokens = [token.text for token in doc]
        lemmas = [token.lemma_ for token in doc]
    # English
    elif lemmatizer == 'nltk_wordnet':
        word_net_lemmatizer = nltk.WordNetLemmatizer()

        for token, pos in wl_pos_tagging.wl_pos_tag(
            main, tokens,
            lang = 'eng_us',
            pos_tagger = 'nltk_perceptron',
            tagset = 'universal'
        ):
            if pos == 'ADJ':
                lemmas.append(word_net_lemmatizer.lemmatize(token, pos = nltk.corpus.wordnet.ADJ))
            elif pos in ['NOUN', 'PROPN']:
                lemmas.append(word_net_lemmatizer.lemmatize(token, pos = nltk.corpus.wordnet.NOUN))
            elif pos == 'ADV':
                lemmas.append(word_net_lemmatizer.lemmatize(token, pos = nltk.corpus.wordnet.ADV))
            elif pos in ['VERB', 'AUX']:
                lemmas.append(word_net_lemmatizer.lemmatize(token, pos = nltk.corpus.wordnet.VERB))
            else:
                lemmas.append(word_net_lemmatizer.lemmatize(token))

        lemma_tokens = tokens.copy()
    # Japanese
    elif lemmatizer == 'sudachipy_jpn':
        tokens_retokenized = main.sudachipy_word_tokenizer.tokenize(''.join(tokens))

        lemma_tokens = [token.surface() for token in tokens_retokenized]
        lemmas = [token.dictionary_form() for token in tokens_retokenized]
    # Russian & Ukrainian
    elif lemmatizer == 'pymorphy2_morphological_analyzer':
        if lang == 'rus':
            morphological_analyzer = main.pymorphy2_morphological_analyzer_rus
        elif lang == 'ukr':
            morphological_analyzer = main.pymorphy2_morphological_analyzer_ukr

        for token in tokens:
            lemmas.append(morphological_analyzer.parse(token)[0].normal_form)

        lemma_tokens = tokens.copy()
    # Tibetan
    elif lemmatizer == 'botok_bod':
        lemma_tokens = []
        tokens_retokenized = main.botok_word_tokenizer.tokenize(''.join(tokens))

        for token in tokens_retokenized:
            if token.lemma:
                lemmas.append(token.lemma)
            else:
                lemmas.append(token.text)

            lemma_tokens.append(token.text)
    # Lemmatization Lists
    elif 'lemmatization_lists' in lemmatizer:
        mapping_lemmas = {}

        lang = wl_conversion.to_iso_639_1(main, lang)
        lang = wl_conversion.remove_lang_code_suffixes(main, lang)

        with open(wl_misc.get_normalized_path(f'lemmatization/Lemmatization Lists/lemmatization-{lang}.txt'), 'r', encoding = 'utf_8_sig') as f:
            for line in f:
                try:
                    lemma, word = line.rstrip().split('\t')

                    mapping_lemmas[word] = lemma
                except ValueError:
                    pass

        lemma_tokens = tokens.copy()
        lemmas = [mapping_lemmas.get(token, token) for token in tokens]

    # Remove empty lemmas and strip whitespace in tokens
    for i, lemma in reversed(list(enumerate(lemmas))):
        lemma_tokens[i] = lemma_tokens[i].strip()
        lemmas[i] = lemma.strip()

        if not lemmas[i]:
            del lemmas[i]
            del lemma_tokens[i]

    # Make sure that tokenization is not modified during lemmatization
    i_tokens = 0
    i_lemmas = 0

    len_tokens = len(tokens)
    len_lemmas = len(lemmas)

    if len_tokens != len_lemmas:
        tags_modified = []
        lemmas_modified = []

        while i_tokens < len_tokens and i_lemmas < len_lemmas:
            # Different token
            if len(tokens[i_tokens]) != len(lemma_tokens[i_lemmas]):
                tokens_temp = [tokens[i_tokens]]
                tags_temp = [tags[i_tokens]]
                lemma_tokens_temp = [lemma_tokens[i_lemmas]]
                lemmas_temp = [lemmas[i_lemmas]]

                # Align tokens
                while i_tokens < len_tokens - 1 or i_lemmas < len_lemmas - 1:
                    len_tokens_temp = sum([len(token) for token in tokens_temp])
                    len_lemma_tokens_temp = sum([len(token) for token in lemma_tokens_temp])

                    if len_tokens_temp > len_lemma_tokens_temp:
                        lemma_tokens_temp.append(lemma_tokens[i_lemmas + 1])
                        lemmas_temp.append(lemmas[i_lemmas + 1])

                        i_lemmas += 1
                    elif len_tokens_temp < len_lemma_tokens_temp:
                        tokens_temp.append(tokens[i_tokens + 1])
                        tags_temp.append(tags[i_tokens + 1])

                        i_tokens += 1
                    else:
                        # Use lemmas in one-to-one
                        if len(tokens_temp) == len(lemma_tokens_temp):
                            tags_modified.extend(tags_temp)
                            lemmas_modified.extend(lemmas_temp)
                        # Use original tokens in many-to-one or one-to-many
                        else:
                            tags_modified.extend(tags)
                            lemmas_modified.extend(tokens_temp)

                        tokens_temp = []
                        tags_temp = []
                        lemma_tokens_temp = []
                        lemmas_temp = []

                        break

                if tokens_temp:
                    # Use lemmas in one-to-one
                    if len(tokens_temp) == len(lemma_tokens_temp):
                        tags_modified.extend(tags_temp)
                        lemmas_modified.extend(lemmas_temp)
                    # Use original tokens in many-to-one or one-to-many
                    else:
                        tags_modified.extend(tags)
                        lemmas_modified.extend(tokens_temp)
            else:
                tags_modified.extend(tags[i_tokens])
                lemmas_modified.append(lemmas[i_lemmas])

            i_tokens += 1
            i_lemmas += 1

        len_lemmas_modified = len(lemmas_modified)

        if len_tokens < len_lemmas_modified:
            tags = tags_modified[:len_tokens]
            lemmas = lemmas_modified[:len_tokens]
        elif len_tokens > len_lemmas_modified:
            tags = tags_modified + [tags_modified[-1]] * (len_tokens - len_lemmas_modified)
            lemmas = lemmas_modified + [lemmas_modified[-1]] * (len_tokens - len_lemmas_modified)
        else:
            tags = tags_modified.copy()
            lemmas = lemmas_modified.copy()

    # Insert empty lemmas and their tags after alignment of input and output
    for empty_offset in sorted(empty_offsets):
        lemmas.insert(empty_offset, '')
        tags.insert(empty_offset, '')

    return [lemma + tag for lemma, tag in zip(lemmas, tags)]
