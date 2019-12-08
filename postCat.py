__author__ = "Linhai"

import urllib3.connection
from urllib import request

from tkinter import *
from tkinter.messagebox import *
# from tkinter.dialog import *
from tkinter.filedialog import *
import os
from tkinter.font import *
import tkinter.ttk as ttk

root = Tk()

root.geometry("960x720+100+100")

var1 = StringVar()
var1.set("http://")

# cv = Canvas(root, background='white')
# cv.grid(row=0, column=0, rowspan=700, columnspan=1)
# tang = cv.create_rectangle(0, 0, 10, 100, fill='red')

font_type = "Consolas"
font_fav = Font(root, font=((font_type, 16, NORMAL)))

entry = Entry(root, textvariable=var1, text="Open", show=None, bg='#DDDED4',
                width=50,font=font_fav,
              fg="#874387", highlightcolor='red', selectbackground='red')#exportselection
# 设置字体后自动改变窗体大小哈
# fg selectborderwidth selectforeground
# 文字颜色。值为颜色或为颜色代码，如：'red','#ff0000'
#默认情况下，你如果在输入框中选中文本，默认会复制到粘贴板，如果要忽略这个功能刻工艺设置 exportselection=0。
entry.grid(row=0, column=1, sticky='nwse', padx=10, pady=15)
# scroll01 = Scrollbar(root, orient=HORIZONTAL)
# entry.config(xscrollcommand=scroll01.set, state='normal')
# scroll01.config(command=entry.xview)
# scroll01.grid(row=1, sticky='ne', padx=10, pady=10)

entry.insert(0, var1.get())
entry.focus()

# 先用frame划分 很牛皮！！！

entry.configure()
var1 = entry.get()
# Entry(root).grid(row=10, column=5)
# Label(root, text="First", width=50, height=20).grid(row=1, column=10, )
# Label(root, text="Second").grid(row=2, column=10, sticky=E, columnspan=10)


var2 = StringVar()

request_com = ttk.Combobox(root, textvariable=var2, width=8, font=Font(root, font=((font_type, 14, ROMAN))))
request_com['value'] = ["GET", "POST"]
# request_com.set("GET") == 下一句
# var2.set("GET") # == 下一句
request_com.current(0)

request_com.grid(row=0, column=0, sticky='nwse', padx=10, pady=15)
print(var2.get())


if __name__ == "__main__":
    root.mainloop()
