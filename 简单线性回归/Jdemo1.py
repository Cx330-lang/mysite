from numpy import genfromtxt
import numpy as np
from sklearn import datasets,linear_model

filename = 'Deliverydata.csv'
data = genfromtxt(filename, delimiter=',')

print("data")
print(data)

X = data[:, :-1]
Y = data[:, -1]

print(X)
print(Y)

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print(regr.coef_)
print(regr.intercept_)

xpred = [102, 6]
ypred = regr.predict([xpred])
print("predicted Y:")
print(ypred)