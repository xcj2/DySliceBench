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

n, k = map(int, input().split())
data = getInputListInt()

def calcCost(a, b):
    mina = abs(a)+abs(a-b)
    minb = abs(b)+abs(b-a)

    return min(mina, minb)

ans = sys.maxsize
for i in range(0, n-k+1, 1):
    tmpans = calcCost(data[i], data[i+k-1])
    ans = min(ans, tmpans)

print(ans)