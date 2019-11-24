'''
刷新frame的实例应用

开发移动电子广告效果就可以使用after()方法实现不断移动 lab
'''

from tkinter import *

win = Tk()
f = Frame(win, height=200, width=200)
lab = Label(f, text='欢迎光临，欢迎光临')
x = 0


def foo():
    global x
    x += 10
    if x > 200:
        x = 0
    lab.place(x=x, y=0)
    f.after(500, foo)


f.pack()
foo()
win.mainloop()
