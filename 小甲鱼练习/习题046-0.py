# 0. 按要求编写描述符 MyDes：当类的属性被访问、修改或设置的时候，分别做出提醒。


class Mydes:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __set__(self, instance, value):
        print('正在修改变量')
        self.fset(instance, value)

    def __get__(self, instance, owner):
        print('正在修改变量')
        self.fget(instance)

    def __del__(self, instance):
        print('正在删除变量')
        self.fdel(instance)


class Test:
    x = Mydes(10, 'x')

