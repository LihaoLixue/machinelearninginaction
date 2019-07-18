from sklearn import tree
from sklearn.datasets import load_iris
import pydotplus

# 载入sklearn中自带的数据Iris，构造决策树

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

# # 训练完成后，我们可以用 export_graphviz 将树导出为 Graphviz 格式，存到文件iris.dot中
# with open("iris.dot", 'w') as f:
#     f = tree.export_graphviz(clf, out_file=f)
dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('iris.pdf')