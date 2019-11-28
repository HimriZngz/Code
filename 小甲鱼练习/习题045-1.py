# 1. 编写 Demo 类，使得下边代码可以正常执行


class Demo:
    def __getattr__(self, item):
        return 'FishC'

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __getattribute__(self, item):
        return super().__getattribute__(item)


"""
参考答案:
class Demo:
    def __getattr__(self, name):
            self.name = 'FishC'
            return self.name

"""
