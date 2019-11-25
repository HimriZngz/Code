# 定义一个类Nstr，当该类的实例对象间发生的加、减、乘、除运算时，将该对象的所有字符串的ASCII码之和进行计算


class Nstr(str):
    def __add__(self, other):
        ss = 0
        oo = 0
        for s in self:
            ss += ord(s)
        for o in other:
            oo += ord(o)
        return int.__add__(ss, oo)

    def __sub__(self, other):
        ss = 0
        oo = 0
        for s in self:
            ss += ord(s)
        for o in other:
            oo += ord(o)
        return int.__sub__(ss, oo)

    def __mul__(self, other):
        ss = 0
        oo = 0
        for s in self:
            ss += ord(s)
        for o in other:
            oo += ord(o)
        return int.__mul__(ss, oo)

    def __truediv__(self, other):
        ss = 0
        oo = 0
        for s in self:
            ss += ord(s)
        for o in other:
            oo += ord(o)
        return int.__truediv__(ss, oo)

    def __floordiv__(self, other):
        ss = 0
        oo = 0
        for s in self:
            ss += ord(s)
        for o in other:
            oo += ord(o)
        return int.__floordiv__(ss, oo)


a = Nstr('FishC')
b = Nstr('love')

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)


"""
参考答案1：

class Nstr:
    def __init__(self, arg=''):
        if isinstance(arg, str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("参数错误！")

    def __add__(self, other):
        return self.total + other.total

    def __sub__(self, other):
        return self.total - other.total

    def __mul__(self, other):
        return self.total * other.total

    def __truediv__(self, other):
        return self.total / other.total

    def __floordiv__(self, other):
        return self.total // other.total


参考答案2：

class Nstr(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)


"""