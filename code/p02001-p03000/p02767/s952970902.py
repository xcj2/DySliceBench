import math
import copy
from copy import deepcopy
import sys
import fractions
import numpy as np
from functools import reduce
import statistics
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
data = getInputListInt()

data.sort()
min_num = sys.float_info.max

for i in range(data[0], data[len(data)-1]+1, 1):
    tmp_dis = 0
    for x in data:
        tmp_dis += float(pow(i - x, 2))
    min_num = min(min_num, tmp_dis)

print(int(min_num))