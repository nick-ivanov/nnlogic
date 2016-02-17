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

class NNLogicGUI:
    def __init__(self, master):
        self.master = master
        master.title("NNLogic GUI")

        # s = Scrollbar(root)
        # T = Text(root)
        #
        # T.focus_set()
        # s.pack(side=RIGHT, fill=Y)
        # T.pack(side=LEFT, fill=Y)
        # s.config(command=T.yview)
        # T.config(yscrollcommand=s.set)
        #
        # for i in range(40):
        #     T.insert(END, "This is line %d\n" % i)

        self.top_label = Label(master, text="NNLogic ver. 0.7", font=("Courier", 20))
        self.top_label.pack()

        output_text = ScrolledText(root, height=20, width=100, bg="#88b898", state=DISABLED)
        output_text.pack()
        output_text.config(state=NORMAL)
        output_text.insert(END, "Line1\nLine2\nLine3")
        output_text.config(state=DISABLED)

        input_text = ScrolledText(root, height=3, width=100, bg="#aaaaff")
        input_text.pack()
        input_text.insert(END, "AnoterLine1\nAnoterLine2\n")

        #
        # self.label = Label(master, text="NNLogic GUI")
        # self.label.grid(row=3, column=0)
        #
        # self.greet_button = Button(master, text="Process", command=self.greet)
        # self.greet_button.grid(row=4, column=0)
        #
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.grid(row=5, column=0)

    def greet(self):
        print("Welcome to NNLogic GUI!")

root = Tk()
my_gui = NNLogicGUI(root)
root.mainloop()