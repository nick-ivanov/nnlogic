# context.py -- class Context
# NNLogic v. 0.3 -- A simple logic expression processor
# Copyright (C) 2014-2016 Nick Ivanov
# Email: nnrowan@gmail.com
# Distributed under GNU General Public License v. 3
# The text of the license is in license.txt file or online:
# https://www.gnu.org/licenses/gpl-3.0.html

class Context:
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