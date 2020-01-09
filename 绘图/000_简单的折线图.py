# https://blog.csdn.net/youku1327/article/details/103833954


import matplotlib.pyplot as mlp


line = [1, 3, 4, 6, 2, 0, 1, 7, 9]


mlp.plot(line, linewidth=2)

mlp.title("line", fontsize=12)

mlp.xlabel("x", fontsize=12)
mlp.ylabel("y", fontsize=12)

mlp.show()
