#  编写一个程序，实现“全部替换”功能

path = input('文件地址：')
str_want = input('想要替换的是：')
str_change = input('想要替换为：')

l = []      # 拿来装将要改之后的文字
count = 0
with open(path, 'r')as f:
    for i in f.read():
        if str_want in i:
            count += 1  # 统计出现次数
            l.append(str_change)    # 如果该文字出现，就加入想改的文字
        l.append(i)     # 反之，就加原来的文字
    print('%s共有%s个\n' % (str_want, count))

print('确定要将%s替换为%s吗？')

while 1:
    decision = input('no=0, yes=1')
    if decision == 'no':
        break
    elif decision == 'yes':
        with open(path, 'w')as e:   # 写入模式打开
            for i in l:
                e.write(i)      # 遍历已经改好的l，然后循环写入进去
        break
    else:
        print('输入有误')
        continue
