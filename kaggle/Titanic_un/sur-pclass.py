# coding: utf-8
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
trainData = pd.read_csv("titanic/train.csv")
testData = pd.read_csv("titanic/test.csv")
# 探索Pclass和是否幸存的关系
dead = [0, 0, 0]
alive = [0, 0, 0]
trainData = np.array(trainData)
for data in trainData:
    if data[1] == 0:
        dead[data[2] - 1] += 1
    else:
        alive[data[2] - 1] += 1
count_dead_1 = dead[0]
count_dead_2 = dead[1]
count_dead_3 = dead[2]
count_alive_1 = alive[0]
count_alive_2 = alive[1]
count_alive_3 = alive[2]
count_1=dead[0]+alive[0]
count_2=dead[1]+alive[1]
count_3=dead[2]+alive[2]
print('class dead ati: 1 is %0.3f%%, 2 is %0.3f%%, 3 is %0.3f%%' % (
count_dead_1 / count_1, count_dead_2 / count_2, count_dead_3 / count_3))
print('class alive rati: 1 is %0.3f%%, 2 is %0.3f%%, 3 is %0.3f%%' % (
count_alive_1 / count_1, count_alive_2 / count_2, count_alive_3 / count_3))
pos = [1, 2, 3]
ax = plt.figure(figsize=(8, 6)).add_subplot(111)
# plt.suptitle('经济阶层与是否幸存统计', fontsize=20)
ax.bar(pos, dead, color='r', alpha=0.6, label="死亡")
ax.bar(pos, alive, color='g', bottom=dead, alpha=0.6, label='幸存')
ax.legend(fontsize=16, loc='best')
ax.set_xticks(pos)
ax.set_xticklabels(['Pclass%d' % (i) for i in range(1, 4)], size=15)
ax.set_title(u'经济阶层与是否幸存统计', size=20)
plt.show()
