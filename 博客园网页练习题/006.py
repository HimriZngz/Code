# 有如下值集合[11,22,33,44,55,66,77,88,99,90]
# 将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。

i = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
'''k1, k2 = []
for k in i:
    if k >= 66:
        k1 = list.append(k)
    else:
        k2 = list.append(k)
print(k1, k2)         # 看看做成了个什么鬼
a = {'K1': k1, 'k2': 'k2'}
print(a)
'''

sort_i = sorted(i, reverse=True)
the_num = sort_i.index(66)
K = {'K1': sort_i[:the_num], 'K2': sort_i[the_num + 1:]}
print(K)