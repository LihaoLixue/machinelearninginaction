from Ch02 import kNN_lih as knn
a,b=knn.loadDataSet()
c,d =knn.gradAscent(a,b)
print(c)
print(d)