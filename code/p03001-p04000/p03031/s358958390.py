import math
import copy
import fractions
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

n, m = map(int, input().split())

status = getSomeInputListInt(m)
condition = getInputListInt()

ans = 0
mask = []

for i in range(len(status)):
    mask.append(0b0)
    for j in range(1, status[i][0]+1):
        tmp = 1
        tmp = tmp << (status[i][j] - 1)
        mask[i] = mask[i] | tmp

for i in range(2**n):
    flg = True
    for j in range(m):
        masked = i & mask[j]
        oneCnt = bin(masked).count("1")
        if oneCnt % 2 != condition[j]:
            flg = False
            break

    if flg:
        ans += 1

print(ans)



