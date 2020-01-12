import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']    # 更改字体,以显示中文


plt.bar([1,3,5,7,9,], [5,2,7,8,2,], label='栗子1')
plt.bar([2,4,6,8,10], [8,6,2,5,6,], label='栗子2')    # 可以额外更改颜色
# plt.bar([2,4,6,8,10], [8,6,2,5,6,], label='栗子2', color='red')

plt.legend()    # 生成默认图例

plt.xlabel('x轴')
plt.ylabel('y轴')

plt.title('条形图')

plt.show()
