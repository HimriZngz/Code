import random
import pickle
import os
import time

#  切换至当前目录，与pkl文件保持同步
os.chdir(os.curdir)

#  先给一个空的列表用来存等会儿已经产生了的文字
list_history = []

# 计数
count = 0


def read_file():
    """这里以随机数来获取列表内的其中一个元素"""
    with open('50yin.pkl', 'rb')as y:
        yin = pickle.load(y)
        num_1 = random.randint(0, 103)
        num_2 = random.randint(0, 2)
        #  通过随机数，随机获得一个列表中的子列表中的一个元素
        word = yin[num_1][num_2]
        #  以及对应子列表的全体元素
        word_all = yin[num_1]
        list_history.append(word_all)
        print(word)
        global count
        count += 1


def wait():
    """等待5s出答案"""
    time.sleep(5)
    for item in list_history[-1]:
        print(item, end='\t')


while 1:
    if count > 104:
        print('没了')
        break
    else:
        read_file()
        wait()
        c = input('\n回车继续下一个， 否则结束并查看全部答案\n')
        if c:
            for i in list_history:
                for x in i:
                    print(x, '\t', end='\t')
                print('\n')
            print(f'学了{count}个')
            break
        else:
            continue
