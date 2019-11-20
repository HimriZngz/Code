# 0. 视频中小甲鱼使用 if elif else 在大多数情况下效率要比全部使用 if 要高，
# 但根据一般的统计规律，一个班的成绩一般服从正态分布，也就是说平均成绩一般集中在 70~80 分之间，
# 因此根据统计规律，我们还可以改进下程序以提高效率。
#   
# 题目备忘：按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，
# 写一个程序，当用户输入分数，自动转换为ABCD的形式打印。
'''
score = int(input('请输入分数：'))
if 60 <= score < 80:
    print('C')
elif 80 <= score < 90:
    print('B')
elif 90 <= score < 100:
    print('A')
elif score < 60:
    print('D')
else:
    print('分数输入有误')
'''


# 1. Python 的作者在很长一段时间不肯加入三元操作符就是怕跟C语言一样搞出国际乱码大赛，
# 蛋疼的复杂度让初学者望而生畏，不过，如果你一旦搞清楚了三元操作符的使用技巧，
# 或许一些比较复杂的问题反而迎刃而解。
# 请将以下代码修改为三元操作符实现：
'''
x, y, z = 6, 5, 4
if x < y:
    small = x
    if z < small:
        small = z
elif y < z:
    small = y
else:
    small = z
'''
# x, y, z = 6, 5, 4
x, y, z = 50, 5, 200
small = z if z < y else y if y < x else x
print(small)
