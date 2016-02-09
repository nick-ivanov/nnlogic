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


class ScrollText:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        self.textPad(frame)
        return

    def textPad(self, frame):
        textPad = Frame(frame)
        self.text = Text(textPad, height=50, width=90)

        scroll = Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)

        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        textPad.pack(side=TOP)
        return



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

        label = Label(master, text="NNLogic ver. 0.7", font=("Courier", 20))
        label.pack()

        T2 = ScrolledText(root, height=20, width=100, bg="#88b898")
        T2.pack()
        T2.insert(END, "Line1\nLine2\nLine3")

        T1 = ScrolledText(root, height=3, width=100, bg="#aaaaff")
        T1.pack()
        T1.insert(END, "AnoterLine1\nAnoterLine2\n")

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