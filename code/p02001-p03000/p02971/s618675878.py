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

n = getInputNum()

a = getSomeInputInt(n)

sorted_a= sorted(a, reverse=True)

maxNum = sorted_a[0]
second = sorted_a[1]

for i in range(n):
    if a[i] == maxNum:
        print(second)
    else:
        print(maxNum)







