#!/usr/bin/env python3
from os import *
from os.path import *
from glob import *
from subprocess import *

matrixFiles = glob("*.mtx")
del matrixFiles[matrixFiles.index("example.mtx")]

i = 0
while(i < len(matrixFiles)):
    if("post" in matrixFiles[i]):
        del matrixFiles[i]
    else:
        i = i + 1

matrices = []
for i in range(len(matrixFiles)):
    matrices.append(matrixFiles[i][:-4])

table = []

for i in range(len(matrices)):
    matrixStats = []
    proc = Popen(["./delta_distribution", matrices[i] + ".mtx"], stdout=PIPE)
    line = proc.stdout.read().decode('UTF-8')
    data = line.split()
    cutoff = 0
    currSum = 0
    total = 0
    for j in range(len(data)):
        if(j == 2**cutoff and cutoff != 10):
            matrixStats.append(currSum)
            cutoff += 1
            currSum = 0
        currSum += int(data[j])
        total += int(data[j])
    matrixStats.append(currSum)
    print("len of matrixStats: " + str(len(matrixStats)))
    for j in range(len(matrixStats)):
        matrixStats[j] = matrixStats[j] / total * 100
    table.append(matrixStats)



averages = []
for i in range(11):
    total = 0
    matrixCount = len(matrices) - 1
    for j in range(len(matrices)):
        if(matrices[j] == "dense2"):
            continue
        total += table[j][i]
    averages.append(total / matrixCount)


print("\\hline")
for i in range(9):
    print(" & " + str(2**i), end="")
print(" \\\\")
print("\\hline")
for i in range(len(matrices)):
    print(matrices[i], end="")
    for j in range(11):
        print(" & {0:0.1f}\\%".format(table[i][j]), end="")
    print(" \\\\")

print("\\hline")
print("average", end="")
for i in range(11):
    print(" & {0:0.1f}".format(averages[i]), end="")
