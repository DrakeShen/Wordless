# ----------------------------------------------------------------------
# Wordless: Tests - Measures - Miscellaneous
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

from wl_tests import wl_test_init
from wl_measures import wl_measures_misc

main = wl_test_init.Wl_Test_Main()

def test_modes():
    modes = wl_measures_misc.modes([1, 3, 3, 3, 2, 2, 1, 2, 5, 4])

    print(f'Modes: {modes}')

    assert modes == [2, 3]

if __name__ == '__main__':
    test_modes()
