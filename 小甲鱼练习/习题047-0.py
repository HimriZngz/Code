# 0. 根据课堂上的例子，定制一个列表，同样要求记录列表中每个元素被访问的次数。
# 这一次我们希望定制的列表功能更加全面一些，比如支持 append()、pop()、extend() 原生列表所拥有的方法。
# 你应该如何修改呢？
#
# 要求1：实现获取、设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）
# 要求2：增加 counter(index) 方法，返回 index 参数所指定的元素记录的访问次数H
# 要求3：实现 append()、pop()、remove()、insert()、clear() 和 reverse() 方法（重写这些方法的时候注意考虑计数器的对应改变）
#
# 今天只有一道动动手的题目，但在写代码的时候要时刻考虑到你的列表增加了计数器功能，所以请务必要考虑周全再提交答案。


class Lie:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys((x for x in args), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        #   返回获取的指定元素
        self.count[item] += 1
        return self.values[item]

    def __setitem__(self, key, value):
        #   设置指定元素到列表
        if key in self.values:
            return '该元素已存在，将会覆盖加入到列表，并清零其访问次数'
        else:
            self.values.append(key)
            self.count[key] = 0

    def __delitem__(self, key):
        #   删除指定元素
        if key not in self.values:
            return '该元素不存在于列表中'
        else:
            del self.values[key]
            self.count.pop(key)
            return '已删除'

    def counter(self, index):
        #   返回指定元素被访问的次数
        if index not in self.count:
            return '该元素不存在于列表中'
        else:
            return '%s被访问了%s次' % (index, self.count[index])

    def append(self, item):
        #   用列表+列表的方式达成append
        l = [item]
        self.values += l
        self.count[item] = 0

    def pop(self):
        #   删除列表最后一个对象
        del self.values[-1]
        del self.count[item]

    def remove(self, item):
        #   删除指定元素
        del self.values[item]
        del self.count[item]

    def insert(self,item):
        pass

    def clear(self):
        self.values =[]
        self.count = {}
        return '已清空列表及其访问次数'

    def reverse(self):
        l_2 = []



"""
我佛了
"""

