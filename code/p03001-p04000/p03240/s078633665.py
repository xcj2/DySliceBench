import math
import copy
import sys
import fractions
import numpy as np
from functools import reduce

# ===FUNCTION===

def getInputInt():
    inputNum = int(input())
    return inputNum

def getInputListInt():
    outputoData = []
    inputData = input().split()
    outputData = [int(n) for n in inputData]

    return outputData

def getSomeInputInt(n):
    outputDataList = []
    for i in range(n):
        inputData = int(input())
        outputDataList.append(inputData)

    return outputDataList

def getSomeInputListInt(n):
    inputDataList = []
    outputDataList = []
    for i in range(n):
        inputData = input().split()
        inputDataList = [int(n) for n in inputData]
        outputDataList.append(inputDataList)

    return outputDataList

# ===CODE===

n, = map(int, input().split())
data = getSomeInputListInt(n)

rng = 101

def clc(i, j, h, x, y):
    return h + abs(i-x) + abs(j-y)

def clcdis(i, j, x, y):
    return abs(i-x) + abs(j-y)

ansi = 0
ansj = 0
ansh = 0

flgBreakI = False

for i in range(rng):
    for j in range(rng):
        flg = True
        tmp = 0
        hmax = 10**10

        for k in range(n):
            if data[k][2] == 0:
                hmax = min(hmax, clcdis(i, j, data[k][0], data[k][1]))
            else:
                if tmp == 0:
                   tmp = clc(i, j, data[k][2], data[k][0], data[k][1])
                else:
                    if tmp != clc(i, j, data[k][2], data[k][0], data[k][1]):
                        flg = False
                        break

        if flg and tmp <= hmax:
            ansi = i
            ansj = j
            ansh = tmp
            flgBreakI = True
            break

    if flgBreakI:
        break

print(ansi, ansj, ansh)


