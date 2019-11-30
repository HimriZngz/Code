# # 0. 用 while 语句实现与以下 for 语句相同的功能：
# for each in range(5):
#     print(each)

a = range(5)
b = iter(a)

while 1:
    try:
        c = next(b)
        print(c)

    except StopIteration:
        break
