from math import sqrt


class A:
    # from math import sqrt   # 在类里面不可以导入模块
    def squer(self, x):
        a = x ** 2
        print(a)
    def abc(self, x):
        l = sqrt(x)
        # print('%d' % l)
        print(l)


class B(A):
    def cac(self, x):
        super().squer(x)
    def ssum(self, x):
        j = x * 10
        print(j)
    def ssqrt(self, x):
        super().abc(x)


B().cac(2)
B().ssum(2)
B().ssqrt(6)
A().abc(9)
A().squer(10)