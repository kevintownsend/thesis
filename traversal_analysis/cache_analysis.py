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
    proc = Popen(["./x_vector_reuse_cache_line", matrices[i] + ".mtx", "512", "8"], stdout=PIPE)
    line = proc.stdout.read().decode('UTF-8')
    data = line.split(",")
    nnz = int(data[1])
    M = int(data[2])
    requests = int(data[0])
    cache_requests = int(data[3])

    proc = Popen(["./x_vector_reuse", matrices[i] + ".mtx", "512"], stdout=PIPE)
    line = proc.stdout.read().decode('UTF-8')
    data = line.split(",")
    nnz = int(data[1])
    M = int(data[2])
    requests = int(data[0])

    table.append([nnz/requests, requests/M, nnz/cache_requests, cache_requests/M, 100*cache_requests/requests - 100])

print(table)
#TODO: print table 1
print()
print("\\hline")
for i in range(len(matrices)):
    print(matrices[i], end='')
    for j in range(5):
        print(" & {0:0.1f}".format(table[i][j]), end='')
    print("\\\\")
