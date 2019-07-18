# coding: utf-8
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
trainData = pd.read_csv("titanic/train.csv")
testData = pd.read_csv("titanic/test.csv")
'''Embacked和Survived的关系'''
trainData = np.array(trainData)
aliveCount = [0, 0, 0]  # S,Q,C
deadCount = [0, 0, 0]
pos = [1, 2, 3]
for data in trainData:
    if data[11] == 'S':
        if data[1] == 1:
            aliveCount[0] += 1
        else:
            deadCount[0] += 1
    else:
        if data[11] == 'Q':
            if data[1] == 1:
                aliveCount[1] += 1
            else:
                deadCount[1] += 1
        else:
            if data[1] == 1:
                aliveCount[2] += 1
            else:
                deadCount[2] += 1
print('embacked dead ati: S is %0.3f%%, Q is %0.3f%%, C is %0.3f%%' % (
deadCount[0] / (aliveCount[0] + deadCount[0]), deadCount[1] / (aliveCount[1] + deadCount[1]),
deadCount[2] / (aliveCount[2] + deadCount[2])))
ax = plt.figure(figsize=(8, 6)).add_subplot(111)
ax.bar(pos, deadCount, color='r', alpha=0.6, label='死亡')
ax.bar(pos, aliveCount, color='g', bottom=deadCount, alpha=0.6, label='幸存')
ax.legend(fontsize=16, loc='best')
ax.set_xticks(pos)
ax.set_xticklabels(['S', 'Q', 'C'], size=15)
ax.set_title('登船港口和能否幸存的关系', size=20)
plt.show()
