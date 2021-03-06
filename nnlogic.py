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

from context import Context
from sub_table import sub_table
from bindigit import bindigit
from welcome_message import welcome_message

def go():
    """ Main function """
    ctx = Context()

    print (welcome_message)
    ctx.query = input("NNLogic >> ")
    ctx.query = ctx.query.replace(" ", "")
    ctx.query = ctx.query.upper()

    whitelist = ctx.alphabet + "01()*^+'"
    for i in ctx.query:
        passflag = False
        for j in whitelist:
            if i == j:
                passflag = True
                break
        if not passflag:
            print("Error: character {} is not allowed.".format(i))
            return

    rc = ctx.get_variables()
    if rc != 0:
        print ("Error: Too many variables (maximum = 8)")
        return

    nvars = len(ctx.variables)		# Number of variables (bits)
    ncomb = 2 ** nvars				# Number of possible combinations

    for i in ctx.variables:
        print(i, end=" ")
    print()

    for i in range(ncomb):
        localquery = ctx.query
        cnt = 0
        for j in ctx.variables:
            varvalue = bindigit(i, cnt, nvars)
            if varvalue == 1: vv = "1"
            else: vv = "0"
            localquery = localquery.replace(j, vv)
            print(vv, end=" ")
            cnt = cnt+1

        cnt = 0
        while localquery != "1" and localquery != "0":
            for k in sub_table:
                localquery = localquery.replace(k[0], k[1])
            if cnt == 100:
                print("Error: Syntax error")
                return
            cnt = cnt+1

        print(localquery)

go()