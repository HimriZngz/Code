# 呃，不得不说我们的用户变得越来越刁钻了。
# 要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。
# 如输入13:21打印第13行到第21行，输入:21打印前21行，输入21:则打印从第21行开始到文件结尾所有内容

path = input('文件位置：')

with open(path, 'r')as f:
    l = f.readlines()
    print('该文件有%s行\n' % len(l))
    while 1:
        line_start = input('开始于第几行:')
        line_end = input('结束于第几行:')
        if int(line_start) < 0 or int(line_end) > len(l):
            print('行数没有输入正确')
            continue

    print('')

    if len(line_start) == 0:
        if len(line_end) == 0:
            print('全文为：\n')
            for i in l:
                print(i)
        else:
            print('开头到第%s行为：\n' % line_end)
            for i in l[:int(line_end)]:
                print(i)
    else:
        if len(line_end) == 0:
            print('从第%s行到末尾为：\n' % line_start)
            for i in (l[int(line_start) - 1:]):
                print(i)
        else:
            print('从第%s行到第%s行为：\n' % (line_start, line_end))
            for i in (l[int(line_start) - 1:int(line_end)]):
                print(i)
