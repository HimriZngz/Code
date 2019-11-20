# 0. 编写一个函数，判断传入的字符串参数是否为“回文联”，即从左往右从右往左读都是一样的


'''def huiwen(x):
    l = []
    for i in x:
        l.append(i)
    if l[:] == l[::-1]:
        print(x, ' - 是回文联')
    else:
        print(x, ' - 不是回文联')


huiwen('123456787654321')
huiwen('上海自来水来自海上')
'''
# 1. 编写一个函数，分别统计出字符串参数中的英文字母，空格，数字以及其他字符个数


def statistics(*args):
    length = len(args)
    for everyone in range(length):
        alpha = 0
        number = 0
        space = 0
        other = 0
        for i in args[everyone]:
            if i.isalpha():
                alpha += 1
            elif i.isdigit():
                number += 1
            elif i.isspace():
                space += 1
            else:
                other += 1
        print('参数'+str((everyone+1))+'中\n英文字符有'+str(alpha)+'个；有数字'+str(number)+'个\n有空格'+str(space)+'个；其他字符'+str(other)+'个\n')


statistics('123456789+abcdefg     ', 'ABCDE22  FG....')