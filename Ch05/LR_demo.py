import matplotlib.pyplot as plt
from numpy import *
from numpy.core.multiarray import ndarray


def loadDataSet():
    dataMat = [];
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)             # convert to NumPy matrix
    labelMat = mat(classLabels).transpose()  # convert to NumPy matrix
    m, n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))
    weights_history = zeros((maxCycles, n))
    for k in range(maxCycles):  # heavy on matrix operations
        gradient = sigmoid(dataMatrix * weights)  # matrix mult
        error = (labelMat - gradient)  # vector subtraction
        weights = weights + alpha * dataMatrix.transpose() * error  # matrix mult
        weights_history[k, :] = weights.transpose()
    return weights,weights_history

def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)   #initialize to all ones
    # weights_history = zeros((m, n))
    for i in range(m):
        gradient = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - gradient
        weights = weights + alpha * error * dataMatrix[i]
        # weights_history[i, :] = weights
    return weights

def plotBestFit(weights):
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = [];
    ycord1 = []
    xcord2 = [];
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1]);
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1]);
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    # y = (0.48 * x + 4.12414) / (0.616)
    print(weights[0,0])
    y = (weights[0,0]+weights[1,0]*x)/(-weights[2,0])
    ax.plot(x, y)
    plt.xlabel('X1');
    plt.ylabel('X2');
    plt.show()


def plot_weights_update(weights_history):
    """用来画权重的更新图"""
    fig = plt.figure()
    # 三行一列的第一行
    ax = fig.add_subplot(311)
    type1 = ax.plot(weights_history[:, 0])
    plt.ylabel('X0')
    ax = fig.add_subplot(312)
    type2 = ax.plot(weights_history[:, 1])
    plt.ylabel('X1')
    ax = fig.add_subplot(313)
    type3 = ax.plot(weights_history[:, 2])
    plt.xlabel('iteration')
    plt.ylabel('X2')
    plt.show()


