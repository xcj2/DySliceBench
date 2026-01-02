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
    outputData = []
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

def gettwice(n):
    counter = 0
    flg = True
    while (flg):
        if n % 2 == 1:
            flg = False
        else:
            n = n / 2
            counter += 1

    return counter


n = getInputInt()
data = getInputListInt()

ans = 0

for i in range(len(data)):
    ans += gettwice(data[i])

print(ans)
