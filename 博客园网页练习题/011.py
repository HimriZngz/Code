# 计算用户输入的内容中有几个十进制小数？几个字母？

str_ = input('输入')
d = 0
s = 0
for i in str_:
    if i.isdecimal():
        d += 1
    elif i.isalpha():
        s += 1
print('十进制数有%s个，字母有%s个' % (d, s))