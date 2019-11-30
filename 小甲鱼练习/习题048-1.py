# 1. 写一个迭代器，要求输出至今为止的所有闰年。


class Leap_year:
    def __init__(self, year):
        self.year = year
        self.ylist = []

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.year):
            if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
                self.ylist.append(i)

        return self.ylist
