# 0. 请写一个密码安全性检查的脚本代码：check.py
#   
# # 密码安全性检查代码
# #
# # 低级密码要求：
# #   1. 密码由单纯的数字或字母组成
# #   2. 密码长度小于等于8位
# #
# # 中级密码要求：
# #   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
# #   2. 密码长度不能低于8位
# #
# # 高级密码要求：
# #   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
# #   2. 密码只能由字母开头
# #   3. 密码长度不能低于16位

pw = input('请输入要检查的密码：')
password = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"


if len(pw) <= 8 and pw.isalnum():
    print('密码安全性低')
elif len(pw) > 8 and pw.isalnum():
    l = []
    for x in pw:
        while x in password:
            l.append(x)
        if len(l) >= 2:
            print('密码安全性中')
        else:
            print('密码安全性低')
elif len(pw) > 16 and pw[0:1].isalpha():
    l = []
    for x in pw:
        while x in password:
            l.append(x)
        if len(l) >= 3:
            print('密码安全性高')
        else:
            print('密码安全性低')
else:
    print('密码安全性低')