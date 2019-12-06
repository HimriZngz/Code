# 1. 写一个迭代器，要求输出至今为止的所有闰年。


class Leap_year:
    def __init__(self):
        self.year = 2020

    def isleapyear(self, i):
        if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isleapyear(self.year):
            self.year -= 1

        ly = self.year
        self.year -= 1
        # 两次都有 -=1 是针对于两个不同的情况而做相同的操作，确保不管是不是闰年，年份都会-1
        return ly

