#!/usr/bin/env python3
from os import *
from os.path import *
from glob import *
from subprocess import *

matrixFiles = glob("*.mtx")
del matrixFiles[matrixFiles.index("example.mtx")]


matrices = []
for i in range(len(matrixFiles)):
    matrices.append(matrixFiles[i][:-4])

table = []
dim = 11

for i in range(len(matrices)):
    matrixStats = []
    for j in range(dim):
        matrixStats.append([])
        for k in range(dim):
            proc = Popen(["./delta_bits", matrices[i] + ".mtx", str(2**j), str(2**k)], stdout=PIPE)
            line = proc.stdout.read().decode('UTF-8')
            data = float(line.strip())
            print(data)
            matrixStats[j].append(data)
    print(matrixStats)
    table.append(matrixStats)

#average
averages = []
for i in range(dim):
    averages.append([])
    for j in range(dim):
        averages[i].append([])
        total = 0
        for k in range(len(table)):
            total = total + table[k][i][j]
        averages[i][j] = total / len(table)

maxEstimate = 0
maxEstimateCoo = [9,2]
maxEstimateIndex = 0

for i in range(len(table)):
    if(table[i][maxEstimateCoo[0]][maxEstimateCoo[1]] > maxEstimate):
        maxEstimate = table[i][maxEstimateCoo[0]][maxEstimateCoo[1]]
        maxEstimateIndex = i
print(table)
print("maxEstimateIndex: " + str(maxEstimateIndex))


#TODO: print table 1
print("\\hline")
for i in range(dim):
    print(" & " + str(2**i), end="")
print(" \\\\")
print("\\hline")
for i in range(dim):
    print(2**i, end="")
    for j in range(dim):
        print(" & {0:0.2f}".format(averages[i][j]), end="")
    print(" \\\\")
    print("\\hline")
#print(" & {0:0.1f}".format(table[i][j][0]), end='')

#TODO: print table 2
print()
print("\\hline")
for i in range(dim):
    print(" & " + str(2**i), end="")
print(" \\\\")
print("\\hline")
for i in range(dim):
    print(2**i, end="")
    for j in range(dim):
        print(" & {0:0.2f}".format(table[maxEstimateIndex][i][j]), end="")
    print(" \\\\")
    print("\\hline")
