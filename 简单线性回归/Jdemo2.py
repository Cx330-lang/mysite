from numpy import genfromtxt
import numpy as np
from sklearn import datasets,linear_model

filename = 'Deliverydatachange.csv'
data = genfromtxt(filename, delimiter=',')

print("data")
print(data)
print(data[1][1])

X = data[:, :-1]
Y = data[:, -1]

print(X)
print(Y)

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print(regr.coef_)
print(regr.intercept_)

xPredict = [90,2,0,0,1]
yPredict = regr.predict([xPredict])

print(yPredict)