# 0. 我们都知道在 Python 中，两个字符串相加会自动拼接字符串，但遗憾的是两个字符串相减却抛出异常。
# 因此，现在我们要求定义一个 Nstr 类，支持字符串的相减操作：A – B，从 A 中去除所有 B 的子字符串


class Nstr:
    def __sub__(self, other):
        x = ''
        for i in other:
            if issubclass(i,self):
                x.join(i)
        return x


a = Nstr('I love FishC.com!iiiiiiii')
b = Nstr('i')
print(a)
