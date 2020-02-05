from tkinter import *


root = Tk()

LANGS = [('Python', 1), ('Java', 2), ('Html', 3), ('Ruby', 4)]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)  # indicatoron=指示器
    b.pack(fill=X)

mainloop()