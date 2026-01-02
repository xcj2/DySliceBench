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
        inputDataList = [int(n) for n in inputData]
        outputDataList.append(inputDataList)

    return outputDataList


# ===CODE===

n = int(input())
obj = getSomeInputListInt(n)

data = [[] for _ in range(8)]
for x in range(8):
    for y in range(8):
        flg = True
        for o in obj:
            tmpx = o[0]-x
            tmpy = o[1]-y
            if tmpx == 0 or tmpy == 0 or abs(tmpx) == abs(tmpy):
                flg = False
                break

        if flg:
            data[x].append([x,y])



def checker(a, b_list):
    flg = True
    for b in b_list:
        tmpx = b[0] - a[0]
        tmpy = b[1] - a[1]
        if tmpx == 0 or tmpy == 0 or abs(tmpx) == abs(tmpy):
            flg = False
            break

    return flg

def printer(l):
    for x in range(8):
        for y in range(8):
            if [x,y] in l:
                print("Q", end="")
            else:
                print(".", end="")
        print("")


def search(cnt, candidate):
    if cnt == 8:
        printer(candidate)
        exit(0)
    if len(data[cnt]) == 0:
        search(cnt+1, candidate)


    for d in data[cnt]:
        if checker(d, candidate):
            tmp = copy.deepcopy(candidate)
            tmp.append(d)
            search(cnt+1, tmp)


search(0, obj)
