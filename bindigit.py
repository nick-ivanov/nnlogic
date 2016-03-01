# NNLogic -- truth table creator for logic expressions
# Copyright (C) 2014-2016 Nick Ivanov <nick@nnbits.org>
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

def bindigit(n, p, bits):
    """ Returns binary digit of number n in position p """
    MAX_DIGIT_LENGTH = 54
    cp = 0 	# Current position
    real_p = bits - p - 1
    while(cp < MAX_DIGIT_LENGTH):		# Assume our number is less than 27 bits
        if cp == real_p:
            return n%2 	# Return remainder of division on 2 at current position
        n = n // 2 		# Integer division
        cp = cp + 1

    return -1