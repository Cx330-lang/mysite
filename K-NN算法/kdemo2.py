import csv
import random
import operator
import math


def loadDataset(filename, spilt, trainingSet, testSet):
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile)
        dataset = list(reader)
        # print(dataset)
        for x in range(len(dataset) - 1):#读入的数据是字符型，转换成float型
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
        # print(dataset)
            if random.random() < spilt:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow(instance1[x] - instance2[x], 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distance = []
    length = len(testInstance) -1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distance.append((trainingSet[x], dist))
    distance.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distance[x][0])
    return neighbors

def getResponse(neighbors):
    classvote = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classvote:
            classvote[response] += 1
        else:
            classvote[response] = 1
    sortedvote = sorted(classvote.items(), key=operator.itemgetter(1), reverse=True)
    return sortedvote[0][0]

def main():
    trainingSet = []
    testSet = []
    spilt = 0.7
    loadDataset('irisdata.txt', spilt, trainingSet, testSet)
    print('Train set:' + repr(len(trainingSet)))
    print('Test set:' + repr(len(testSet)))
    prediction = []
    k =3
    corret = []
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        response = getResponse(neighbors)
        prediction.append(response)
        # print('predictions: ' + repr(predictions))
        # print('>predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        if response == testSet[x][-1]:
            corret.append(x)
    accuracy = (len(corret) / float(len(testSet))) * 100.0
    print("accuracy=" + repr(accuracy) + "%")

if __name__ == '__main__':
    main()