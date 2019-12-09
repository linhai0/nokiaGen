__author__ = "Linhai"
# -*- encoding: utf8 -*-

from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
# from tkinter.dialog import *
from tkinter.filedialog import *
import os
from tkinter.font import *


root = Tk()
root.geometry("800x500+100+100")
# root.geometry("800x500+700+400")
root.title("Linhai Node")

font_type = "Consolas"
font_fav = Font(root, font=((font_type, 16, NORMAL)))

def author():
    showinfo("Author", "）——）——）——）——）——）——）——")


def about():
    showinfo("About", "）——）——）——）——）——）——）——")

filename = ""
def open_and_save():
    global filename
    filename = askopenfile(defaultextension='txt')
    full_filename = filename.name
    if filename is "":
        filename = None
    else:
        print("FileName" + os.path.basename(full_filename))
        root.title(full_filename)
        textPad.delete(1.0, END)
        with open(full_filename, 'r', encoding='utf-8') as f:
            s1 = f.read()
            print(s1)
            textPad.insert(1.0, s1)

            # textPad.insert(1.0, "\n----\n")

def save_file_as():
    f = asksaveasfilename(initialfile="unTitle.txt", defaultextension="*.txt")
    global filename
    filename = f

    msg = textPad.get(1.0, END)
    with open(filename, 'w', encoding='utf-8') as fff:
        fff.write(msg)
    root.title("FileName:" + os.path.basename(filename))

def cut_content():
    textPad.event_generate("<<Cut>>")
    textPad.event_generate("<<Copy Paste Redo ...Undo>>")


def selectAll():
    textPad.tag_add('sel', '1.0', END)

def search():
    top_search = Toplevel(root)
    top_search.geometry('300x30+200+250')
    lable1 = Label(top_search, text='Find')
    lable1.grid(row=0, column=0, padx=5)
    entry1 = Entry(top_search, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = Button(top_search, text="search")
    button1.grid(row=0, column=2)




def save_file():
    global filename
    try:
        with open(filename, "w", encoding="utf-8") as f:
            msg = textPad.get(1.0, END)
            f.write(msg)
    except:
        save_file_as()


menubar = Menu(root) # 生成
root.config(menu = menubar) # 加上

# 建立子菜单
file_menu = Menu(menubar) # 生成
file_menu.add_command(label="New file", accelerator="Ctrl + N")
file_menu.add_command(label="Open file", accelerator="Ctrl + O", command=open_and_save)
file_menu.add_command(label="Save file", accelerator="Ctrl + S", command=save_file)
file_menu.add_command(label="Save file as", accelerator="Ctrl + Shift + S", command=save_file_as)

menubar.add_cascade(label="File", menu=file_menu) # 加上

edit_menu = Menu(menubar)
edit_menu.add_command(label="Cancel", accelerator="Ctrl + Z")
edit_menu.add_command(label="Redo", accelerator="Ctrl + Z")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl + X")
edit_menu.add_command(label="Copy", accelerator="Ctrl + C")
edit_menu.add_command(label="Paste", accelerator="Ctrl + V")
edit_menu.add_separator()
edit_menu.add_command(label="Search", accelerator="Ctrl + F")
edit_menu.add_command(label="Select All", accelerator="Ctrl + A")
menubar.add_cascade(label="Edit", menu=edit_menu)

about_menu = Menu(menubar)
about_menu.add_command(label="Author", command=author)
about_menu.add_command(label="Copyright", command=about)
menubar.add_cascade(label="About", menu=about_menu, )

toolbar = Frame(root, height=25, bg="light sea green")
short_button = Button(toolbar, text="Open", relief=RAISED, command=open_and_save)
short_button.pack(side="left", padx=5, pady=3)

short_button01 = Button(toolbar, text="Save")
short_button01.pack(side="left", padx=10, pady=6)
toolbar.pack(expand=NO, fill=X)

statusbar = tk.Label(root, text="LN20", bd=1, relief=RIDGE, anchor='se')
# statusbar.pack(side=BOTTOM, fill=X)
statusbar.place(relx=0, rely=0.95, relwidth=0.0975, relheight=0.05)


# line number and text
# input_text = Text(root, width=2, bg="black")
# input_text.pack(side="left", fill=Y)

ln_label = Label(root, bg="antique white")
ln_label.place(relx=0, rely=0.1, relwidth=0.025, relheight=0.85)
# ln_label.pack(side="left", fill="y")

# TODO add New Menu

textPad = Text(root, undo=True, bg="antique white", state='disabled', relief=FLAT, font=font_fav, padx=1, pady=2, highlightbackground="white")

scroll = Scrollbar(root, relief=RIDGE, bg='red', )
textPad.config(yscrollcommand=scroll.set, state='normal')
scroll.config(command=textPad.yview)
scroll.place(relx=0.975, rely=0.1, relwidth=0.025, relheight=0.85)
# scroll.pack(side="right", fill=Y, padx=0)
textPad.place(relx=0.025, rely=0.1, relwidth=0.95, relheight=0.85)
# textPad.pack(expand=True, fill=BOTH, side=LEFT)


cv = Canvas(root,bg = 'white')

font_size = 16

def wheel(event):
    global font_size
    print(event.delta)

    if event.delta == -1:
        font_size += 2
        textPad['font'] = "Arial " + str(font_size)
    else:
        font_size -= 2
        textPad['font'] = "Arial " + str(font_size)

textPad.bind("<Control-MouseWheel>", wheel)



if __name__ == '__main__':
    root.mainloop()
