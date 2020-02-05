from tkinter import *


root = Tk()

group = LabelFrame(root, text='最好的编程语言是？', padx=5, pady=5)
group.pack(padx=10, pady=10)

LANGS = [('Python', 1), ('Java', 2), ('Html', 3), ('Ruby', 4)]

v = IntVar()

for lang, num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num)
    b.pack(anchor=W)

mainloop()