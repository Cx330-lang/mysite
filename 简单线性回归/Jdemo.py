import numpy as np

def fitslr(x, y):
    lenth = len(x)
    di = 0
    mi = 0
    for i in range(lenth):
        di += (x[i] - np.mean(x))*(y[i] - np.mean(y))
        mi += (x[i] - np.mean(x)) ** 2

    b1 = di/float(mi)
    b0 = np.mean(y) - b1*np.mean(x)

    return b0, b1

def predict(x, b0, b1):
    return b1*x +b0

x = [1, 3, 2, 1, 3]
y = [14, 24, 18, 17, 27]

b0, b1 = fitslr(x, y)
print(b0, b1)

x_test = 6
y_test = predict(6, b0, b1)

print("y_test:",y_test)
