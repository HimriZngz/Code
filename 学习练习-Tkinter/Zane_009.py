'''
菜单组件 menu
'''

from tkinter import *

win = Tk()


def hello():        # 菜单项的事件函数，每个菜单都可以单独设置
    print('点击了主菜单')


def com():
    print('第二个命令')


# 创建菜单实例
m = Menu(win)

for item in ['文件', '编辑', '视图', '工具']:       # 添加上菜单项
    m.add_command(label=item, command=hello)        # 通过遍历来使全体菜单项都指向一个命令函数

'''
# 以单独的方式添加菜单项及其命令

m.add_command(label='文件', command=com)
m.add_command(label='编辑', command=com)
m.add_command(label='视图', command=com)
m.add_command(label='工具', command=com)

'''

# 附加主菜单到窗口
win['menu'] = m
win.mainloop()
