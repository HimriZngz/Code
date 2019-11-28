# 0. 按要求编写描述符 MyDes：当类的属性被访问、修改或设置的时候，分别做出提醒。


class Mydes:
    def __init__(self, initval=None, name=None):
        self.name = name
        self.val = initval

    def __set__(self, instance, value):
        print('正在修改变量' + self.name)
        self.val = value

    def __get__(self, instance, owner):
        print('正在获取变量' + self.name)
        return self.val

    def __del__(self):
        print('正在删除变量' + self.name)
        print('但是删不了')
        #  这里在调用del的时候会报错，AttributeError: __delete__


class Test:
    x = Mydes(10, 'x')


"""
运行后输入下面：

test = Test()
y = test.x
正在获取变量： x
y
10
test.x = 8
正在修改变量： x
del test.x
正在删除变量： x
噢~这个变量没法删除~
test.x
正在获取变量： x
8
"""
