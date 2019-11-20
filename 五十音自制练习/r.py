#  先以列表套列表方式准备五十音文本，然后设置空白列表存放已经提取到的对象(以便复看)
#

import random
import pickle
from tkinter import *
import os
import time

#  切换至当前目录，与pkl文件保持同步
os.chdir(os.curdir)

#  先给一个空的列表用来存等会儿已经产生了的文字
list_history = []

#  生成框架，写入标题，并限制窗体大小
window = Tk()
window.title('五十音练习')
window.geometry('230x50')
# window.minsize(100, 300)
# window.maxsize(500, 300)


def start():
    """点击开始，计时也随之开始"""
    time_1 = time.time()


def end():
    """点击停止，几时也随之停止"""
    time_2 = time.time()


def count(time_1, time_2):
    """计算时长"""
    t = time_2 - time_1


def open_pkl():
    """这里打开pkl数据文件"""
    with open('50yin.pkl', 'rb')as y:
        yin = pickle.load(y)


def read_file(yin):
    """这里以随机数来获取列表内的其中一个元素"""
    num_1 = random.randint(0, 103)
    num_2 = random.randint(0, 2)
    #  通过随机数，随机获得一个列表中的子列表中的一个元素
    word = yin[num_1][num_2]
    #  以及对应子列表的全体元素
    word_all = yin[num_1]


button_start = Button(window, text='开始练习')
button_start.pack(anchor=SW, pady=0, command=start())

# button_end = Button(window, text='停止练习')
# button_end.pack(side=RIGHT, pady=10, command=end())





window.mainloop()
