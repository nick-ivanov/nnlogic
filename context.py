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

class Context:
    query = ""
    variables = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def add_variable(self, v):
        """ Add a unique variable to the list of variables """
        if len(self.variables) == 8:
            return 1

        for i in self.variables:
            if i == v:
                return 0
        self.variables.append(v)
        return 0

    def get_variables(self):
        """ Get the list of variables """
        for i in self.query:
            for j in self.alphabet:
                if i == j:
                    rc = self.add_variable(j)
                    if rc != 0: return 1
        return 0
