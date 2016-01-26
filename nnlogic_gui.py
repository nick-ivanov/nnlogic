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

class NNLogicGUI:
    def __init__(self, master):
        self.master = master
        master.title("NNLogic GUI")

        frame = Frame(master, bd=2, relief=SUNKEN)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        text = Text(frame, bg="blue", wrap=WORD, yscrollcommand=scrollbar.set)
        text.pack()



        text.insert(END, "Line1\nLine2\nLine3")
        scrollbar.config(command=text.yview)

        T = Text(root, height=2, width=100, bg="green")
        T.pack()
        T.insert(END, "Line1\nLine2\nLine3")

        T1 = Text(root, height=2, width=100, bg="red")
        T1.pack()
        T1.insert(END, "AnoterLine1\nAnoterLine2\n")

        self.label = Label(master, text="NNLogic GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Process", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Welcome to NNLogic GUI!")

root = Tk()
my_gui = NNLogicGUI(root)
root.mainloop()