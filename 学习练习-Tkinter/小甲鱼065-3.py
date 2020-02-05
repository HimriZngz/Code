import os
from tkinter import *

os.chdir('.')


def call():
    var.set('你说你马呢')


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('您年满十八岁了吗？\n满十八岁才可以观看哦~')
textLabel = Label(frame1, textvariable=var, justify=LEFT)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='forbidden.png')
imgLabel = Label(frame1, image=photo,)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text='我满18了', command=call)
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()
