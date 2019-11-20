# 编写9*9乘法表

for i in range(1, 10):
    for x in range(1, i+1):
        print('%d * %d = %d' % (x, i, i*x), '\t')
    print('')