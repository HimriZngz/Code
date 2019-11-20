g = 5
print('初始g值:', g)


def cac_1(g):       # 只能通过函数的设置参数才能调用到g 否则要报错 并且仅属于调用g值而无法修改
    g += g
    print(g)


cac_1(g)
print('当前g值:', g)


def cac_2():        # 在函数中使用了global后可以无需设置参数即可调用并控制全局变量g
    global g
    g = g**2
    print(g)


cac_2()
print('当前g值:', g)