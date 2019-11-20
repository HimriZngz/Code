'''
编写一个符合下列要求的函数：
    a) 计算打印所有参数的和乘以基数（base = 3）的结果
    b) 如果参数中最后一个参数为5，则设定基数为5，（base = x) 此时不参与求和运算
'''


def cac_by_base(x, y=3):
    l = list(x)
    if l[-1] == 5:
        y = 5
        l.pop()
        # print(l)
    a = 0
    for i in l:
        a += i
    # print(a)
    return a * y


print(cac_by_base([1,2,3,4,5]))