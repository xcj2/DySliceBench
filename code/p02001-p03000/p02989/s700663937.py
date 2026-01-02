import math
import copy
# import numpy as np

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

a = getInputNum()
b = getInputListInt()

c = sorted(b)

mean = c[int(a/2)-1]
next = c[int(a/2 + 1)-1]

ans = next - mean

print(ans)
