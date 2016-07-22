# NNLogic v. 0.3 -- A simple logic expression processor
# Copyright (C) 2014-2016 Nick Ivanov
# Email: nnrowan@gmail.com
# Distributed under GNU General Public License v. 3
# The text of the license is in license.txt file or online:
# https://www.gnu.org/licenses/gpl-3.0.html

class context:
	query = ""
	variables = []
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	def add_variable(self, v):
		""" Add a unique variable to the list of variables """
		if len(self.variables) == 8: return 1

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

def bindigit(n,p, bits):
	""" Returns binary digit of number n in position p """
	cp = 0 	# Current position
	real_p = bits - p - 1
	while(cp < 27):		# Assume our number is less than 27 bits
		if cp == real_p:
			return n%2 	# Return remainder of division on 2 at current position
		n = n // 2 		# Integer division
		cp = cp + 1

	return -1

def go():
	""" Main function """
	sub_table = [
		["(1)", "1"], ["(0)", "0"], ["1'", "0"], ["0'", "1"],			# Parenterses and NOT
		["1*1", "1"], ["0*1", "0"], ["1*0", "0"], ["0*0", "0"],			# AND
		["11", "1"], ["01", "0"], ["10", "0"], ["00", "0"],				# Reduced form of AND
		["1+1", "1"], ["0+1", "1"], ["1+0", "1"], ["0+0", "0"],			# OR
		["1^1", "0"], ["0^1", "1"], ["1^0", "1"], ["0^0", "0"],			# XOR
		["1^'1", "1"], ["0^'1", "0"], ["1^'0", "0"], ["0^'0", "1"],		# XNOR
		["1*'1", "0"], ["0*'1", "1"], ["1*'0", "1"], ["0*'0", "0"],		# NAND
		["1+'1", "0"], ["0+'1", "0"], ["1+'0", "0"], ["0+'0", "1"],		# NOR
	]

	ctx = context()

	hello = """Nickemu v. 0.3 -- A simple logic expression processor
Copyright (C) 2014-2016 Nick Ivanov
Email: nnrowan@gmail.com
Distributed under GNU General Public License v. 3
The text of the license is in license.txt file or online:
https://www.gnu.org/licenses/gpl-3.0.html

Nickemu creates a truth table for a logical expression.
An expression can use parentheses and the following elements:
1 - True; 0 - False;
' - NOT (used after an operand); * - AND; + - OR;
^ - XOR (exclusive OR); ^' - XNOR; *' - NAND; +' - NOR;
A, B, C, ... Z - one-character variables
NOTE: Nickemu is case unsensitive

No operand between variables is treated as AND (AB = A*B).
Maximum number of variables is 8.
EXAMPLE 1: (A^B)+'C+(AB)'+D
=========================================================================
"""
	
	print (hello)
	ctx.query = input("NICKEMU >> ")
	ctx.query = ctx.query.replace(" ", "")
	ctx.query = ctx.query.upper()

	whitelist = ctx.alphabet + "01()*^+'"
	for i in ctx.query:
		passflag = False
		for j in whitelist:
			if i == j:
				passflag = True
				break
		if passflag == False:
			print("Error: character {} is not allowed.".format(i))
			return

	rc = ctx.get_variables()
	if (rc != 0):
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
		while (localquery != "1" and localquery != "0"):
			for k in sub_table:
				localquery = localquery.replace(k[0], k[1])
			if cnt == 100:
				print ("Error: Syntax error")
				return
			cnt = cnt+1

		print (localquery)

go()