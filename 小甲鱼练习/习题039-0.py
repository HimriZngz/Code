# 0. 思考这一讲我学习的内容，请动手在一个类中定义一个变量，用于跟踪该类有多少个实例被创建
# （当实例化一个对象，这个变量+1，当销毁一个对象，这个变量自动-1）

class C:
    count = 0

    def __init__(self):
        C.count += 1

    def kill(self):
        C.count -= 1


a = C()
b = C()
c = C()
print(c.count)

a.kill()
b.kill()
c.kill()
print(c.count)