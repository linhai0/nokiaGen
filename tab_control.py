# -*- coding: utf-8 -*-
# /usr/bin/

__author__ = "Linhai"

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
        self.tab1 = self.create_tab("第一页")
        self.tab2 = self.create_tab("第二页")
        self.tab3 = self.create_tab("第三页")

        # header = StringVar()
        self.header = {}
        self.param = {}
        self.body = ""

    def tab1(self, add_row=True, current_row=1, _initial=True):
        if _initial:
            lable1 = Label(self.base_frame, text="Key")
            lable2 = Label(self.base_frame, text="Value")
            lable1.grid(row=0, column=0, padx=10, pady=5)
            lable2.grid(row=0, column=1, padx=10, pady=5)
            _initial = False

        if not add_row:
            return

        keyvar = StringVar()
        value = StringVar()
        entry_left = Entry(self.base_frame, textvariable=keyvar)
        entry_right = Entry(self.base_frame, textvariable=value)
        entry_left.grid(row=current_row, columnu=0, padx=10, pady=5)
        entry_right.grid(row=current_row, columnu=1, padx=10, pady=5)

        def callback_input():
            x = keyvar.get()

            if x != "":
                current_row += 1
                self.tab1(add_row=True, current_row=, _initial=False)

        keyvar.trace("w", callback=callback_input)


    def create_tab(self, text):
        tab = ttk.Frame(self.base_frame)
        self.base_frame.add(tab, text=text)

