import numpy as np
import random

sizes = [2,3,1]
# bias = [np.random.randn(y, 1) for y in sizes[1:]]
# # print(bias)

weight = [np.random.randn(y, x) for x,y in zip(sizes[:-1], sizes[1:])]
print(weight)