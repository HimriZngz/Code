# 1. 定义一个单词（Word）类继承自字符串，重写比较操作符（参考自学：Python 魔法方法详解），
# 当两个 Word 类对象进行比较时，根据单词的长度来进行比较大小。
# 加分要求：实例化时如果传入的是带空格的字符串，则取第一个空格前的单词作为参数。


class Word(str):
    def __new__(cls, s=''):
        ss = len(s.split()[0])
        return ss

    def __lt__(self, other):
        if self < other:
            return True
        else:
            return False

    def __eq__(self, other):
        if self == other:
            return True
        else:
            return False

    def __gt__(self, other):
        if self > other:
            return True
        else:
            return False

    def __le__(self, other):
        if self <= other:
            return True
        else:
            return False

    def __ge__(self, other):
        if self >= other:
            return True
        else:
            return False


a = Word('abcde')       # 5
b = Word('cc zzzzz')    # 2
c = Word('abcde aa')    # 5

print(a > b)    # T
print(b > a)    # F
print(b < a)    # T
print(a == c)   # T
print(a >= c)   # T
print(b >= c)   # F


"""
参考答案：

class Word(str):
'''存储单词的类，定义比较单词的几种方法'''

    def __new__(cls, word):
        # 注意我们必须要用到 __new__ 方法，因为 str 是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

"""