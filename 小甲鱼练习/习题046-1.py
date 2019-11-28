# 1. 按要求编写描述符 MyDes：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件：record.txt


from datetime import datetime
import time
import os

os.chdir(os.curdir)
# f = open('./小甲鱼练习题辅助文档/record.txt', 'a')


def time_now():
    #   得到现在的时间，以str的 . 为分隔符切分，保留前段
    t = datetime.now()
    t_2 = str(t).split('.')[0]

    #   先给个列表，以localtime()的6号索引返回的数值来确定今天属于星期几
    week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    week_2 = week[time.localtime()[6]]
    return t_2 + ' ' + week_2


class Mydes:
    def __init__(self, value_default=None, name=None):
        self.val = value_default
        self.name = name

    def __set__(self, instance, value):
        self.val = value
        word = '变量 %s 于 %s 被修改为 %s \n' % (self.name, time_now(), self.val)
        with open('./小甲鱼练习题辅助文档/record.txt', 'a')as f:
            f.writelines(word)
        print('变量修改了')

    def __get__(self, instance, owner):
        word = '变量 %s 于 %s 被读取，值为 %s \n' % (self.name, time_now(), self.val)
        with open('./小甲鱼练习题辅助文档/record.txt', 'a')as f:
            f.writelines(word)
        print('变量被读取了')
        return self.val


class Test:
    x = Mydes(10, 'x')
    y = Mydes(8.8, 'y')


"""
运行时输入下面：

test = Test()
test.x
10
test.y
8.8
test.x = 123
test.x = 1.23
test.y = "I love FishC.com!"


"""


"""
参考答案：

import time

class Record:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name
        self.filename = "record.txt"

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被读取，%s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(self.val)))
        return self.val

    def __set__(self, instance, value):
        filename = "%s_record.txt" % self.name
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被修改, %s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(value)))
        self.val = value

"""