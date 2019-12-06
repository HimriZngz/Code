# 0. 要求实现一个功能与 reversed() 相同
# （内置函数 reversed(seq) 是返回一个迭代器，是序列 seq 的逆序显示）的生成器。


# def myrev(*args):
#     a = len(args)
#     while 1:
#         if a == 0:
#             break
#         else:
#             a -= 1
#             yield args[a]


def myrev(data):
    # 这里用 range 生成 data 的倒序索引
    # 注意，range 的结束位置是不包含的
    for index in range(len(data)-1, -1, -1):
        yield data[index]



for x in myrev('ABCD'):
    print(x)
