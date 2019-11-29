import os
import pickle


class Mydes:
    saved = []

    def __init__(self, name=None):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in Mydes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)

        with open(self.filename, 'rb') as f:
            value = pickle.load(f)

        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            Mydes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        Mydes.saved.remove(self.name)


class Test:
    x = Mydes('x')
    y = Mydes('y')


