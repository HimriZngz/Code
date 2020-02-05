import os
from tkinter import *


os.chdir('.')

root = Tk()

textLabel = Label(root, text='您年满十八岁了吗？\n满十八岁才可以观看哦~', justify=LEFT, padx=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='forbidden.png')
imgLabel = Label(root, image=photo,)
imgLabel.pack(side=RIGHT)

mainloop()