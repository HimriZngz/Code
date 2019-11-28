"""
有点难以理解
"""


class Counter:
    def __init__(self):
        super().__setattr__('count', 0)

    def __setattr__(self, key, value):
        super().__setattr__('count', self.count + 1)
        super().__setattr__(key, value)

    def __delattr__(self, item):
        super().__setattr__('count', self.count - 1)
        super().__delattr__(item)

