'''
几何布局管理 - pack
'''

import tkinter

item = tkinter.Tk()
item.title('一个窗口')
item.geometry("300x300")
item.minsize(200, 200)
item.maxsize(400, 400)

# 设置窗口的标签
label =tkinter.Label(item, text='一个标签')

# 将label组件添加到窗口中显示
label.pack()

# 创建文字是‘按钮1’的button组件, 下同
button1 = tkinter.Button(item, text='按钮1')
button2 = tkinter.Button(item, text='按钮2')

# 将组件添加到窗口中显示，并指定好位置
button1.pack(side=tkinter.LEFT, anchor=tkinter.N, fill=tkinter.Y)      # side上下左右，anchor东南西北，fill填充到...
button2.pack(side=tkinter.RIGHT)

item.mainloop()
