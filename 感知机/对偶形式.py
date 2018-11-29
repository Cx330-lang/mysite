import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

traing_set = np.array([[[3, 3], 1], [[4, 3], 1], [[1, 1], -1]])
print(len(traing_set))
a = np.zeros(len(traing_set), np.float)
b = 0.0
Gram = None
y = np.array(traing_set[:, 1])
x = np.empty((len(traing_set), 2), np.float)
for i in range(len(traing_set)):
    x[i] = traing_set[i][0]

history = [] #history记录每次迭代结果

def cal_gram():
    g = np.empty((len(traing_set), len(traing_set)), np.int)
    for i in range(len(traing_set)):
        for j in range(len(traing_set)):
            g[i][j] = np.dot(traing_set[i][0], traing_set[j][0])
    return g

# 随机梯度下降更新参数
def update(i):
    global a,b
    a[i] +=1
    b =b + 1*y[i] #1表示的学习效率
    history.append([np.dot(a*y, x),b])
    print(a,b)


def check():
    global a,b,x,y
    flag = False
    for i in range(len(traing_set)):
        if cal(i) <= 0:
            flag = True
            update(i)
    if not flag:
        w = np.dot(a * y, x)
        print("RESULT: w:" + str(w) + "b: " + str(b))
        return False
    return True

# 判断是否误分类
def cal(i):
    global a,b,x,y
    res = np.dot(a*y, Gram[i])
    res = (res + b)*y[i]
    return res

if __name__ == "__main__":
    Gram = cal_gram() # 初始化Gram矩阵
    for i in range(1000):
        if not check():
            break
