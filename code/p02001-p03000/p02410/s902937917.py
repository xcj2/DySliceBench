import math
import copy
from copy import deepcopy
import sys
import fractions
# import numpy as np
from functools import reduce
# import statistics
import decimal
import heapq
import collections
import itertools
sys.setrecursionlimit(100001)

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
n, m = map(int, input().split())
a = getSomeInputListInt(n)
b = getSomeInputInt(m)

ans = 0
for i in range(n):
    for j in range(m):
        a[i][j] *= b[j]
    print(sum(a[i]))


