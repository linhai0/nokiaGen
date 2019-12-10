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


class MyNotebook(Widget):

    def __init__(self, master=None, cnf={}, **kw):

        Widget.__init__(self, master, 'MyNotebook', cnf, kw)

