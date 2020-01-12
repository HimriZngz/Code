import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']    # 更改字体,以显示中文


"""
直方图非常像条形图，倾向于通过将区段组合在一起来显示分布。 
这个例子可能是年龄的分组，或测试的分数。 
我们并不是显示每一组的年龄，而是按照 20 ~ 25，25 ~ 30... 等等来显示年龄。
"""

ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(ages, bins, histtype='bar', width=6, color='brown')

plt.xlabel('年龄')
plt.ylabel('数量')

plt.title('年龄分布图')

plt.show()
