# 2. 再来一个有趣的案例：编写描述符 MyDes，使用文件来存储属性，
# 属性的值会直接存储到对应的pickle（腌菜，还记得吗？）的文件中。如果属性被删除了，
# 文件也会同时被删除，属性的名字也会被注销。


import os
import pickle

os.chdir(os.curdir)


class Mydes:
    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        val = value
        word = '变量 %s 被修改为 %s \n' % (self.name, val)
        file_name = './小甲鱼练习题辅助文档/%s.pkl' % self.name
        with open(file_name, 'wb')as f:
            pickle.dump(word, f)
        print('变量被修改了')

    def __get__(self, instance, owner):
        file_name = './小甲鱼练习题辅助文档/%s.pkl' % self.name
        with open(file_name, 'rb')as f:
            val = pickle.load(f)
        print('变量被读取了')
        return val

    def __delete__(self, instance):
        # del self.val
        file_name = './小甲鱼练习题辅助文档/%s-%s.pkl' % self.name
        os.remove(file_name)
        print('变量被删除了')


class Test:
    x = Mydes('x')
    y = Mydes('y')


