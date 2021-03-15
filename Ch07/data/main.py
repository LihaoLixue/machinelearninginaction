import Ch07.adaboost as adaboost
import Ch07.data.demo as demo
a,b = demo.loadDataSet('forestfires.csv')
c,d=adaboost.adaBoostTrainDS(a,b,100000)
# e=adaboost.adaClassify(a,c)
# demo.errArr(e,b)