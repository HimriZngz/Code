# 0. 定义一个类，当实例化该类的时候，自动判断传入了多少个参数，并显示出来


class J:
    def __init__(self, *args):
        if not args:
            print('还没有传入参数')
        else:
            print('传入了%s个参数，分别是:' % len(args), end='')
            for i in args:
                print(i, end=' ')


"""
哇草
"""


a = J(9, 9)
b = J()