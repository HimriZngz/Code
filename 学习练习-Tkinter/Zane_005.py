'''
几何布局管理 - 标签组件 Label
                Label组件用于在窗口中显示文本或位图
'''

from tkinter import *

win = Tk()
win.title('一个窗口')

# 创建名字是‘你好’的Label组件
lab1 = Label(win, text='你好', anchor='nw')

# 显示Label组件
lab1.pack()

# 显示内置的位图
lab2 = Label(win, bitmap='question')    # 创建显示疑问图标的Label组件
lab2.pack()

''' 

这里出现错误：无法识别图像文件中的数据

# 显示自己的图片
bm = PhotoImage(file=r'D:\PycharmProjects\001.bmp')
lab3 = Label(win, image=bm)
lab3.bmp = bm
lab3.pack()
'''


win.mainloop()
