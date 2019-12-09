import sys


class Const:
    def __init__(self):
        self.NAME = ''

    def __setattr__(self, key, value):
        if self.key == self.NAME:
            print('已存在的常量名')
        else:
            try:
                str(self.key).isupper()
            except TypeError:
                print('常量名必须大写')
            else:
                self.key = value


sys.modules[__name__] = Const()

"""
报错，不存在key
"""