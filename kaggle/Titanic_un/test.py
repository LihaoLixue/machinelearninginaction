# coding: utf-8
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kaggle import treePlotter,trees
import random
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
trainData = pd.read_csv("titanic/train.csv")
testData = pd.read_csv("titanic/test.csv")
'''处理年龄缺失'''
for i in range(len(trainData)):
    if np.isnan(trainData.iloc[i, 5]):
        trainData.iloc[i, 5] = random.randint(29 - 14, 29 + 14)
trainData = np.array(trainData)
'''处理年龄缺失'''
for i in range(len(testData)):
    if np.isnan(testData.iloc[i, 5]):
        testData.iloc[i, 5] = random.randint(29 - 14, 29 + 14)

'''年龄段划分'''
def life(age):
    if age >= 66:
        return 4    #老年
    else:
        if age >= 41:
            return 3  #中年
        else:
            if age >= 18:
                return 2 #青年
            else:
                if age >= 7:
                    return 1  #少年
                else:
                    return 0  #孩童
labels = ['Pclass','Sex','Age','Embacked']
data=[]
for d in trainData:
    temp = []
    temp.append(str(d[2]))
    temp.append(str(d[4]))
    temp.append(str(life(d[5])))
    temp.append(str(d[11]))
    if d[1] == 1:
        temp.append('yes')
    else:
        temp.append('no')
    data.append(temp)
tree = trees.createTreeOfRito(data,labels)
treePlotter.createPlot(tree)
print(tree)

'''决策树分类器
    参数：inputTree：构建的决策树，  
    featureLabels,testVec：测试数据的特征标签和特征值
'''
def classify(inputTree,featureLabels,testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featureIndex = featureLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featureIndex] == key:
            global classLabel
            if isinstance(secondDict[key],dict):
                classLabel = classify(secondDict[key],featureLabels,testVec)
            else:
                classLabel = secondDict[key]
    return classLabel

'''预测'''
testData = np.array(testData)
featureLabels = ['Pclass','Sex','Age','Embacked']
count=[]
passengerid=[]
for test in testData:
    temp = []
    temp.append(str(test[1]))
    temp.append(str(test[3]))
    temp.append(str(life(test[4])))
    temp.append(str(test[10]))
    string = classify(tree, featureLabels, temp)
    if string=="yes":
        string=1
    else:
        string=0
    count.append(string)
    passengerid.append(test[0])
result = pd.DataFrame({'PassengerId':passengerid, 'Survived':count})
result.to_csv('titanic/telecom_churn.csv',index=False)
print(result)

