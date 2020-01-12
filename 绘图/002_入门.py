#  https://www.jianshu.com/p/aa4150cf6c7f


import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']    # 更改字体,以显示中文


x = [3, 5, 7]
y = [1, 4, 7]

x2 = [4, 7, 11]
y2 = [2, 9, 5]

plt.plot(x, y, 'ro', label='第一条线')
plt.plot(x2, y2, 'b-', label='第二条线')

plt.xlabel('x轴')
plt.ylabel('y轴')

plt.title('test lines \n double color')

plt.legend()
plt.show()

