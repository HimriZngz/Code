# 0. 设计一个验证用户密码程序，用户只有三次机会输入错误，
# 不过如果用户输入的内容中包含"*"则不计算在内。
'''
password = '123'
i = 0
while i < 3:
    password_input = input('请输入密码：')
    if password_input != password:
        if '*' in password_input:
            continue
        else:
            i += 1
            print('当前密码输入错误' + str(i) + '次')
            continue
    else:
        print('密码正确')
        break
else:
    print('密码输入错误超过三次')
'''

# 1. 编写一个程序，求 100~999 之间的所有水仙花数。
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。

'''
for num in range(100, 999):
    hund = int(num / 100)
    ten = int((num - hund * 100) / 10)
    one = int((num - hund * 100) - ten * 10)
    while num == hund ** 3 + ten ** 3 + one ** 3:
        print(num)
        break
'''


# 2. 三色球问题
# 有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。
# 先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。


for red in range(4):
    for yellow in range(4):
        for green in (2, 7):
            if red + yellow + green == 8:
                print('红球', red, '', '黄球', yellow, '', '绿球', green)
