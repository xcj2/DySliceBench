import math
import copy
import sys
import fractions
import numpy as np
from functools import reduce
import statistics


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

n = getInputInt()
data = getInputListInt()

for i in range(n):
    data[i] = data[i] - (i + 1)

ave = statistics.median(data)



ans = 0

for i in range(n):
    ans += abs(data[i] - ave)

print(int(ans))