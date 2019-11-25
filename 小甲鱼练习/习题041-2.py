# 2. 定义一个类继承于 int 类型，并实现一个特殊功能：
# 当传入的参数是字符串的时候，返回该字符串中所有字符的 ASCII 码的和（使用 ord() 获得一个字符的 ASCII 码值）


class Nint(int):
    def __new__(cls, s):
        a = 0
        if not isinstance(s, (int, float)):
            for i in s:
                a += ord(i)
            return a
        else:
            return int(s)


print(Nint(123))
print(Nint(1.5))
print(Nint('A'))
print(Nint('FishC'))


"""
参考答案：

class Nint(int):
        def __new__(cls, arg=0):
                if isinstance(arg, str):
                        total = 0
                        for each in arg:
                                total += ord(each)
                        arg = total
                return int.__new__(cls, arg)



"""