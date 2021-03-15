from Ch02 import kNN
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
group,labels = kNN.createDataSet()
# kNN.classify0([0,0],group,labels,3)

a,b=kNN.file2matrix("datingTestSet.txt")
c,d,e=kNN.autoNorm(a)

kNN.datingClassTest()


kNN.classifyPerson()


# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(a[:,0],a[:,1], 15.0 * np.array(b),15.0 * np.array(b))
# plt.show()


# kNN.handwritingClassTest()
kNN.classifyWrite('trainingDigits/9_0.txt')