# 0. 编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。


def power(x, y):
    return x**y


print(power(5, 2))


# 1. 编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，
# 例如gcd(x, y)返回值为参数x和参数y的最大公约数。

def euclid(x, y):
    a = max(x, y)
    b = min(x, y)
    while a % b != 0:
        a, b = b, (a % b)
    else:
        return b


print(euclid(615, 1997))

# 2. 编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，
# 结果与调用bin()一样返回字符串形式。

def ten2two(dec):
    temp = []
    result = ''
    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)
    while temp:
        result += str(temp.pop())

    return result


print(ten2two(62))
