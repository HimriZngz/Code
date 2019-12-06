# 2. 要求自己写一个 MyRev 类，功能与 reversed() 相同
# （内置函数 reversed(seq) 是返回一个迭代器，是序列 seq 的逆序显示）。


class Myrev:
    def __init__(self, s):
        self.s = s
        self.l = len(self.s)

    def __iter__(self):
        return self

    def __next__(self):
        if self.l == 0:
            raise StopIteration

        self.l -= 1     # -1 最开始达到索引最后一位，在此之后达到依次索引前一位
        r = self.s[self.l]

        return r


