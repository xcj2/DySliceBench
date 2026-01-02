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
        inputDataList = [int(n) for n in inputData]
        outputDataList.append(inputDataList)

    return outputDataList


# ===CODE===

n, m = map(int, input().split())

s = getSomeInputListInt(m)
p = getInputListInt()

s_bit = []

for tmp_s in s:
    tmp_bit = 0
    for i in range(1, tmp_s[0] + 1, 1):
        aaa = 1 << (tmp_s[i] - 1)
        tmp_bit = aaa | tmp_bit
    s_bit.append(tmp_bit)

ans = 0
for i in range(int(pow(2, n))):
    flg = True
    for j in range(m):
        cnt = bin(s_bit[j] & i).count("1")
        if cnt % 2 != p[j]:
            flg = False
            break
    if flg:
        ans += 1

print(ans)