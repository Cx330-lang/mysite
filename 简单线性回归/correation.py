import numpy as np
import math

def computeCorrelation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR = 0
    varX =0
    varY =0
    for i in range(0, len(x)):
        diffXXBar = X[i] - xBar
        diffYYBAr = Y[i] - yBar
        SSR +=(diffXXBar * diffYYBAr)
        varX +=diffXXBAr ** 2
        varY += diffYYBAr ** 2

    SST = math.sqrt(varX*varY)
    return SSR/SST

def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)

    results['polynomial'] = coeffs.tolist()

    p = np.poly1d(coeffs)

    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg =np.sum((yhat - ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['determination'] = ssreg/sstot

    return results
