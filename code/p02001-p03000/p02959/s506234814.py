import math
import copy
import sys
import numpy as np

# ===FUNCTION===

def getInputNum():
    inputNum = int(input())
    return inputNum

def getInputListInt():
    outputoData = []
    inputData = input().split()
    outputData = [int(n) for n in inputData]

    return outputData

def getSomeInputInt(n):
    inputDataList = []
    outputDataList = []
    for i in range(n):
        inputData = input().split()
        inputDataList = [int(n) for n in inputaNum]
        outputDataList.append(inputDataList)

    return outputDataList

# ===CODE===

n = getInputNum()

a = getInputListInt()
b = getInputListInt()

b.append(0)

ans = 0
tmp = 0

for i in range(n + 1):
    if a[i] >= b[i] + tmp:
        ans += b[i] + tmp
        tmp = 0
    else:
        ans += a[i]
        preyusyacalc = a[i] - tmp
        preyusyacalc = max(0, preyusyacalc)
        tmp = b[i] - preyusyacalc

print(ans)


