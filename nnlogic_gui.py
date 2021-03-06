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

from tkinter import *
from tkinter.scrolledtext import *
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.messagebox import showerror

from nnlogic2 import go2

class NNLogicGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("NNLogic")

        self.menubar = Menu(self.master)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save", command=self.savefile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        self.editmenu.add_command(label="Paste", command=self.paste)
        self.editmenu.add_command(label="Clear Input", command=self.clear_input)
        self.editmenu.add_command(label="Clear Output", command=self.clear_output)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Quick Tutorial", command=self.help)
        self.helpmenu.add_command(label="About...", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.master.config(menu=self.menubar)

        self.top_label = Label(self.master, text="NNLogic ver. 0.7", font=("Courier", 20))
        self.top_label.pack()

        self.output_text = ScrolledText(root, height=30, width=100, bg="#88b898")
        self.output_text.pack()

        self.input_text = ScrolledText(root, height=3, width=100, bg="#aaaaff")
        self.input_text.pack()

        self.greet_button = Button(master, text="Process", command=self.process)
        self.greet_button.pack()

    def process(self):
        self.output_text.delete("1.0", END)     # So stupid!
        s = self.input_text.get("1.0", END)     # You know what I think... Right?
        self.output_text.insert(INSERT, go2(s))

    def clear_input(self):
        self.input_text.delete("1.0", END)

    def clear_output(self):
        self.output_text.delete("1.0", END)

    def copy(self):
        self.master.clipboard_clear()
        text = self.master.selection_get()
        self.master.clipboard_append(text)

    def cut(self):
        widget = self.master.focus_get()
        if isinstance(widget, Entry):
            if widget.selection_present():
                widget.clipboard_clear()
                widget.clipboard_append(widget.selection_get())
                widget.delete(SEL_FIRST, SEL_LAST)
        else:
            widget.tk.call('tk_textCut', widget._w)

    def paste(self):
        widget = self.master.focus_get()
        widget.tk.call('tk_textPaste', widget._w)

    def openfile(self):
        fname = askopenfilename(filetypes=(("NNLogic Files (*.nnlogic)", "*.nnlogic"),
                                           ("All files", "*.*")))
        if fname:
            try:
                print("Filename: " + fname)
                file = open(fname, "r")
                self.clear_input()
                self.input_text.insert(INSERT, file.read())
                file.close()
            except IOError:
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return

    def savefile(self):
        file = asksaveasfile(mode='w', defaultextension=".nnlogic")
        if file is None:
            return
        text = str(self.input_text.get(1.0, END))
        file.write(text)
        file.close()

    def help(self):
        self.output_text.delete("1.0", END)
        file = open("help.txt", "r")
        self.output_text.insert(INSERT, file.read())

    def about(self):
        self.output_text.delete("1.0", END)
        file = open("about.txt", "r")
        self.output_text.insert(INSERT, file.read())


root = Tk()
my_gui = NNLogicGUI(root)
root.mainloop()