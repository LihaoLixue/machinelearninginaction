from Ch11 import apriori

mushDatSet = [line.split() for line in open('mushroom.dat').readlines()]
L, suppData = apriori.apriori(mushDatSet, minSupport = 0.3)
for item in L[2]:
    if item.intersection('2'):
        print (item)