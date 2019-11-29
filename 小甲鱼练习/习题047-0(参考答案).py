# 为了实现这么多功能，我们不能再用字典来存放元素的计数了。因为对于列表来说，
# 如果你删除其中一个元素，那么其他元素的下标都会发生相应的变化（利用下标作为键的字典肯定就不能应对自如）。
# 因此，我们改用一个列表来存放对应的元素的计数。
#
# 下边的 CountList 类继承并严重依赖其父类（list）的行为，并按要求重写了一些方法。


class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()
