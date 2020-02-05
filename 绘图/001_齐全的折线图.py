import matplotlib.pyplot as mlp
import numpy as np


line1 = [1, 2, 6, 8, 9]
line2 = [2, 4, 12, 16, 18]

mlp.plot(line1, line2, linewidth=3)

mlp.title("line", fontsize=12)

mlp.xlabel("x", fontsize=12)
mlp.ylabel("y", fontsize=12)

mlp.show()
