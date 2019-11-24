'''
单选按钮与复选框
'''

from tkinter import *

win = Tk()
'''
c = IntVar()
c.set(2)
check = Checkbutton(win, text='ABCD', variable=c, onvalue=1, offvalue=2)
check.pack()
# win.mainloop()
'''

# 单选按钮

# 创建StringVar对象  并设置初始值为1,即选中‘中国’
r = StringVar()
r.set('1')
ra = Radiobutton(win, variable=r, value='1', text='中国')
ra.pack()
ra = Radiobutton(win, variable=r, value='2', text='米国')
ra.pack()
ra = Radiobutton(win, variable=r, value='3', text='印度')
ra.pack()
ra = Radiobutton(win, variable=r, value='4', text='俄罗斯')
ra.pack()
ra = Radiobutton(win, variable=r, value='5', text='德国')
ra.pack()
win.mainloop()
print(r.get())