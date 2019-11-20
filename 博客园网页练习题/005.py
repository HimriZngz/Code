# 实现一个整数加法计算器
# 思路： 用户输入 123+456 即以+为分离符号

user_input = input('加法运算>>>')
i = 0
# print(user_input.split('+'))
# 分离
split_input = user_input.split('+')
for x in split_input:
    i += int(x)   # 如果没有int 就会报错，字符串不能与数字相加减
print(i)