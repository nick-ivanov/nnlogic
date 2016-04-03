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

welcome_message = """Nickemu v. 0.7 -- A simple logic expression processor
Copyright (C) 2014-2016 Nick Ivanov
Email: nick@nnbits.org
Distributed under GNU General Public License v. 3
The text of the license is in license.txt file or online:
https://www.gnu.org/licenses/gpl-3.0.html

NNLogic creates a truth table for a logical expression.
An expression can use parentheses and the following elements:
1 - True; 0 - False;
' - NOT (used after an operand); * - AND; + - OR;
^ - XOR (exclusive OR); ^' - XNOR; *' - NAND; +' - NOR;
A, B, C, ... Z - one-character variables
NOTE: NNLogic is case unsensitive

No operand between variables is treated as AND (AB = A*B).
Maximum number of variables is 8.
EXAMPLE 1: (A^B)+'C+(AB)'+D
=========================================================================
"""