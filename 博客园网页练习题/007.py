# 编写代码，有如下数字

li = [1,2,3,4,5,6,7,8,8]
# 能组成多少个互不相同且不重复的数字的两位数
li2 = []
for num_1 in li:
    for num_2 in li:
        if num_1 != num_2:
            van = num_1 * 10 + num_2
            li2.append(van)
s = list(set(li2))      # 用set去重
print(s)
print(len(s))
