import math
import copy
import sys
import fractions
import numpy as np
from functools import reduce

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

n, A, B, C = map(int, input().split())
data = getSomeInputInt(n)

def dfs(cnt, a, b, c):
    if cnt == n:
        return abs(a-A)+abs(b-B)+abs(c-C)-30 if min(a,b,c) > 0 else sys.maxsize

    nothing = dfs(cnt+1, a, b, c)
    ap = dfs(cnt+1, a+data[cnt], b, c) + 10
    bp = dfs(cnt+1, a, b+data[cnt], c) + 10
    cp = dfs(cnt+1, a, b, c + data[cnt]) + 10

    return min(nothing, ap, bp, cp)

print(dfs(0, 0, 0, 0))