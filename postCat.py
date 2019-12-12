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

from tab_control import *

root = Tk()

root.geometry("1250x900")
# Style(root).theme_use('default') # ('aqua', 'clam', 'alt', 'default', 'classic')

print(ttk.Style().layout("TNotebook"))

# 最底下一拦 显示整体状态
frame_buttom = Frame(root)
frame_buttom.grid(row=1, column=0, sticky="e")

frame_base = Frame(root)
frame_base.grid(row=0)

frame0 = Frame(frame_base)
frame0.grid(row=0, column=0, sticky='news')



listbox01 = Listbox(frame0)
listbox01.grid(row=0, column=0, padx=10, pady=10)
for x in ['Python', 'Kotlin', 'Swift', 'Ruby']:
            listbox01.insert(END, x)

for x in range(20):
    b = Button(frame0, text="--{}--".format(x))
    b.grid(row=x + 1, column=0 )

# 中间一大片
frame1 = Frame(frame_base)
frame1.grid(row=0, column=1, )

# 右边一大列
frame2 = Frame(frame_base, )
frame2.grid(row=0, column=2)

listbox02= Listbox(frame2)
listbox02.configure(height=10)
listbox02.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
listbox02.configure(width=10)
for x in ['Python', 'Kotlin', 'Swift', 'Ruby']:
            listbox02.insert(END, x)

# buttom

statusbar = tk.Label(frame_buttom, bd=0, text="LN20: --", relief=RIDGE, anchor='se')
statusbar.grid(row=0, column=0, sticky="s")
statusbar1 = tk.Label(frame_buttom, bd=0, text="Time: --", relief=RIDGE, anchor='se', padx=10)
statusbar1.grid(row=0, column=1, sticky="s")
# statusbar.configure(width=110)
# statusbar.place(relx=0, relwidth=1)
# statusbar.pack(fill=X, side=BOTTOM, expand=1)

# statusbar = tk.Label(frame_buttom, text="LN20ghjklkdjhgd", bd=1, relief=RIDGE, anchor='se', width=100)
# # statusbar.pack(side=BOTTOM, fill=X)
# statusbar.place(relx=0, rely=0, relwidth=1, relheight=1)
# # statusbar.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

# 最上面
frame10 = Frame(frame1, )
frame10.grid(row=0, column=0, )



# url
frame11 = Frame(frame1, )
frame11.grid(row=1, column=0, sticky='newe')



# 请求参数选项卡
frame12 = Frame(frame1)
frame12.grid(row=2, column=0,  columnspan=2,  pady=50, padx=80, )
# frame.grid_columnconfigure(1, weight=1)
# frame.grid_rowconfigure(1, weight=1)
# 进度条 先不用
frame13 = Frame(frame1, )
frame13.grid(row=3, column=0,  columnspan=2)
# response标题
frame14 = Frame(frame1, )
frame14.grid(row=4, column=0,  sticky='W', )
# frame14.configure(foreground="#748734")
# response状态
frame15 = Frame(frame1)
frame15.grid(row=5, column=0,  sticky="w")

response_frame = Frame(frame11)
response_frame.grid(row=6, column=0, sticky="news")


var1 = StringVar()
var1.set("HHHH")

# cv = Canvas(root, background='white')
# cv.grid(row=0, column=0, rowspan=700, columnspan=1)
# tang = cv.create_rectangle(0, 0, 10, 100, fill='red')

font_type = "Consolas"
font_fav = Font(frame11, font=((font_type, 16, NORMAL)))

entry = Entry(frame11, textvariable=var1, text="Open", show=None,
              background='#DDDED4',
              width=50, font=font_fav,
              foreground="#874387")
#                highlightcolor='red', selectbackground='red')#exportselection
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
request_com = ttk.Combobox(frame11, textvariable=var2, width=8,state='readonly',
                           font=Font(root, font=((font_type, 13, ROMAN))))
request_com['value'] = ["67890", "POST"]
# request_com.set("GET") == 下一句
# var2.set("GET") # == 下一句
request_com.current(0)

request_com.grid(row=0, column=0, sticky='news', padx=10, pady=15)

x0, y0, x1, y1= 0, 0, 40, 40
cv = Canvas(frame11, height=40, width=40)
cv.grid(row=0, column=2)
cv.create_arc(x0+10, y0+10, x1+10, y1+10, start=0, extent=180)  #创建一个扇形
line = cv.create_line(x0, y0, x1, y1)

send_but = Button(cv,  )
send_but.grid(row=0, column=1)

def moveit(rect): # 参数，目标组件
    cv.move(rect, 0, 2)


# sp01 = Spinbox(frame1)
# sp01.grid(row=0, column=2)


var3 = StringVar()
pro_bar = Progressbar(frame13, variable=var3)
pro_bar.grid(row=0, column=0, sticky='news', padx=10, pady=10)
for x in range(50):
    var3.set(x)



# style.configure('lefttab.TNotebook', tabposition='ns')
base_tab = Notebook(frame12, )

base_tab.grid(row=0, column=0, padx=10, pady=10, ipady=6)
tabs = TabControl(base_tab)

# notebook.grid_columnconfigure(1, weight=1)
# notebook.grid_rowconfigure(1, weight=1)

res_button = Label(frame14, text="response", foreground='green')
res_button.grid(row=0, column=0, sticky="news", padx=10)

# 相应 进度条
res_process_var = IntVar()
res_process_bar = Progressbar(frame14, value=0, variable=res_process_var)
res_process_bar.grid(row=0, column=1, sticky="e", )
res_process_var.set(20)

#
status_label = Label(frame14, text="Status: ")
status_label.grid(row=1, column=1, sticky="w", padx=10)

response_var = StringVar()
status_string = Label(frame14, textvariable=response_var)
status_string.grid(row=1, column=2, sticky="w", padx=10)
response_var.set("0------0")



if __name__ == "__main__":
    root.mainloop()
