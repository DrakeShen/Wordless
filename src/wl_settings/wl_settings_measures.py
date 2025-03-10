# ----------------------------------------------------------------------
# Wordless: Settings - Measures
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

import copy

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from wl_settings import wl_settings
from wl_widgets import wl_boxes, wl_labels, wl_layouts, wl_widgets

# Measures - Dispersion
class Wl_Settings_Dispersion(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['dispersion']
        self.settings_custom = self.main.settings_custom['measures']['dispersion']

        # General
        group_box_general_settings = QGroupBox(self.tr('General Settings'), self)

        (self.label_dispersion_divide,
         self.spin_box_dispersion_number_sections,
         self.label_dispersion_sections) = wl_widgets.wl_widgets_number_sections(self)

        group_box_general_settings.setLayout(wl_layouts.Wl_Layout())
        group_box_general_settings.layout().addWidget(self.label_dispersion_divide, 0, 0)
        group_box_general_settings.layout().addWidget(self.spin_box_dispersion_number_sections, 0, 1)
        group_box_general_settings.layout().addWidget(self.label_dispersion_sections, 0, 2)

        group_box_general_settings.layout().setColumnStretch(3, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(group_box_general_settings, 0, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(1, 1)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        self.spin_box_dispersion_number_sections.setValue(settings['general']['number_sections'])

    def apply_settings(self):
        self.settings_custom['general']['number_sections'] = self.spin_box_dispersion_number_sections.value()

        return True

# Measures - Adjusted Frequency
class Wl_Settings_Adjusted_Freq(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['adjusted_freq']
        self.settings_custom = self.main.settings_custom['measures']['adjusted_freq']

        # General
        group_box_general_settings = QGroupBox(self.tr('General Settings'), self)

        (self.label_adjusted_freq_divide,
         self.spin_box_adjusted_freq_number_sections,
         self.label_adjusted_freq_sections) = wl_widgets.wl_widgets_number_sections(self)
        self.checkbox_use_same_settings_dispersion = QCheckBox(self.tr('Use same settings in "Settings → Measures → Dispersion"'), self)

        self.checkbox_use_same_settings_dispersion.stateChanged.connect(self.use_same_settings_changed)

        group_box_general_settings.setLayout(wl_layouts.Wl_Layout())
        group_box_general_settings.layout().addWidget(self.label_adjusted_freq_divide, 0, 0)
        group_box_general_settings.layout().addWidget(self.spin_box_adjusted_freq_number_sections, 0, 1)
        group_box_general_settings.layout().addWidget(self.label_adjusted_freq_sections, 0, 2)
        group_box_general_settings.layout().addWidget(self.checkbox_use_same_settings_dispersion, 1, 0, 1, 4)

        group_box_general_settings.layout().setColumnStretch(3, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(group_box_general_settings, 0, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(1, 1)

        self.use_same_settings_changed()

    def use_same_settings_changed(self):
        if self.checkbox_use_same_settings_dispersion.isChecked():
            self.spin_box_adjusted_freq_number_sections.setEnabled(False)
        else:
            self.spin_box_adjusted_freq_number_sections.setEnabled(True)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        self.spin_box_adjusted_freq_number_sections.setValue(settings['general']['number_sections'])
        self.checkbox_use_same_settings_dispersion.setChecked(settings['general']['use_same_settings_dispersion'])

    def apply_settings(self):
        self.settings_custom['general']['number_sections'] = self.spin_box_adjusted_freq_number_sections.value()
        self.settings_custom['general']['use_same_settings_dispersion'] = self.checkbox_use_same_settings_dispersion.isChecked()

        return True

# Measures - Statistical Significance
class Wl_Settings_Statistical_Significance(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['statistical_significance']
        self.settings_custom = self.main.settings_custom['measures']['statistical_significance']

        # z-score
        group_box_z_score = QGroupBox(self.tr('z-score'), self)

        (self.label_z_score_direction,
         self.combo_box_z_score_direction) = wl_widgets.wl_widgets_direction_2(self)

        group_box_z_score.setLayout(wl_layouts.Wl_Layout())
        group_box_z_score.layout().addWidget(self.label_z_score_direction, 0, 0)
        group_box_z_score.layout().addWidget(self.combo_box_z_score_direction, 0, 1)

        group_box_z_score.layout().setColumnStretch(2, 1)

        # Student's t-test (2-sample)
        group_box_students_t_test_2_sample = QGroupBox(self.tr("Student's t-test (2-sample)"), self)

        (self.label_students_t_test_2_sample_divide,
         self.spin_box_students_t_test_2_sample_number_sections,
         self.label_students_t_test_2_sample_sections) = wl_widgets.wl_widgets_number_sections(self)

        (self.label_students_t_test_2_sample_use_data,
         self.combo_box_students_t_test_2_sample_use_data) = wl_widgets.wl_widgets_use_data_freq(self)
        self.label_students_t_test_2_sample_variances = QLabel(self.tr('Variances:'), self)
        self.combo_box_students_t_test_2_sample_variances = QComboBox(self)
        self.label_welchs_t_test = wl_labels.Wl_Label_Hint(
            self.tr('''
                <p>* If variances are set to "Unequal", the Welch's t-test will be performed instead.</p>
            '''), self)

        self.combo_box_students_t_test_2_sample_variances.addItems([
            self.tr('Equal'),
            self.tr('Unequal')
        ])

        layout_students_t_test_2_sample_number_sections = wl_layouts.Wl_Layout()
        layout_students_t_test_2_sample_number_sections.addWidget(self.label_students_t_test_2_sample_divide, 0, 0)
        layout_students_t_test_2_sample_number_sections.addWidget(self.spin_box_students_t_test_2_sample_number_sections, 0, 1)
        layout_students_t_test_2_sample_number_sections.addWidget(self.label_students_t_test_2_sample_sections, 0, 2)

        layout_students_t_test_2_sample_number_sections.setColumnStretch(3, 1)

        group_box_students_t_test_2_sample.setLayout(wl_layouts.Wl_Layout())
        group_box_students_t_test_2_sample.layout().addLayout(layout_students_t_test_2_sample_number_sections, 0, 0, 1, 3)
        group_box_students_t_test_2_sample.layout().addWidget(self.label_students_t_test_2_sample_use_data, 1, 0)
        group_box_students_t_test_2_sample.layout().addWidget(self.combo_box_students_t_test_2_sample_use_data, 1, 1)
        group_box_students_t_test_2_sample.layout().addWidget(self.label_students_t_test_2_sample_variances, 2, 0)
        group_box_students_t_test_2_sample.layout().addWidget(self.combo_box_students_t_test_2_sample_variances, 2, 1)
        group_box_students_t_test_2_sample.layout().addWidget(self.label_welchs_t_test, 3, 0, 1, 3)

        group_box_students_t_test_2_sample.layout().setColumnStretch(2, 1)

        # Pearson's Chi-squared Test
        group_box_pearsons_chi_squared_test = QGroupBox(self.tr("Pearson's Chi-squared Test"), self)

        self.checkbox_pearsons_chi_squared_test_apply_correction = QCheckBox(self.tr("Apply Yates's correction for continuity"))

        group_box_pearsons_chi_squared_test.setLayout(wl_layouts.Wl_Layout())
        group_box_pearsons_chi_squared_test.layout().addWidget(self.checkbox_pearsons_chi_squared_test_apply_correction, 0, 0)

        # Fisher's Exact Test
        group_box_fishers_exact_test = QGroupBox(self.tr("Fisher's Exact Test"), self)

        (self.label_fishers_exact_test_direction,
         self.combo_box_fishers_exact_test_direction) = wl_widgets.wl_widgets_direction(self)

        group_box_fishers_exact_test.setLayout(wl_layouts.Wl_Layout())
        group_box_fishers_exact_test.layout().addWidget(self.label_fishers_exact_test_direction, 0, 0)
        group_box_fishers_exact_test.layout().addWidget(self.combo_box_fishers_exact_test_direction, 0, 1)

        group_box_fishers_exact_test.layout().setColumnStretch(2, 1)

        # Mann-Whitney U Test
        group_box_mann_whitney_u_test = QGroupBox(self.tr('Mann-Whitney U Test'), self)

        (self.label_mann_whitney_u_test_divide,
         self.spin_box_mann_whitney_u_test_number_sections,
         self.label_mann_whitney_u_test_sections) = wl_widgets.wl_widgets_number_sections(self)

        (self.label_mann_whitney_u_test_use_data,
         self.combo_box_mann_whitney_u_test_use_data) = wl_widgets.wl_widgets_use_data_freq(self)
        (self.label_mann_whitney_u_test_direction,
         self.combo_box_mann_whitney_u_test_direction) = wl_widgets.wl_widgets_direction(self)
        self.checkbox_mann_whitney_u_test_apply_correction = QCheckBox(self.tr('Apply continuity correction'), self)

        layout_mann_whitney_u_test_number_sections = wl_layouts.Wl_Layout()
        layout_mann_whitney_u_test_number_sections.addWidget(self.label_mann_whitney_u_test_divide, 0, 0)
        layout_mann_whitney_u_test_number_sections.addWidget(self.spin_box_mann_whitney_u_test_number_sections, 0, 1)
        layout_mann_whitney_u_test_number_sections.addWidget(self.label_mann_whitney_u_test_sections, 0, 2)

        layout_mann_whitney_u_test_number_sections.setColumnStretch(3, 1)

        group_box_mann_whitney_u_test.setLayout(wl_layouts.Wl_Layout())
        group_box_mann_whitney_u_test.layout().addLayout(layout_mann_whitney_u_test_number_sections, 0, 0, 1, 3)
        group_box_mann_whitney_u_test.layout().addWidget(self.label_mann_whitney_u_test_use_data, 1, 0)
        group_box_mann_whitney_u_test.layout().addWidget(self.combo_box_mann_whitney_u_test_use_data, 1, 1)
        group_box_mann_whitney_u_test.layout().addWidget(self.label_mann_whitney_u_test_direction, 2, 0)
        group_box_mann_whitney_u_test.layout().addWidget(self.combo_box_mann_whitney_u_test_direction, 2, 1)
        group_box_mann_whitney_u_test.layout().addWidget(self.checkbox_mann_whitney_u_test_apply_correction, 3, 0, 1, 3)

        group_box_mann_whitney_u_test.layout().setColumnStretch(3, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(group_box_z_score, 0, 0)
        self.layout().addWidget(group_box_students_t_test_2_sample, 1, 0)
        self.layout().addWidget(group_box_pearsons_chi_squared_test, 2, 0)
        self.layout().addWidget(group_box_fishers_exact_test, 3, 0)
        self.layout().addWidget(group_box_mann_whitney_u_test, 4, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(5, 1)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        self.combo_box_z_score_direction.setCurrentText(settings['z_score']['direction'])

        self.spin_box_students_t_test_2_sample_number_sections.setValue(settings['students_t_test_2_sample']['number_sections'])
        self.combo_box_students_t_test_2_sample_use_data.setCurrentText(settings['students_t_test_2_sample']['use_data'])
        self.combo_box_students_t_test_2_sample_variances.setCurrentText(settings['students_t_test_2_sample']['variances'])

        self.checkbox_pearsons_chi_squared_test_apply_correction.setChecked(settings['pearsons_chi_squared_test']['apply_correction'])

        self.combo_box_fishers_exact_test_direction.setCurrentText(settings['fishers_exact_test']['direction'])

        self.spin_box_mann_whitney_u_test_number_sections.setValue(settings['mann_whitney_u_test']['number_sections'])
        self.combo_box_mann_whitney_u_test_use_data.setCurrentText(settings['mann_whitney_u_test']['use_data'])
        self.combo_box_mann_whitney_u_test_direction.setCurrentText(settings['mann_whitney_u_test']['direction'])
        self.checkbox_mann_whitney_u_test_apply_correction.setChecked(settings['mann_whitney_u_test']['apply_correction'])

    def apply_settings(self):
        self.settings_custom['z_score']['direction'] = self.combo_box_z_score_direction.currentText()

        self.settings_custom['students_t_test_2_sample']['number_sections'] = self.spin_box_students_t_test_2_sample_number_sections.value()
        self.settings_custom['students_t_test_2_sample']['use_data'] = self.combo_box_students_t_test_2_sample_use_data.currentText()
        self.settings_custom['students_t_test_2_sample']['variances'] = self.combo_box_students_t_test_2_sample_variances.currentText()

        self.settings_custom['pearsons_chi_squared_test']['apply_correction'] = self.checkbox_pearsons_chi_squared_test_apply_correction.isChecked()

        self.settings_custom['fishers_exact_test']['direction'] = self.combo_box_fishers_exact_test_direction.currentText()

        self.settings_custom['mann_whitney_u_test']['number_sections'] = self.spin_box_mann_whitney_u_test_number_sections.value()
        self.settings_custom['mann_whitney_u_test']['use_data'] = self.combo_box_mann_whitney_u_test_use_data.currentText()
        self.settings_custom['mann_whitney_u_test']['direction'] = self.combo_box_mann_whitney_u_test_direction.currentText()
        self.settings_custom['mann_whitney_u_test']['apply_correction'] = self.checkbox_mann_whitney_u_test_apply_correction.isChecked()

        return True

# Measures - Effect Size
class Wl_Settings_Effect_Size(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['effect_size']
        self.settings_custom = self.main.settings_custom['measures']['effect_size']

        # Kilgarriff's Ratio
        group_box_kilgarriffs_ratio = QGroupBox(self.tr("Kilgarriff's Ratio"), self)

        self.label_kilgarriffs_ratio_smoothing_param = QLabel(self.tr('Smoothing Parameter:'), self)
        self.spin_box_kilgarriffs_ratio_smoothing_param = wl_boxes.Wl_Double_Spin_Box(self)

        self.spin_box_kilgarriffs_ratio_smoothing_param.setRange(0.01, 10000)

        group_box_kilgarriffs_ratio.setLayout(wl_layouts.Wl_Layout())
        group_box_kilgarriffs_ratio.layout().addWidget(self.label_kilgarriffs_ratio_smoothing_param, 0, 0)
        group_box_kilgarriffs_ratio.layout().addWidget(self.spin_box_kilgarriffs_ratio_smoothing_param, 0, 1)

        group_box_kilgarriffs_ratio.layout().setColumnStretch(2, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(group_box_kilgarriffs_ratio, 0, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(1, 1)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        self.spin_box_kilgarriffs_ratio_smoothing_param.setValue(settings['kilgarriffs_ratio']['smoothing_param'])

    def apply_settings(self):
        self.settings_custom['kilgarriffs_ratio']['smoothing_param'] = self.spin_box_kilgarriffs_ratio_smoothing_param.value()

        return True
