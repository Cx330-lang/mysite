import numpy as np
import pylab as pl
from sklearn import svm

np.random.seed(0) #固定随机产生的点
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
print("X:", X)
# np.r_是将一系列的序列合并到一个数组中，调用是要用中括号[],而不是()
Y = [0]*20 + [1]*20

clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

w = clf.coef_[0]
a = -w[0]/w[1] #画出直线的斜率
print("w:", w)
print("a:", a)
xx = np.linspace(-5, 5)
print("xx:", xx)
yy = a*xx - (clf.intercept_[0]/w[1])
print("yy:", yy)

b = clf.support_vectors_[0]
print(b)
yy_down = a*xx + (b[1] - a*b[0])
b = clf.support_vectors_[-1]
yy_up = a*xx + (b[1] - a*b[0])

print("support_vectors_:", clf.support_vectors_)
print("clf.coef_:", clf.coef_)
print("clf.intercept_:", clf.intercept_)

pl.plot(xx, yy, 'k-')
pl.plot(xx, yy_down, 'k--')
pl.plot(xx, yy_up, 'k--')

pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none')
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()