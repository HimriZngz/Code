# Copy from  https://www.cnblogs.com/PPhoebe/p/6708642.html

year = int(input('请输入年:'))
month = int(input('请输入月:'))
day = int(input('请输入天:'))
sum_ = day
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 0
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days[1] = 29
while i < month - 1:
    sum_ += days[i]
    i += 1
print('这一天是该年的第', sum_, '天')