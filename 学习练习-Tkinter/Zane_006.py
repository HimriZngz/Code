'''
各种组件
'''

from tkinter import *

win = Tk()

s = StringVar()
s.set('123456')
ent = Entry(win, textvariable=s, show='*', width=20, bg='blue', state='readonly', fg='red')
ent.pack()
# print(s.get())
win.mainloop()