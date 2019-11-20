def func1():
    return 1, 4


def cacl1():
    a = 0
    for i in func1():
        a += i
    return a


print(cacl1())