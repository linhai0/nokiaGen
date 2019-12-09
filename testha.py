# -*- coding: utf-8 -*-
# /usr/bin/

#listbox scrollbar
from random import randint
from tkinter import *
from tkinter.ttk import *
import os
root = Tk()
root.title("REACTOR")
root.geometry("400x400")

keyvar = StringVar()
value = StringVar()
ev = []
global row
row = 0
# is_add = True
def callback(sv, *keys, **kwargs):
    global row
    print(sv.get(), keys, "\n", kwargs)
    if ev[-1][1].get() != "":
        # if len(ev) > 0: pass
        row += 1
        tmpvar = StringVar()
        tmpvar.trace_add("write", callback=lambda name, index, mode, sv1=tmpvar: callback(sv1))
        entry = Entry(root, textvariable=tmpvar)
        entry.grid(row=row, column=0, padx=10, pady=5, sticky="we")
        ev.append((entry, tmpvar))
        print(len(ev))
    elif len(ev) >= 2 and ev[-2][1].get() == "":
        en1, _ = ev.pop()
        en1.destroy()

    # elif len(ev) == 1 and ev[-1][1].get() == "":



def callback01(*args, **kwargs):
    print(args, "---", kwargs)

keyvar.trace_add("write", callback=lambda name, index, mode, sv=keyvar: callback(sv))
# keyvar.trace_add("unset", callback=callback01)
entry_left = Entry( root, textvariable=keyvar)
entry_left.grid(row=0, column=0, padx=10, pady=5, sticky="we")
ev.append((entry_left, keyvar))


root.mainloop()