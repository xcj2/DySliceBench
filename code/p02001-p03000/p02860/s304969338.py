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

def getInputStr():
    inputNum = str(input())
    return inputNum

n = getInputInt()

s = getInputStr()

tmplist = list(s)
listA = tmplist[0: int(len(s)/2)]
listB = tmplist[int(len(s)/2) : len(s)]

if listA == listB:
    print("Yes")
else:
    print("No")
