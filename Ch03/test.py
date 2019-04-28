from Ch03 import trees, treePlotter

fr = open("lenses.txt")
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
print(type(lenses))
labels = ['age','prescript','astigmatic','tearRate']
tree = trees.createTree(lenses,labels)
treePlotter.createPlot(tree)
print(tree)