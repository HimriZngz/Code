from tkinter import *

root = Tk()

L1 = Label(root, text='请选择x的值', width=15)
L1.pack(anchor=N)
L2 = Label(root, text='请选择y的值', width=15)
L2.pack(anchor=N)


def choice_x(v):
    L1.config(text='x=%s' % v)


def choice_y(v):
    L2.config(text='y=%s' % v)


s1 = Scale(root, from_=0.00, to=10.00, command=choice_x, tickinterval=1, resolution=0.01, length=300)
s1.pack(side=RIGHT)
s2 = Scale(root, from_=0.00, to=30.00, orient=HORIZONTAL, command=choice_y, tickinterval=3, resolution=0.1, length=500)
s2.pack(side=BOTTOM)


def show():
    print('x=', s1.get(), 'y=', s2.get())


B = Button(root, text='获取值打印出来', command=show).pack(side=BOTTOM)

mainloop()
