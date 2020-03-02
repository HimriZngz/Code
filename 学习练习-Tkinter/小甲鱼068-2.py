from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

LB = Listbox(root, yscrollcommand=sb.set)

for i in range(1, 501):
    LB.insert(END, i)

LB.pack(side=LEFT, fill=BOTH)

sb.config(command=LB.yview)     # 先生成滚动条，在列表未生成时设置滚动条的command属性可能出现意外

mainloop()
