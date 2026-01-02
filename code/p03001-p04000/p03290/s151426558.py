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

basecost = 100

##saiki
def dfs(i, total, cnt, nokori):
    global ans
    if i == d:
        if total < g:
            use = max(nokori)
            n = min(data[use - 1][0], -(-(g - total) // (use * basecost)))
            cnt += n
            total += n * use * basecost + data[use - 1][1]
        if total >= g:
            ans = min(ans, cnt)
    else:
        dfs(i + 1, total, cnt, nokori)
        dfs(i + 1, total + (i + 1) * data[i][0] * basecost + data[i][1], cnt + data[i][0], nokori - {i+1})


d, g = map(int, input().split())
data = getSomeInputListInt(d)

ans = sys.maxsize

dfs(0, 0, 0, set(range(1, d + 1)))
print(ans)
