import itertools


# num1 = itertools.count(1)
# con1 = itertools.takewhile(lambda x: x <= 20, num1)
# print(list(con1))
# 打印结果 ： [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# for chain1 in itertools.chain('abc', 'ABC'):
#     print(chain1)

# for key, group in itertools.groupby('AABBCCaaccbac'):
#     print(key, list(group))

# for key, group in itertools.groupby('AaaBBbcCAAa', lambda x: x.upper()):
#     print(key, list(group))

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    jishu = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    quxiang = itertools.takewhile(lambda x: x <= 2 * N - 1, jishu)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    a = -1
    b = 0
    for i in quxiang:
        a *= -1
        b += a*4/i
    # step 4: 求和:
    return b


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
