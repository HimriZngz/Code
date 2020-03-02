from tkinter import *

root = Tk()

L1 = Label(root, text='作品:').grid(row=0, column=0, padx=10, pady=5)
L2 = Label(root, text='作者:').grid(row=1, column=0, padx=10, pady=5)

E1 = Entry(root)
E1.grid(row=0, column=1, padx=10, pady=5)
E2 = Entry(root)
E2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print('作品:《%s》' % E1.get())
    print('作者:%s' % E2.get())


B1 = Button(root, text='发送信息', command=show).grid(row=2, column=0, sticky=W, padx=10, pady=5)
B2 = Button(root, text='结束进程', command=root.quit).grid(row=2, column=1, sticky=E, padx=10, pady=5)

mainloop()

