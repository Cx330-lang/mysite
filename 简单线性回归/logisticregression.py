import numpy as np
import random

def gradientDescent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose() #转置
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta) #点积
        loss = hypothesis - y
        cost = np.sum(loss ** 2)/(2 * m)
        print("Iteration %d|Cost:%f"%(i, cost))
        gradient = np.dot(xTrans, loss)/m
        theta = theta - alpha * gradient
    return theta

def genData(numPoints, bias, variance):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    #basically a straight line
    for i in range(0, numPoints):
        #bias feature
        x[i][0] = 1
        x[i][1] = i
        #our target variable
        y[i] = (i + bias) + random.uniform(0, 1) * variance #从0-1中随机产生数字*v
    return x, y

# gen 100 points with a bias
x,y = genData(100, 25, 10)
print("x:", x)
print("y:", y)
m, n = np.shape(x)
n_y = np.shape(y)

print("m:"+str(m)+" n:"+str(n)+" n_y:"+str(n_y))

numIterations = 100000
alpha = 0.0005
theta = np.ones(n)
theta= gradientDescent(x, y, theta, alpha, m, numIterations)
print(theta)