import time
from datetime import datetime
from tkinter import *
from tkinter import messagebox as msgbox

'''
V3 相比V2稍微优化了代码排版，添加了自定义时间的方式
(原来存在“加时-开始-重置”三连后的alert问题)
'''

num = 0  # 默认为0秒
run = True  # T 则开始按钮亮，倒计时可以运行，反之不能


def back_info():
    """通过num的值，将其转化为指定的剩余时间文本"""
    global num

    num_second = num % 60
    num_minute = num // 60 % 60
    num_hour = num // 3600
    info = '%d小时%d分%d秒' % (num_hour, num_minute, num_second)

    return info


def get_time():
    """获取当前时间"""
    time_float = time.time()
    time_now = datetime.fromtimestamp(time_float)
    var_now.set(str(time_now).split('.')[0])
    # 每隔一秒调用函数自身获取时间
    root.after(1000, get_time)


def countdown():
    """开始倒计时按钮"""
    global num, run
    if run:
        hour_u.config(state='disabled')
        hour_d.config(state='disabled')
        minute_u.config(state='disabled')
        minute_d.config(state='disabled')
        second_u.config(state='disabled')
        second_d.config(state='disabled')

        start.config(state='disabled')
        reset.config(state='normal')

        var_residue.set(back_info())

        num -= 1
        if num >= 0:
            root.after(1000, countdown)
        elif run:
            re_set()
            run = True
            alert()
    else:
        run = True


def alert():
    """提示框"""
    time_float = time.time()
    time_now = datetime.fromtimestamp(time_float)
    end_time = str(time_now).split('.')[0]
    msg = end_time + '\n' + '时间到了'

    msgbox.showinfo(title='Time up', message=msg)


def re_set():
    """重置按钮"""
    global num, run
    hour_u.config(state='normal')
    hour_d.config(state='normal')
    minute_u.config(state='normal')
    minute_d.config(state='normal')
    second_u.config(state='normal')
    second_d.config(state='normal')

    start.config(state='disable')
    reset.config(state='disable')

    num = 0
    var_residue.set(back_info())

    run = False
    # countdown()


"""
设置时分秒的增减按钮并且当num为0时使开始按钮不可用
"""


def set_h1():
    start.config(state='normal')
    reset.config(state='normal')

    global num, run
    run = True

    num += 3600
    var_residue.set(back_info())


def set_h2():
    global num
    if num >=3600:
        num -= 3600
        var_residue.set(back_info())

    if num == 0:
        start.config(state='disable')
        reset.config(state='disable')


def set_m1():
    start.config(state='normal')
    reset.config(state='normal')

    global num, run
    run = True

    num += 60
    var_residue.set(back_info())


def set_m2():
    global num
    if num >= 60:
        num -= 60
        var_residue.set(back_info())

    if num == 0:
        start.config(state='disable')
        reset.config(state='disable')


def set_s1():
    start.config(state='normal')
    reset.config(state='normal')

    global num, run
    run = True

    num += 1
    var_residue.set(back_info())


def set_s2():
    global num
    if num >= 1:
        num -= 1
        var_residue.set(back_info())

    if num == 0:
        start.config(state='disable')
        reset.config(state='disable')


"""
"""


def exit():
    """退出询问"""
    if msgbox.askyesno(title='Exit', message='要退出吗？'):
        root.quit()


def move(event):
    new_x = (event.x) + root.winfo_x()

    # new_x = (event.x - x) + root.winfo_x()
    # new_y = (event.y - y) + root.winfo_y()

    new_y = (event.y) + root.winfo_y()

    root.geometry('320x210+%d+%d' % (new_x, new_y))


def move_button(event):
    x, y = event.x, event.y


# Tk基本框架信息
root = Tk()
root.title('倒计时器')

# 原生的框架大小设置 (这里不使用)
# root.geometry('290x190')
# root.minsize(290, 190)
# root.maxsize(290, 190)

# 获取屏幕大小并让窗口居中显示
screen_width = screen_height = root.maxsize()
root_width = 320
root_height = 210
x = (screen_width[0]-root_width)/2
y = (screen_height[-1]-root_height)/2
root.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

# 此调用方法会禁止根窗体改变大小
root.resizable(False, False)

# 该方法设置覆盖重定向标志，这将删除窗口中的所有窗口管理器的装饰，使其无法移动、调整大小、最小化或关闭。
# (此方法需谨慎使用，使用后没有任务图标了)
# root.overrideredirect(True)
# 以及窗口的移动函数
# root.bind("<B1-Motion>", move)
# root.bind("<Button-1>", move_button)

# 值用来显示为当前时间文本
var_now = StringVar()

# 当前时间的标签
now = Label(root, text='当前的时间', font=('楷体', 19))
now2 = Label(root, textvariable=var_now, font=('Consolas', 16))
now.pack()
now2.pack()

# 开始获取当前时间并持续更新
get_time()

# 用来显示剩余时间的标签框架
L = LabelFrame(root, text='Remaining Time', width=20, height=1)
L.pack(fill='both', padx=10, pady=0)

# 值用来显示剩余时间标签文本并进行默认设置
var_residue = StringVar()
var_residue.set(back_info())

# 处于L中的剩余时间的标签
residue = Label(L, textvariable=var_residue, font=('Comic Sans MS', 16))
residue.pack(side=LEFT, padx=35)

# 重置按钮，使开始按钮、计时都恢复默认
reset = Button(L, text='重置', command=re_set, state='disable')
reset.pack(side=RIGHT, padx=2, pady=0)

# 开始、停止按钮
start = Button(root, text='开始', fg='green' , width=13, height=1, state='disable', command=countdown)
start.pack(side=LEFT, anchor=SW, padx=10, pady=5)
end = Button(root, text='退出', fg='red', width=13, height=1, command=exit)
end.pack(side=RIGHT, anchor=SE, padx=10, pady=5)

# 放置自定义时间的按钮的框架
set_hour = LabelFrame(root, text='H', width=100, height=5)
set_hour.place(x=50,y=116)
set_minute = LabelFrame(root, text='M', width=100, height=5)
set_minute.place(x=130,y=116)
set_second = LabelFrame(root, text='S', width=100, height=5)
set_second.place(x=210,y=116)

# 自定义时间的值增减按钮
hour_u = Button(set_hour, text='+', width=2, height=1, command=set_h1)
hour_u.pack(side=LEFT, padx=2)
hour_d = Button(set_hour, text='-', width=2, height=1, command=set_h2)
hour_d.pack(side=RIGHT, padx=2)

minute_u = Button(set_minute, text='+', width=2, height=1, command=set_m1)
minute_u.pack(side=LEFT, padx=2)
minute_d = Button(set_minute, text='-', width=2, height=1, command=set_m2)
minute_d.pack(side=RIGHT, padx=2)

second_u = Button(set_second, text='+', width=2, height=1, command=set_s1)
second_u.pack(side=LEFT, padx=2)
second_d = Button(set_second, text='-', width=2, height=1, command=set_s2)
second_d.pack(side=RIGHT, padx=2)


mainloop()
