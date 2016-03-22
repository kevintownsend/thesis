#!/usr/bin/env python3
import os
from os.path import *
from glob import *
from subprocess import *
from math import *

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
nonPatternMatrices = []

for i in range(len(matrices)):
    #TODO: get M N nnz info
    matrixFile = open(matrices[i] + ".mtx", "r")
    line = matrixFile.readline()
    if("pattern" in line):
        continue
    nonPatternMatrices.append(matrices[i])
    line = matrixFile.readline().split()
    M = int(line[0])
    N = int(line[1])
    proc = Popen(["./cvbv", matrices[i] + ".mtx"], stdout=PIPE)
    line = proc.stdout.read().decode('UTF-8')
    proc.wait()
    data = line.split(",")
    bits = float(data[0].strip())
    nnz = float(data[1].strip())


    #TODO: csr.gz
    proc = Popen(["./decompose", matrices[i] + ".mtx"])
    proc.wait()
    proc = Popen(["gzip", "-k", "-f", matrices[i] + ".row"])
    proc.wait()
    proc = Popen(["gzip", "-k", "-f", matrices[i] + ".val"])
    proc.wait()
    proc = Popen(["gzip", "-k", "-f", matrices[i] + ".col"])
    proc.wait()
    proc = Popen(["gzip", "-k", "-f", matrices[i] + ".compressedRow"])
    proc.wait()
    statinfo = os.stat(matrices[i] + ".compressedRow.gz")
    csrGzTotal = statinfo.st_size
    statinfo = os.stat(matrices[i] + ".col.gz")
    csrGzTotal += statinfo.st_size

    #TODO: fzip
    proc = Popen(["../repos/convey_spmv/src/smac/fzip/fzip", "-c", matrices[i] + ".val", matrices[i] + ".fz"])
    proc.wait()
    statinfo = os.stat(matrices[i] + ".fz")
    fzBytes = statinfo.st_size


    proc = Popen(["gzip", "-k", "-f", matrices[i] + ".val"])
    proc.wait()
    statinfo = os.stat(matrices[i] + ".val.gz")
    smcGzBytes = statinfo.st_size

    table.append([(nnz * 8) / fzBytes, (nnz * 8) / smcGzBytes])

#TODO average
matrices = nonPatternMatrices
averages = []
for i in range(2):
    total = 1.0
    matrixCount = len(matrices)
    for j in range(len(matrices)):
        total = total * table[j][i]
    averages.append(pow(total, 1.0 / matrixCount))

newOrder = ["pdb1HYS", "consph", "cant", "pwtk", "shipsec1", "mac_econ_fwd500", "mc2depi", "cop20k_A", "scircuit", "webbase-1M"]

for i in range(len(newOrder)):
    for j in range(len(matrices)):
        if(newOrder[i] == matrices[j]):
            print(str(i + 1) + "/" + str(log(table[j][0],2) + 1), end="")
    print(",", end="")
print("11/" + str(log(averages[0],2) + 1))
print()

print()
for i in range(len(newOrder)):
    for j in range(len(matrices)):
        if(newOrder[i] == matrices[j]):
            print("\\node[black,anchor=west] at (" + str(log(table[j][0],2) + 1) + "," + str(i + 1.3) + "){{{0:0.2f}}};".format(table[j][0]))
    print(",", end="")

print("\\node[black,anchor=west] at (" + str(log(averages[0],2) + 1) + "," + str(11.3) + "){{{0:0.2f}}};".format(averages[0]))
