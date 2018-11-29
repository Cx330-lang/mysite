import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.preprocessing import LabelBinarizer
from neuralnetwork import NeuralNetwork
from sklearn.cross_validation import train_test_split

digits = load_digits()
X = digits.data
# print(X)
y =digits.target
# print(y)
X -= X.min()
X /= X.max()
# print(X)

nn = NeuralNetwork([64,100,10], 'logistic')
X_train, X_test, y_train, y_test = train_test_split(X ,y)
lables_train = LabelBinarizer().fit_transform(y_train)
lables_test = LabelBinarizer().fit_transform(y_test)
print("start fitting")
nn.fit(X_train, lables_train, epochs=3000)
predictions = []
for i in range(X_test.shape[0]):
    o = nn.predict(X_test[i])
    predictions.append(np.argmax(o))
print(predictions)

#混淆矩阵是一种特定的矩阵用来呈现算法性能的可视化效果
print(confusion_matrix(y_test, predictions))

# sklearn中的classification_report函数用于显示主要分类指标的文本报告．在报告中显示每个类的精确度，召回率，F1值等信息。
print(classification_report(y_test, predictions))