from numpy import *
l = zeros((5,4))#构建一个5*4的零矩阵
for i in range(5):#给该矩阵赋值
    for j in range(4):
        l[i][j] = i * 5 + j
print(l)#打印赋值后的矩阵
print(shape(l))#输出l的行列值
print(l.shape[0])#输出l的行数值
print(l.shape[1])#输出l的列数值
