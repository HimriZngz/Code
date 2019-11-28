# 1. 编写一个 Counter 类，用于实时检测对象有多少个属性


class Counter:
    def __init__(self, count=0):
        self.count = count

    def __setattr__(self, key, value):
        self.count += 1
        return '增加了1个属性'

    def __getattribute__(self, item):
        return self.count

    def __getattr__(self, item):
        return '还没有属性'

    def __delattr__(self, item):
        self.count -= 1
        return '删除了1个属性'

#  运行后会报错，无限递归


"""
参考答案：

class Counter:
        def __init__(self):
                super().__setattr__('counter', 0)
        def __setattr__(self, name, value):
                super().__setattr__('counter', self.counter + 1)
                super().__setattr__(name, value)
        def __delattr__(self, name):
                super().__setattr__('counter', self.counter - 1)
                super().__delattr__(name)
                
"""
