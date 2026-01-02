import math
import copy
import sys
import fractions
# import numpy as np
# import statistics
import decimal
import heapq
import collections
import itertools
import bisect


# from operator import mul

# sys.setrecursionlimit(100001)


# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# ===FUNCTION===

def getInputIntList():
    outputDataList = []
    inputData = input().split()
    outputDataList = [int(n) for n in inputData]

    return outputDataList


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

n = int(input())

data = getSomeInputListInt(n)

ans = [[] for _ in range(n)]

edge = []
for d in data:
    edge.append(d[2:])


def dfs(i, cnt):
    if len(ans[i]) > 0:
        return cnt

    cnt += 1

    ans[i].append(cnt)
    for j in range(len(edge[i])):
        cnt = dfs(edge[i][j], cnt)

    cnt += 1
    ans[i].append(cnt)

    return cnt

tmp = 0
for i in range(n):
    tmp = dfs(i, tmp)

for i in range(n):
    print(i + 1, *ans[i], sep=" ")

