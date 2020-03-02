from tkinter import *

root = Tk()

LB = Listbox(root)
LB.pack()

for i in ['汤水', '兔', '汤水兔', '汤兔水', '哦豁']:
    LB.insert(END, i)


def show():
    print(LB.get(ACTIVE))


B = Button(root, text='你选了什么', command=show).pack()

mainloop()
