# NNLogic -- truth table creator for logic expressions
# Copyright (C) 2014-2016 Nick Ivanov <nnrowan@gmail.com>
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

sub_table = [
    ["(1)", "1"], ["(0)", "0"], ["1'", "0"], ["0'", "1"],  # Parenterses and NOT
    ["1*1", "1"], ["0*1", "0"], ["1*0", "0"], ["0*0", "0"],  # AND
    ["11", "1"], ["01", "0"], ["10", "0"], ["00", "0"],  # Reduced form of AND
    ["1+1", "1"], ["0+1", "1"], ["1+0", "1"], ["0+0", "0"],  # OR
    ["1^1", "0"], ["0^1", "1"], ["1^0", "1"], ["0^0", "0"],  # XOR
    ["1^'1", "1"], ["0^'1", "0"], ["1^'0", "0"], ["0^'0", "1"],  # XNOR
    ["1*'1", "0"], ["0*'1", "1"], ["1*'0", "1"], ["0*'0", "0"],  # NAND
    ["1+'1", "0"], ["0+'1", "0"], ["1+'0", "0"], ["0+'0", "1"],  # NOR
]