'''
创建一个列表框 选择内容添加到另一个列表框的GUI程序
'''

from tkinter import *

win = Tk()
win.title('KK')
# 创建列表与列表框组件
l = ['A', 'B', 'C', 'D', 'E', 'F']
list1 = Listbox(win)
list2 = Listbox(win)


def callbutton1():
    for i in list1.curselection():  # 遍历选中项
        list2.insert(0, list1.get(i))  # 然后添加到右侧


def callbutton2():
    for i in list2.curselection():  # 遍历选中项
        list2.delete(i)  # 然后从右侧删除该项


for item in l:  # 在左侧列表框插入数据
    list1.insert(0, item)

# 将列表框组件添加到窗口对象中
list1.grid(row=0, column=0, rowspan=2)
list2.grid(row=0, column=2, rowspan=2)

# 创建并显示按钮组件
b1 = Button(win, text='添加→', command=callbutton1, width=20)
b1.grid(row=0, column=1, rowspan=2)

b2 = Button(win, text='删除←', comman=callbutton2, width=20)
b2.grid(row=1, column=1, rowspan=2)

win.mainloop()