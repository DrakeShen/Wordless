# ----------------------------------------------------------------------
# Wordless: Tests - Keyword Extractor
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

import random
import re

from wl_dialogs import wl_dialogs_misc
from wl_tests import wl_test_init

import wl_keyword_extractor

main = wl_test_init.Wl_Test_Main()

def test_keyword_extractor():
    print('Start testing module Keyword Extractor... ')

    tests_significance = list(main.settings_global['tests_significance']['keyword_extractor'].keys())
    measures_effect_size = list(main.settings_global['measures_effect_size']['keyword_extractor'].keys())
    len_diff = abs(len(tests_significance) - len(measures_effect_size))

    if len(tests_significance) > len(measures_effect_size):
        measures_effect_size += measures_effect_size * (len_diff // len(measures_effect_size)) + measures_effect_size[: len_diff % len(measures_effect_size)]
    elif len(measures_effect_size) > len(tests_significance):
        tests_significance += tests_significance * (len_diff // len(tests_significance)) + tests_significance[: len_diff % len(tests_significance)]

    files = main.settings_custom['file_area']['files_open']

    for i, (test_significance, measure_effect_size) in enumerate(zip(tests_significance, measures_effect_size)):
        for file in main.settings_custom['file_area']['files_open']:
            file['selected'] = False

        # Single reference file & single observed file
        if i % 4 == 0:
            file_reference, file_observed = random.sample(files, 2)

            main.settings_custom['keyword_extractor']['generation_settings']['ref_files'] = [file_reference['name']]

            file_reference['selected'] = True
            file_observed['selected'] = True
        # Single reference file & multiple observed files
        elif i % 4 == 1:
            file_reference = random.choice(files)

            main.settings_custom['keyword_extractor']['generation_settings']['ref_files'] = [file_reference['name']]

            for file in files:
                file['selected'] = True
        # Multiple reference files & single observed file
        elif i % 4 == 2:
            file_observed = random.choice(files)

            main.settings_custom['keyword_extractor']['generation_settings']['ref_files'] = [
                file['name']
                for file in files
                if file != file_observed
            ]

            for file in files:
                file['selected'] = True
        # Multiple reference files & multiple observed files
        elif i % 4 == 3:
            main.settings_custom['keyword_extractor']['generation_settings']['ref_files'] = [
                file['name']
                for file in random.sample(files, len(files) // 2)
            ]

            for file in main.settings_custom['file_area']['files_open']:
                file['selected'] = True

        files_reference = [
            re.search(r'(?<=\[)[a-z_]+(?=\])', file_name).group()
            for file_name in main.settings_custom['keyword_extractor']['generation_settings']['ref_files']
        ]
        files_observed = [
            re.search(r'(?<=\[)[a-z_]+(?=\])', file['name']).group()
            for file in files
            if (
                file['selected']
                and file['name'] not in main.settings_custom['keyword_extractor']['generation_settings']['ref_files']
            )
        ]

        print(f"Reference files: {', '.join(files_reference)}")
        print(f"Observed files: {', '.join(files_observed)}")
        print(f'Test of Statistical significance: {test_significance}')
        print(f'Measure of effect size: {measure_effect_size}\n')

        wl_keyword_extractor.Wl_Worker_Keyword_Extractor_Table(
            main,
            dialog_progress = wl_dialogs_misc.Wl_Dialog_Progress_Process_Data(main),
            update_gui = update_gui
        ).run()

    main.app.quit()

    print('All pass!')

def update_gui(err_msg, keywords_freq_files, keywords_stats_files):
    assert not err_msg

    assert keywords_freq_files
    assert keywords_stats_files
    assert len(keywords_freq_files) == len(keywords_stats_files)

    for keyword, stats_files in keywords_stats_files.items():
        freq_files = keywords_freq_files[keyword]

        assert len(freq_files) == len(stats_files) + 1 >= 1

        # Keyword
        assert keyword
        # Frequency (observed files)
        assert any([freq_file for freq_file in freq_files[1:-1]])
        # Frequency (total)
        assert freq_files[-1]
        assert freq_files[-1] == sum(freq_files[1:-1])
        # p-value
        for _, p_value, _, _ in stats_files:
            assert 0 <= p_value <= 1
        # Number of Files Found
        assert len([freq for freq in freq_files[1:-1] if freq]) >= 1

if __name__ == '__main__':
    test_keyword_extractor()
