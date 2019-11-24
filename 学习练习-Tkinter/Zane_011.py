'''
框架组件 Frame，LabelFrame组件
'''

from tkinter import *

win = Tk()
win.title('使用frame组件的例子')

# 创建组件并生成
f1 = Frame(win)
f2 = Frame(win)
f1.pack()
f2.pack()

# 第三个组件是LabelFrame组件，放在下面
f3 = LabelFrame(win, text='第三个组件')
f3.pack(side=BOTTOM)

# f1的三个组件
redbutton = Button(f1, text='红色', fg='red')
redbutton.pack(side=LEFT)
brownbutton = Button(f1, text='棕色', fg='brown')
brownbutton.pack(side=LEFT)
bluebutton = Button(f1, text='蓝色', fg='blue')
bluebutton.pack(side=LEFT)

# f2的一个组件
blackbutton = Button(f2, text='黑色', fg='black')
blackbutton.pack()

# f3的一个组件
greenbutton = Button(f3, text='绿色', fg='green')
greenbutton.pack()

win.mainloop()
