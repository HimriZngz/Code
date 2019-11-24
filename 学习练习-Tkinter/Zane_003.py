'''
几何布局管理 - grid
'''

from tkinter import *

item = Tk()

# 200x200代表初始化时窗口的大小，280+280代表了初始化时窗口所在的位置
item.geometry('200x200+280+280')
item.title('模型计算器')

# 开始布局
b1 = Button(item, text='1', width=5, bg='yellow')
b2 = Button(item, text='2', width=5, bg='grey')
b3 = Button(item, text='3', width=5, bg='blue')
b4 = Button(item, text='4', width=5, bg='red')
b5 = Button(item, text='5', width=5, bg='white')
b6 = Button(item, text='6', width=5, bg='green')
b7 = Button(item, text='7', width=5, bg='orange')
b8 = Button(item, text='8', width=5, bg='pink')
b9 = Button(item, text='9', width=5, bg='purple')
b0 = Button(item, text='0', bg='gold')
bp = Button(item, text='.')
# row 行， column 列
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=3, column=0, columnspan=2, sticky=E+W)   # 跨两行，左右贴紧
bp.grid(row=3, column=2, sticky=E+W)    # 左右贴紧

item.mainloop()
