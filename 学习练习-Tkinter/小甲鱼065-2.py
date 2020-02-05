import os
from tkinter import *


os.chdir('.')

root = Tk()

photo = PhotoImage(file='bg.png')

theLabel = Label(root, text='学挖掘机技术哪家强', image=photo, compound=CENTER, font=('苹方-简', 18), fg='black')

theLabel.pack()

mainloop()
