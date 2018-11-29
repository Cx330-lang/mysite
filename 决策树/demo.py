from sklearn.feature_extraction import DictVectorizer
import csv
import numpy as np
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

# read in the csv file and put features into list of dict and list or classlabel
allElectronicsData = open('AllElectronics.csv', 'rt')
reader = csv.reader(allElectronicsData)
headers = next(reader) #python2 headers = reader.next
print(headers)

featureList = []
labelList = []

# 将每一行转换成字典模式，放在list里面
for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i]

    featureList.append(rowDict)

print(featureList)

# Vectorize features
vec = DictVectorizer() #将字典中对应的数据矢量化
# age，credit_rating,income,student
dummyX = vec.fit_transform(featureList) .toarray()
print(vec.get_feature_names())
print("dummyX:"+str(dummyX))
# print(vec.get_feature_names())

# vectorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:"+ str(dummyY))


clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf:" + str(clf))

# visualize model
with open("change.dot", "w", encoding='utf-8') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)
# 在命令行执行 dot -Tpdf 路径 -o 名称.pdf, 在当前目录生成决策树的可视化文件.pdf.

oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

# check new
newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(oneRowX))

predictedY = clf.predict([newRowX])
print("predictedY: " + str(predictedY))