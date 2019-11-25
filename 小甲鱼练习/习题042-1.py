# 1. 移位操作符是应用于二进制操作数的，现在需要你定义一个新的类 Nstr，也支持移位操作符的运算


class Nstr(str):
    def __lshift__(self, other):
        x = self[:int(other)]
        return self[int(other):] + x

    def __rshift__(self, other):
        x = self[-(int(other)):]
        return x + self[:-int(other)]


"""
卧槽，佛了
"""

a = Nstr('I love FishC.com!')
b = Nstr('I love FishC.com!')

print(a << 3)
print(a >> 3)
