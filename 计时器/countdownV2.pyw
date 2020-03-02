import time
from datetime import datetime
from tkinter import *
from tkinter import messagebox as msgbox

'''
V2 相比V1添加了重置按钮，运行时点击重置可停止计时并恢复到初始状态
'''

root = Tk()
root.title('倒计时器')
root.geometry('290x190')
root.minsize(290, 190)
root.maxsize(290, 190)


def get_time():
    # 获取当前时间
    time_float = time.time()
    time_now = datetime.fromtimestamp(time_float)
    var1.set(str(time_now).split('.')[0])
    # 每隔一秒调用函数自身获取时间
    root.after(1000, get_time)


var1 = StringVar()

now = Label(root, text='当前的时间', font=('XHei iOS', 15))
now2 = Label(root, textvariable=var1, font=('Consolas', 15))
now.pack()
now2.pack()

get_time()


L = LabelFrame(root, text='Remaining Time', width=20, height=1)
L.pack(fill='both', padx=10, pady=10)

var2 = StringVar()
var2.set('2小时0分0秒')


def alert():
    time_float = time.time()
    time_now = datetime.fromtimestamp(time_float)
    end_time = str(time_now).split('.')[0]
    msg = end_time + '\n' + '时间到了'

    msgbox.showinfo(title='Time up', message=msg)


num = 7200
run = True  # T 则开始按钮亮，倒计时可以运行，反之不能


def countdown():
    global num, run
    if num <= 7200 and run:

        start.config(state='disabled')
        reset.config(state='normal')

        num_second = num % 60
        num_minute = num // 60 % 60
        num_hour = num // 3600

        var2.set('%d小时%d分%d秒' % (num_hour, num_minute, num_second))

        num -= 1

        if num >= 0:
            root.after(1000, countdown)
        else:
            re_set()
            run = True
            alert()
    else:
        run = True


residue = Label(L, textvariable=var2, font=('Comic Sans MS', 16))
residue.pack(side=LEFT, padx=35)


start = Button(root, text='开始', fg='green', width=13, height=1, command=countdown)
start.pack(side=LEFT, anchor=SW, padx=10, pady=5)
end = Button(root, text='退出', fg='red', width=13, height=1, command=root.quit)
end.pack(side=RIGHT, anchor=SE, padx=10, pady=5)


def re_set():
    global num, run

    start.config(state='normal')
    num = 7200
    var2.set('2小时0分0秒')

    run = False

    reset.config(state='disabled')


# 重置按钮，使开始按钮、计时都恢复默认
reset = Button(L, text='重置', command=re_set, state='disable')
reset.pack(side=RIGHT, padx=2)

mainloop()
