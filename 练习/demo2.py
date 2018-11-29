import numpy as np
import matplotlib
import time
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.pyplot as plt

# a = np.arange(1,10,0.5)
# print(a)

# b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#
# print(b)
# print(b.shape)
#
# b.shape =
#
# print(b)

# b = np.linspace(1, 10, 10, endpoint=False)
#
# print(b)

#
# d = np.logspace(0, 10, 10, endpoint=True)
# print(d)

# 字符串的值转换为数值
# s = 'abcd'
# g = np.fromstring(s, dtype=np.int8)
# print(g)

# a = np.random.rand(10)
# print(a)
# b = a[a>0.5]
# print(b)
# print(a)

# a = np.arange(0, 60, 10)
# print("a=", a)
# b = a.reshape(-1, 1)
# print(b)
# c = np.arange(6)
# print(c)
# f = a+b
# print(f)

# print(f[(0,1,2,3),(2,3,4,5)])
# print(f[3:,[0,2,5]])

# for j in np.logspace(0, 7, 10):
#     print(int(j))
#     x = np.linspace(0, 10, j)
#     start = time.clock()
#     y = np.sin(x)
#     t1 = time.clock() - start
#
#     x = x.tolist()
#     start = time.clock()
#     for i, t in enumerate(x):
#         x[i] = math.sin(t)
#     t2 = time.clock() - start
#     print(j, ": ", t1, t2, t2/t1)

# 正态分布
# matplotlib.rcParams['font.sans-serif'] = [u'SimHei']  #FangSong/黑体 FangSong/KaiTi
# matplotlib.rcParams['axes.unicode_minus'] = False
# mu = 0
# sigma = 1
# x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50)
# y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
# print(x.shape)
# print('x = \n', x)
# print(y.shape)
# print('y = \n', y)
# # plt.plot(x, y, 'ro-', linewidth=2)
# plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)
# plt.title("高斯分布")
# plt.grid(True)
# plt.show()

# x = np.array(np.linspace(start=-2, stop=3, num=1001, dtype=np.float))
# y_logit = np.log(1 + np.exp(-x)) / math.log(2)
# y_boost = np.exp(-x)
# y_01 = x < 0
# y_hinge = 1.0 - x
# y_hinge[y_hinge < 0] = 0
# plt.plot(x, y_logit, 'r-', label='Logistic Loss', linewidth=2)
# plt.plot(x, y_01, 'g-', label='0/1 Loss', linewidth=2)
# plt.plot(x, y_hinge, 'b-', label='Hinge Loss', linewidth=2)
# plt.plot(x, y_boost, 'm--', label='Adaboost Loss', linewidth=2)
# plt.grid()
# plt.legend(loc='upper right')
# # plt.savefig('1.png')
# plt.show()

# # 5.3 x^x
# x = np.linspace(-1.3, 1.3, 101)
# y = x**2
# plt.plot(x, y, 'g-', label='x^x', linewidth=2)
# plt.grid()
# plt.legend(loc='upper left')
# plt.show()

# # 6.1 均匀分布
# x = np.random.rand(10000)
# t = np.arange(len(x))
# plt.hist(x, 30, color='m', alpha=0.5)
# plt.plot(t, x, 'r-', label=u'均匀分布')
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()

# t = 10000
# a = np.zeros(1000)
# for i in range(t):
#     a += np.random.uniform(-5, 5, 1000)
# a /= t
# plt.hist(a, bins=30, color='g', alpha=0.5, normed=True)
# plt.grid()
# plt.show()

# squares = [1, 4, 9,16, 25]
#
# plt.plot(squares, linewidth=5)
#
# plt.title("y=x*x", fontsize=24)
# plt.xlabel("value", fontsize=14)
# plt.ylabel("Square of value",fontsize=24)
#
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

x_values = list(range(1,1001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)

plt.show()