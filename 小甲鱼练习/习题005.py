# 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用）
#
# 这样定义闰年的:能被4整除但不能被100整除,或者能被400整除都是闰年。

year = input('输入年份：')
while not year.isdigit():
    print('请输入整数年')
    year = input('输入年份：')

year_int = int(year)
if year_int / 400 == int(year_int / 400):
    print(year + '是闰年')
elif year_int / 4 == int(year_int / 4) and year_int / 100 != int(year_int / 100):
    print(year + '是闰年')
else:
    print(year + '不是闰年')
