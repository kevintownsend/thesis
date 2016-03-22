#!/usr/bin/env python3
import os
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

csrGz = [0.40, 0.19, 1.07, 0.03, 1.48, 1.78, 0.14, 0.17, 0.31, 0.20, 1.61, 0.86, 1.35]

table = []

for i in range(len(matrices)):
    #TODO: get M N nnz info
    matrixFile = open(matrices[i] + ".mtx", "r")
    matrixFile.readline()
    line = matrixFile.readline().split()
    M = int(line[0])
    N = int(line[1])


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

    proc = Popen(["./cvbv", matrices[i] + ".mtx"], stdout=PIPE)
    line = proc.stdout.read().decode('UTF-8')
    proc.wait()
    data = line.split(",")
    bits = float(data[0].strip())
    nnz = float(data[1].strip())

    csr = nnz * 32 + M * 32

    proc = Popen(["./kourtis", matrices[i] + ".mtx"], stdout=PIPE)
    line = proc.stdout.read().decode('UTF-8')
    proc.wait()
    data = line.split(",")
    kourtisBits = float(data[0].strip())

    #TODO: SMC
    proc = Popen(["../repos/convey_spmv/src/smac/smac", "-c", matrices[i] + ".mtx", matrices[i] + ".smac"])
    proc.wait()
    proc = Popen(["../repos/convey_spmv/src/smac/smac", "-d", matrices[i] + ".smac", matrices[i] + "post.mtx"])
    proc.wait()
    proc = Popen(["../repos/convey_spmv/src/smac/spMatrixHelp/spm", "-c", matrices[i] + "post.mtx", matrices[i] + ".smc"])
    proc.wait()
    statinfo = os.stat(matrices[i] + ".smc")
    smcBytes = statinfo.st_size


    #TODO: SMC.gz
    proc = Popen(["gzip", "-k", "-f", matrices[i] + ".smc"])
    proc.wait()
    statinfo = os.stat(matrices[i] + ".smc.gz")
    smcGzBytes = statinfo.st_size

    table.append([8.0, csr / nnz / 8, csrGzTotal / nnz, bits / nnz / 8, kourtisBits / nnz / 8, smcBytes / nnz, smcGzBytes / nnz])

#TODO average
averages = []
for i in range(7):
    total = 0
    matrixCount = len(matrices) - 1
    for j in range(len(matrices)):
        if(matrices[j] == "dense2"):
            continue
        total += table[j][i]
    averages.append(total / matrixCount)


#TODO: print table 1
print("\\hline")
for i in range(len(matrices)):
    print(matrices[i], end="")
    for j in range(7):
        print(" & {0:0.2f}".format(table[i][j]), end="")
    print(" \\\\")
print("\\hline")
print("average", end="")
for i in range(7):
    print(" & {0:0.2f}".format(averages[i]), end="")
