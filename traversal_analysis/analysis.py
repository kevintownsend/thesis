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

for i in range(len(matrices)):
    matrixStats = []
    for j in range(11):
        proc = Popen(["./x_vector_reuse", matrices[i] + ".mtx", str(2**j)], stdout=PIPE)
        line = proc.stdout.read().decode('UTF-8')
        data = line.split(",")
        nnz = int(data[1])
        M = int(data[2])
        requests = int(data[0])
        matrixStats.append([nnz/requests, requests/M])

        print(data)
    print(matrixStats)
    table.append(matrixStats)
    #TODO: run x vector analysis
    #TODO: capture output

#TODO: print table 1
print()
print("\\hline")
for i in range(len(matrices)):
    print(matrices[i], end='')
    for j in range(11):
        print(" & {0:0.1f}".format(table[i][j][0]), end='')
    print("\\\\")
    print("\\hline")

#TODO: print table 2
print()
print("\\hline")
for i in range(len(matrices)):
    print(matrices[i], end='')
    for j in range(11):
        print(" & {0:0.1f}".format(table[i][j][1]), end='')
    print("\\\\")
    print("\\hline")

#TODO: do something with data

#matrices = 
