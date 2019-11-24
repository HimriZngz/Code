'''
刷新frame组件

用 Python 做 GUI 图形界面，可使用after()方法每隔几秒刷新 GUI 图形界面。
下面的代码实现计数器功能，并且文字背景色不断改变
'''

from tkinter import *

color = ('red', 'brown', 'blue', 'yellow', 'gold', 'white')

win = Tk()
f = Frame(win, height=200, width=200)
f.color = 0

# 设置框架背景颜色
f['bg'] = color[f.color]
lab1 = Label(f, text='0')
lab1.pack()


def foo():
    f.color = (f.color + 1) % (len(color))
    lab1['bg'] = color[f.color]
    lab1['text'] = str(int(lab1['text']) + 1)
    # 隔500ms刷新一次foo函数也就是刷新屏幕
    f.after(500, foo)


f.pack()
foo()   # 开始执行
# f.after(500, foo)     # 或者以这种方式执行  无所谓
win.mainloop()
