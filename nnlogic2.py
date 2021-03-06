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


def go2(q):
    """ Executes query q in a GUI-interface-friendly way """
    ctx = Context()
    ret = ""
    ctx.query = q
    ctx.query = ctx.query.replace(" ", "")
    ctx.query = ctx.query.replace("\n", "")
    ctx.query = ctx.query.upper()

    ret += ("Truth table for: " + ctx.query + "\n")

    whitelist = ctx.alphabet + "01()*^+'"

    for i in ctx.query:
        passflag = False
        for j in whitelist:
            if i == j:
                passflag = True
                break

        if not passflag:
            return "Error: character {} is not allowed.".format(i)

    rc = ctx.get_variables()
    if rc != 0:
        return "Error: Too many variables (maximum = 8)"

    nvars = len(ctx.variables)
    ncomb = 2 ** nvars

    for i in ctx.variables:
        ret += str(i)
        ret += " "

    ret += "\n"

    for i in range(ncomb):
        localquery = ctx.query
        cnt = 0
        for j in ctx.variables:
            varvalue = bindigit(i, cnt, nvars)
            if varvalue == 1: vv = "1"
            else: vv = "0"
            localquery = localquery.replace(j, vv)
            ret += str(vv)
            ret += " "
            cnt = cnt + 1

        cnt = 0
        while localquery != "1" and localquery != "0":
            for k in sub_table:
                localquery = localquery.replace(k[0], k[1])
            if cnt == 100:
                return "Error: Syntax error"
            cnt = cnt + 1

        ret += localquery
        ret += "\n"

    return ret
