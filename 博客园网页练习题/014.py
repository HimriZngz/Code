# 编写代码，实现求100-200里面所有的素数


def cac(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


l = []
for x in range(100, 201):
    if cac(x):
        l.append(x)
print(l)
print(len(l))