__author__ = "Linhai"
# -*- encoding: utf8 -*-

from tkinter import *
from tkinter.messagebox import *
# from tkinter.dialog import *
from tkinter.filedialog import *
import os
from tkinter.font import *


root = Tk()
root.geometry("800x500+100+100")
root.title("Linhai Node")

font_type = "Consolas"
font_fav = Font(root, font=((font_type, 20, NORMAL)))

def author():
    showinfo("Author", "）——）——）——）——）——）——）——")


def about():
    showinfo("About", "）——）——）——）——）——）——）——")

filename = ""
def open_and_save():
    global filename
    filename = askopenfile(defaultextension=".text")
    if filename is "":
        filename = None
    else:
        root.title("FileName:" + os.path.basename(filename))
        textPad.delete(1.0, END)

menubar = Menu(root) # 生成
root.config(menu = menubar) # 加上

# 建立子菜单
file_menu = Menu(menubar) # 生成
file_menu.add_command(label="New file", accelerator="Ctrl + N")
file_menu.add_command(label="Open file", accelerator="Ctrl + O")
file_menu.add_command(label="Save file", accelerator="Ctrl + S")
file_menu.add_command(label="Save file as", accelerator="Ctrl + Shift + S")

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
short_button = Button(toolbar, text="Open", relief=RAISED)
short_button.pack(side="left", padx=5, pady=3)

short_button01 = Button(toolbar, text="Save")
short_button01.pack(side="left", padx=10, pady=6)
toolbar.pack(expand=NO, fill=X)

statusbar = Label(root, text="LN20", bd=1, relief=RIDGE, anchor='se')
statusbar.pack(side=BOTTOM, fill=X)

# line number and text
# input_text = Text(root, width=2, bg="black")
# input_text.pack(side="left", fill=Y)

ln_label = Label(root, width=2, bg="antique white")
ln_label.pack(side="left", fill="y")


textPad = Text(root, undo=True, bg="antique white", font=font_fav)
textPad.pack(expand=YES, fill=BOTH)

scroll = Scrollbar(textPad, relief=FLAT)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side="right", fill='y')

if __name__ == '__main__':
    root.mainloop()
