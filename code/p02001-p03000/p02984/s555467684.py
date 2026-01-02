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

N = getInputInt()
A = getInputListInt()

s_sum = sum(A)

ans = [None] * N

ans[0] = s_sum
for i in range(1, N, 2):
    ans[0] -= 2 * A[i]

for i in range(N - 1):
    ans[i + 1] = 2 * A[i] - ans[i]

print(*ans)