from Ch12 import fpGrowth
first = fpGrowth.loadSimpDat()
second = fpGrowth.createInitSet(first)
three,four=fpGrowth.createTree(second)
three.disp()
print(four)
