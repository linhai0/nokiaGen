# -*- coding: utf-8 -*-
# /usr/bin/

#listbox scrollbar
from random import randint
from tkinter import *
root = Tk()
root.title("2 Listbox scolling in sync")
root.geometry("400x400")

switch = 1
def scrolllistbox2(event):
    global switch
    if switch == 1:
        listbox2.yview_scroll(int(-4*(event.delta/120)), "units")
def scrolllistbox1(event):
    global switch
    if switch == 1:
        listbox1.yview_scroll(int(-4*(event.delta/120)), "units")

def do_switch():
    global switch
    if switch:
        switch = 0
        label['text'] = "Not in sync"
    else:
        switch = 1
        label['text'] = "In sync"

frame1 = Frame(root)
frame1.pack(expand=1, fill="both")
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
listbox1 = Listbox(frame1)
listbox1.pack(expand=1, fill="both", side="left")
for i in range(100):
    rnd = str(randint(1,100))
    listbox1.insert(END, f"OUR INCOMES day {i}:" + rnd)
# attach listbox to scrollbar
listbox1.config(bg = "yellow", yscrollcommand=scrollbar.set)
listbox1.bind("<MouseWheel>", scrolllistbox2)

listbox2 = Listbox(frame1)
listbox2.pack(expand=1, fill="both", side="left")
for i in range(100):
    rnd = str(randint(1,100))
    listbox2.insert(END, f"THEIR INCOMES day {i}: " + rnd)
listbox2.config(bg="cyan",yscrollcommand=scrollbar.set)
listbox2.bind("<MouseWheel>", scrolllistbox1)
#scrollbar.config(command=listbox.yview)
frame2 = Frame(root)
frame2.pack()
button = Button(frame2, text= "Sync/unsync", command=do_switch)
button.pack()
label = Label(frame2, text = "In sync")
label.pack()
root.mainloop()