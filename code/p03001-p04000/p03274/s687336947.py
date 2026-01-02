#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/1
Solved on 2019/3/  WA
@author: shinjisu
"""


# ABC 107 C Candles
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


ALPHABET = [chr(i+ord('a')) for i in range(26)]
DIGIT = [chr(i+ord('0')) for i in range(10)]
N1097 = 10**9 + 7
INF = 10**12


def dmp(x, cmt=''):
    global debug
    if debug:
        if cmt != '':
            print(cmt, ':  ', end='')
        print(x)
    return x


def probC_WA():
    N, K = getIntList()
    X = getIntList()
    dmp((N, K, X))
    X = [-INF] + X + [INF]
    dmp(X)
    for i in range(N+2):
        if X[i] >= 0:
            break
    zeroIdx = i
    dmp(zeroIdx, 'zeroIdx')
    fromIdx = max(1, zeroIdx-K+1)
    dmp(fromIdx, 'fromIdx')
    # X[fromIdx] = 0 if X[fromIdx] == -INF else X[fromIdx]
    minTime = INF
    # for i in range(fromIdx, N+2-fromIdx-K+1):
    # for i in range(fromIdx, N+2-K+1):
    for i in range(fromIdx, N+2-K):
        if X[i] >= 0:
            moveTime = X[i+K-1]
        elif X[i+K-1] <= 0:
            moveTime = abs(X[i])
        else:
            plDist = X[i+K-1]
            mnDist = abs(X[i])
            moveTime = min(plDist, mnDist)*2 + max(plDist, mnDist)
        dmp((i, minTime, moveTime), 'moveTime in loop')
        minTime = min(minTime, moveTime)
    return minTime


def probC():
    N, K = getIntList()
    X = getIntList()
    dmp((N, K, X))
    # X = [-INF] + X + [INF]
    # dmp(X)
    # for i in range(N+2):
    for i in range(N):
        if X[i] >= 0:
            break
    zeroIdx = i
    dmp(zeroIdx, 'zeroIdx')
    fromIdx = max(0, zeroIdx-K+1)
    dmp(fromIdx, 'fromIdx')
    # X[fromIdx] = 0 if X[fromIdx] == -INF else X[fromIdx]
    minTime = INF
    # for i in range(fromIdx, N+2-fromIdx-K+1):
    # for i in range(fromIdx, N+2-K+1):
    for i in range(fromIdx, N-K+1):
        if X[i] >= 0:
            moveTime = X[i+K-1]
        elif X[i+K-1] <= 0:
            moveTime = abs(X[i])
        else:
            plDist = X[i+K-1]
            mnDist = abs(X[i])
            moveTime = min(plDist, mnDist)*2 + max(plDist, mnDist)
        dmp((i, minTime, moveTime), 'moveTime in loop')
        minTime = min(minTime, moveTime)
    return minTime


debug = False  # True False
ans = probC()
print(ans)
#for row in ans:
#    print(row)
