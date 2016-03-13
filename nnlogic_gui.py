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

from tkinter import *
from tkinter.scrolledtext import *

from nnlogic2 import go2

class NNLogicGUI:
    def __init__(self, master):
        self.master = master
        master.title("NNLogic GUI")

        go2("AB")

        self.top_label = Label(master, text="NNLogic ver. 0.7", font=("Courier", 20))
        self.top_label.pack()

        self.output_text = ScrolledText(root, height=20, width=100, bg="#88b898")
        self.output_text.pack()
        self.output_text.insert(END, "Line1\nLine2\nLine3")

        self.input_text = ScrolledText(root, height=3, width=100, bg="#aaaaff")
        self.input_text.pack()
        self.input_text.insert(END, "AnoterLine1\nAnoterLine2\n")

        self.greet_button = Button(master, text="Process", command=self.process)
        self.greet_button.pack()

    def process(self):
        print("Welcome to NNLogic GUI!")
        self.output_text.delete("1.0", END)
        self.output_text.insert(INSERT, "Welcome to NNLogic GUI!")
        print(END, INSERT)

root = Tk()
my_gui = NNLogicGUI(root)
root.mainloop()