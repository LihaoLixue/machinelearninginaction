from numpy import *

from Ch04 import bayes

a,b=bayes.loadDataSet()
c=bayes.createVocabList(a)
trainMat=[]
for postinDoc in a:
    trainMat.append(bayes.setOfWords2Vec(c,postinDoc))
p0,p1,p2,=bayes.trainNB0(trainMat,b)