#!/usr/bin/env python
import Tkinter as Tk

root = Tk()

buff = StringVar()
buff.set("")

label = Label(root, textvariable = buff)
label.pack()
