# 从键盘获取用户名、密码
# 如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎登陆xxx”，否则提示密码或者用户名错误

username = input('用户名：')
password = input('密码：')
def_username = 'Tom'
def_password = '123456'
if username == def_username:
    if password == def_password:
        print('欢迎登录')
    else:
        print('密码错误')
else:
    print('用户名错误')