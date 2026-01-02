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

sys.setrecursionlimit(100001)


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
        inputDataList = [int(n) for n in inputData]
        outputDataList.append(inputDataList)

    return outputDataList


# ===CODE===

def dfs(x, y):
    flg = False
    if data[x][y] == 0 or table[x][y] == 1:
        return False
    else:
        table[x][y] = 1
        flg = True


    for i in range(x - 1, x + 2):
        if i < 0 or i > h-1:
            continue
        for j in range(y - 1, y + 2):
            if j < 0 or j > w-1:
                continue
            if not(x == i and y == j):
                tmp = dfs(i, j)

    return flg


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    data = getSomeInputListInt(h)
    table = [[0 for _ in range(w)] for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                ans += 1

    print(ans)

