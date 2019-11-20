'''
0. 猜想一下 min() 这个BIF的实现过程


1. 视频中我们说 sum() 这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，
请写出一个新的实现过程，自动“无视”参数里的字符串并返回正确的计算结果
'''

# 0


def min2(*args):
    a = args[0]
    for i in args:
        if i < a:
            a = i
    return a

print(min2(1,2,3,4,555,6,-444))
# 1


def sum2(args):
    result = 0
    for i in args:
        if (type(i) == int) or (type(i) == float):
            result += i
        else:
            continue
    return result


print(sum2([1, 2.1, 2.3, 'a', '1', True]))