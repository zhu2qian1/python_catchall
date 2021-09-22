#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter


root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

# -----

EditBox: tkinter.Entry = tkinter.Entry(width=50)
EditBox.insert(tkinter.END, "Inserted String")
EditBox.pack()

value: str = EditBox.get()

# -----

root.mainloop()
