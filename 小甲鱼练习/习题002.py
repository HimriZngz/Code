i = input('要做哪道题？\n\n\t1 - hello.py\t\t2 - cacl.py\n')
if int(i) == 1:
    
    # hello.py

    name = input('请输入你的姓名: ')
    print('你好呀,', name)
    
elif int(i) == 2:
    
    # calc.py

    num = input('请输入1-100以内的数字：')
    if 1 <= int(num) <= 100:
        print('你妹好漂亮え')

    else:
        print('你妹的,太丑了8')

else:
    pass
