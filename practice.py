
from Tkinter import *

root = Tk()

v = IntVar()
v.set(0)

f0 = LabelFrame(root, text = 'Group1')
f1 = LabelFrame(root, text = 'Group2')
for x in (0, 1, 2):
    Radiobutton(f0, text = 'radiobutton %d' % x, value = x, variable = v).pack()
    Checkbutton(f1, text = 'checkbutton %d' % x).pack()

f0.pack(padx = 5, pady = 5, side = LEFT)
f1.pack(padx = 5, pady = 5, side = LEFT)

root.mainloop()

