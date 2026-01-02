import math
import copy
from copy import deepcopy
import sys
import fractions
import numpy as np
from functools import reduce
# import statistics
import heapq


# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

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
n = getInputInt()
data = getSomeInputListInt(n)

data_sorted = sorted(data, key=lambda x:x[1], reverse=True)

lim = sys.maxsize
flg = True

for d in data_sorted:
    if lim > d[1]:
        lim = d[1]
    lim -= d[0]

    if lim<0:
        flg = False
        break

if flg:
    print("Yes")
else:
    print("No")