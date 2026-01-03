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
from operator import mul

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
        inputDataList = [int(n) - 1 for n in inputData]
        outputDataList.append(inputDataList)

    return outputDataList


# ===CODE===

n, m = map(int, input().split())

d = getSomeInputListInt(m)

path = []
for p in itertools.permutations(range(1, n), n-1):
    tmp = (0,) + p
    path.append(tmp)


def pathsearch(a, b):
    flga = False
    for tmp_d in d:
        if a in tmp_d and b in tmp_d:
            flga = True
            break

    return flga


ans = 0
for p in path:
    flg = True
    for i in range(1, n, 1):
        tmp = pathsearch(p[i - 1], p[i])
        if not tmp:
            flg = False
            break

    if flg:
        ans += 1

print(ans)
