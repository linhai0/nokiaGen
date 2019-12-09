# -*- coding: utf-8 -*-
# /usr/bin/

__author__ = "Linhai"
# from tkinter.tix import *
import urllib3.connection
from urllib import request

from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
# from tkinter.dialog import *
from tkinter.filedialog import *
import os
from tkinter.font import *
import tkinter.ttk as ttk
from tkinter.ttk import *


def tab_header(tab1:Frame, header):
    
    pass

def tab_param(tab2:Frame, param):
    pass

def tab_body(tab3:Frame, body, header):
    pass


class TabControl(object):
    
    def __init__(self, base_frame):
        self.base_frame = base_frame
        self.tab1 = self.create_tab("第一页", 0)
        self.tab2 = self.create_tab("第二页", 1)
        self.tab3 = self.create_tab("第三页", 2)
        self.padx = 30
        self.pady = 6
        # header = StringVar()
        self.header = {}
        self.param = {}
        self.body = ""
        self.entity_list = []
        self.row = 2
        self.tab1_initial()
        self.tab3_initial()

    def tab1_initial(self):

        label1 = Label(self.tab1, text="Key")
        label2 = Label(self.tab1, text="Value")
        label1.grid(row=1, column=0, padx=30, pady=5)
        label2.grid(row=1, column=1, padx=40, pady=5)
        _initial = False


        key_var = StringVar()
        value_var = StringVar()
        key_var.trace_add("write", callback=lambda name, index, mode, var=key_var: self.callback(key_var))
        value_var.trace_add("write", callback=lambda name, index, mode, var=key_var: self.callback(value_var))
        entry_key = Entry(self.tab1, textvariable=key_var)
        entry_value = Entry(self.tab1, textvariable=value_var)
        entry_key.grid(row=self.row, column=0, padx=self.padx, pady=self.pady, sticky='e')
        entry_value.grid(row=self.row, column=1, padx=self.padx, pady=self.pady)

        self.entity_list.append((entry_key, entry_value, key_var, value_var))


    def  callback(self, var, *keys, **kwargs):
        print(var.get(), keys, "\n", kwargs)
        if self.entity_list[-1][2].get() != "" or self.entity_list[-1][3].get() != "":
            # if len(ev) > 0: pass
            self.row += 1
            key_var   = StringVar()
            value_var = StringVar()
            key_var.trace_add("write", callback=lambda name, index, mode, var=key_var: self.callback(key_var))
            value_var.trace_add("write", callback=lambda name, index, mode, var=key_var: self.callback(value_var))
            entry_key   = Entry(self.tab1, textvariable=key_var)
            entry_value = Entry(self.tab1, textvariable=value_var)
            entry_key.  grid(row=self.row, column=0, padx=self.padx, pady=self.pady)
            entry_value.grid(row=self.row, column=1, padx=self.padx, pady=self.pady)
            self.entity_list.append((entry_key, entry_value, key_var, value_var))
            print(len(self.entity_list))
        elif len(self.entity_list) >= 2 and self.entity_list[-2][2].get() == "" and self.entity_list[-2][3].get() == "":
            entry_tmp_key, entry_tmp_value, _, __  = self.entity_list.pop()
            entry_tmp_key.destroy()
            entry_tmp_value.destroy()


    def tab3_initial(self):
        text = Text(self.tab3, undo=True, bg="antique white", state='normal', relief=FLAT,
                    # width=145, height=120,
                    font=("Consolas", 12, NORMAL), padx=5, pady=5, highlightbackground="white")
        text.grid(row=0, column=0)
        text.config(width=80, height=18)
        # text.place(relx=0, rely=0, relwidth=1, relheight=1)
    def create_tab(self, text, number):
        tab = tk.Frame(self.base_frame)
        tab.grid(row=0, column=number, padx=15, pady=15, sticky='ew')
        self.base_frame.add(tab, text=text)
        return tab


if __name__ == "__main__":
    root = Tk()

    root.geometry("500x400")
    notebook = Notebook(root)
    notebook.grid(row=0, column=0, padx=10, pady=5, sticky='ew')
    ccc = TabControl(notebook)
    root.mainloop()


