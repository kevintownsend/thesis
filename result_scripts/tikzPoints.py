#!/usr/bin/env python2
uVal = [1, 1574940, 107, 1, 1, 132862, 118306, 3584, 282665, 673, 1383, 73230, 271382, 531668, 806653]
uValLog = [0.0, 6.197264013258786, 2.0293837776852097, 0.0, 0.0, 5.123400785682125, 5.0730067708393705, 3.5543680009900878, 5.451272036830906, 2.828015064223977, 3.1408221801093106, 4.864689034136851, 5.433, 5.725640521811938, 5.906686753316721]
#r3Flop = [13.6, 8.7, 12.7, 13.6, 12.8, 7.9, 5.9, 6.2, 6.2, 2.1, 3.8, 3.3, 5.2, 4.9, 6.4]
#r3Flop = [14.1, 13.3, 12.7, 13.6, 12.8, 7.9, 5.9, 6.2, 6.2, 2.1, 3.8, 3.3, 5.2, 4.9, 6.4]
r3Flop = [13.5, 10.1, 13.3, 13.9, 13.4, 10.2, 11.1, 11.5, 10.9, 2.1, 4.35, 4.75, 10.3, 11.4, 11.1]
r3FlopScale = [3.4, 2.175, 3.175, 3.4, 3.2, 1.975, 1.475, 1.55, 1.55, 0.55, 1.0, 0.85, 1.3, 1.225, 1.6]
matrices = ["dense", "consph", "cant", "rma10", "qcd5\_4", "shipsec1", "mac\_econ\_fwd500", "mc2depi", "scircuit", "dw8192", "t2d\_q9", "epb1", "raefsky1", "psmigr\_2", "torso2"]

#r3NewFlop = [13.6, 8.7, 12.7, 13.6, 12.8, 7.9, 5.9, 6.2, 6.2, 2.1, 3.8, 3.3, 5.2, 4.9, 6.4]


coord = []
for i in range(len(uVal)):
    coord.append([matrices[i], uVal[i], r3Flop[i], uValLog[i], r3FlopScale[i]])

coordSort = sorted(coord, key=lambda a: a[3])
#print coordSort

for i in range(len(coordSort)):
    print repr(i) + "/" + repr(coordSort[i][3]) + "/" + repr(coordSort[i][4]) + "/" + coordSort[i][0] + "/" + repr(coordSort[i][1]) + "/" + repr(coordSort[i][2]) + "/0,%"

hc1Flop = [1.7, 2.5, 2.6, 3.9, 3.9, 1.2]
teslaFlop = [0.5, 0.9, 0.8, 2.6, 2.8, 3.0]

gtxFlop = [16, 14, 11, 8, 14, 13, 5, 12, 6]
intelFlop = [14, 11, 12, 24, 30, 10, 23, 21, 12]

m2090Flop = [23, 15, 17, 11, 20, 11, 6, 22, 6]



for i in range(9, 15):
    coord[i].append(coord[i][2]/5.0)
    coord[i].append(hc1Flop[i-9])
    coord[i].append(hc1Flop[i-9]/5.0)
    coord[i].append(teslaFlop[i-9])
    coord[i].append(teslaFlop[i-9]/5.0)
    for j in range(4):
        coord[i].append(0)

for i in range(0,9):
    coord[i].append(coord[i][2]/5.0)
    for j in range(4):
        coord[i].append(0)
    coord[i].append(gtxFlop[i])
    coord[i].append(gtxFlop[i]/5.0)
    coord[i].append(intelFlop[i])
    coord[i].append(intelFlop[i]/5.0)
    
nnzS = [4000000, 6010480, 4007383, 2329092, 1916928, 3568176, 1273389, 2100225, 958936, 41746, 87025, 95053, 294276, 540022, 1033473]
for i in range(15):
    coord[i].append(nnzS[i])
    coord[i].append(nnzS[i]/500000.0)

for i in range(0,9):
    coord[i].append(m2090Flop[i])
    coord[i].append(m2090Flop[i]/5.0)

for i in range(9, 15):
    for j in range(2):
        coord[i].append(0)

coordSort = sorted(coord, key=lambda matrix: matrix[14])
print "R3"
for i in range(len(coordSort)):
    print repr(i) + "/" + repr(coordSort[i][15]) + "/" + repr(coordSort[i][5]) + "/" + repr(coordSort[i][2]) + "/0/0,%"
print "hc1"
for i in range(len(coordSort)):
    print repr(i) + "/" + repr(coordSort[i][15]) + "/" + repr(coordSort[i][7]) + "/" + repr(coordSort[i][6]) + "/0/0,%"
print "tesla"
for i in range(len(coordSort)):
    print repr(i) + "/" + repr(coordSort[i][15]) + "/" + repr(coordSort[i][9]) + "/" + repr(coordSort[i][8]) + "/0/0,%"
print "gtx"
for i in range(len(coordSort)):
    print repr(i) + "/" + repr(coordSort[i][15]) + "/" + repr(coordSort[i][11]) + "/" + repr(coordSort[i][10]) + "/0/0,%"
print "intel"
for i in range(len(coordSort)):
    print repr(i) + "/" + repr(coordSort[i][15]) + "/" + repr(coordSort[i][13]) + "/" + repr(coordSort[i][12]) + "/0/0,%"

print "m2090"
for i in range(len(coordSort)):
    print repr(i) + "/" + repr(coordSort[i][15]) + "/" + repr(coordSort[i][17]) + "/" + repr(coordSort[i][16]) + "/0/0,%"

print "lines"
for i in range(len(coordSort)):
    print "\draw [dashed] (" + repr(coordSort[i][15]) + ", -.5) -- (" + repr(coordSort[i][15]) + ", 7)  node [midway,above, sloped]{\small " + coordSort[i][0] + " $(" + format(coordSort[i][14]/1000000.0, '.2f') + "M)$};"

print "R3"
for i in range(len(coordSort) - 1):
    print repr(i) + "/" + repr(coordSort[i][5]) + "/" + repr(i+1) + "/" + repr(coordSort[i+1][5]) + ", ",
print

print "hc1"
for i in range(len(coordSort) - 1):
    print repr(i) + "/" + repr(coordSort[i][7]) + "/" + repr(i+1) + "/" + repr(coordSort[i+1][7]) + ", ",
print

print "tesla"
for i in range(len(coordSort) - 1):
    print repr(i) + "/" + repr(coordSort[i][9]) + "/" + repr(i+1) + "/" + repr(coordSort[i+1][9]) + ", ",
print

print "gtx"
for i in range(len(coordSort) - 1):
    print repr(i) + "/" + repr(coordSort[i][11]) + "/" + repr(i+1) + "/" + repr(coordSort[i+1][11]) + ", ",
print

print "intel"
for i in range(len(coordSort) - 1):
    print repr(i) + "/" + repr(coordSort[i][13]) + "/" + repr(i+1) + "/" + repr(coordSort[i+1][13]) + ", ",
print

print "m2090"
for i in range(len(coordSort) - 1):
    print repr(i) + "/" + repr(coordSort[i][17]) + "/" + repr(i+1) + "/" + repr(coordSort[i+1][17]) + ", ",
print

print "x axis"
for i in range(len(coordSort)):
    print repr(i) + "/" + coordSort[i][0] + "/" + repr(coordSort[i][14]) + ",",
print
