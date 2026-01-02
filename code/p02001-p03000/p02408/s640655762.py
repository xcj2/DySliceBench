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

n = int(input())
def getSomeInputListIntn(n):
    inputDataList = []
    outputDataList = []
    for i in range(n):
        inputData = input().split()
        inputDataList = [str(n) for n in inputData]
        outputDataList.append(inputDataList)

    return outputDataList
data = getSomeInputListIntn(n)

s = [int(i) for i in range(13)]
h = [int(i) for i in range(13)]
c = [int(i) for i in range(13)]
d = [int(i) for i in range(13)]

def checker(l, num):
    num = int(num)
    if l[num-1] == num-1:
        l[num-1] = -1

for suits, num in data:
    if suits == "S":
        checker(s, num)
    elif suits =="H":
        checker(h, num)
    elif suits =="C":
        checker(c, num)
    elif suits =="D":
        checker(d, num)

for i in range(13):
    if s[i] != -1:
        print("S", i+1)
for i in range(13):
    if h[i] != -1:
        print("H", i+1)
for i in range(13):
    if c[i] != -1:
        print("C", i+1)
for i in range(13):
    if d[i] != -1:
        print("D", i+1)
