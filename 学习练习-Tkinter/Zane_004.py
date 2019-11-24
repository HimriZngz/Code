'''
几何布局管理 - place
'''

from tkinter import *

item = Tk()
item.title('登录')
item['width'] = 200
item['height'] = 80

# 设置属性.(绝对坐标)
Label(item, text='用户名', width=6).place(x=1, y=1)
Entry(item, width=20).place(x=45, y=1)

Label(item, text='密码', width=6).place(x=1, y=20)
Entry(item, width=20, show='*').place(x=45, y=20)

# 设置按钮.(绝对坐标)
Button(item, text='登录', width=8).place(x=42, y=42)
Button(item, text='取消', width=8).place(x=115, y=42)

item.mainloop()
