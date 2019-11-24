'''
图形窗口编辑
'''

import tkinter

# 生成窗口对象
wi = tkinter.Tk()

# 给窗口起名
wi.title('一个窗口程序')

# 设置默认窗口大小
wi.geometry("400x400")

# 可选设置窗口的最大化与最小化值
wi.minsize(200, 200)
wi.maxsize(600, 600)

# 显示窗口(进入消息循环)
wi.mainloop()

