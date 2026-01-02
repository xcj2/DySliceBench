#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/2/
Solved on 2019/2/
@author: shinjisu
"""


# ABC 111 C /\/\/\/
def getInt(): return int(input())


def getIntList(): return [int(x) for x in input().split()]


def zeros(n): return [0]*n


def getIntLines(n): return [int(input()) for i in range(n)]


def getIntMat(n):
    mat = []
    for i in range(n):
        mat.append(getIntList())
    return mat


def zeros2(n, m): return [zeros(m)]*n


def dmp(x):
    global debug
    if debug:
        print(x)
    return x


def probC():
    N = getInt()
    V = getIntList()
    dmp((N, V))
    odd = {}
    even = {}
    for i in range(N):
        if i % 2 == 0:
            if V[i] in even:
                even[V[i]] += 1
            else:
                even[V[i]] = 1
        else:
            if V[i] in odd:
                odd[V[i]] += 1
            else:
                odd[V[i]] = 1
    dmp(('even',even))
    dmp(('odd',odd))
    evenList = [[even[k], k] for k in even]
    evenList.sort()
    evenList.reverse()
    dmp(evenList)
    oddList = [[odd[k], k] for k in odd]
    oddList.sort()
    oddList.reverse()
    dmp(oddList)
    if evenList[0][1] == oddList[0][1]:  # 度数最大の値が同一の場合
        if len(evenList) == 1 and len(oddList) == 1:
            evenMaxCount = evenList[0][0]
            oddMaxCount = 0
        elif len(evenList) > 1 and len(oddList) > 1:
            evenMaxCount = evenList[0][0]
            oddMaxCount = max(evenList[1][0], oddList[1][0])
        elif len(evenList) > 1:
            evenMaxCount = evenList[1][0]
            oddMaxCount = oddList[0][0]
        else:
            evenMaxCount = evenList[0][0]
            oddMaxCount = oddList[1][0]
    else:
        evenMaxCount = evenList[0][0]
        oddMaxCount = oddList[0][0]
    dmp(oddMaxCount)
    dmp(evenMaxCount)
    return N - evenMaxCount - oddMaxCount


debug = False  # True False
print(probC())
