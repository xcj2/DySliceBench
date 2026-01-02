#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/9
Solved on 2019/3/9
@author: shinjisu
"""


# ABC 121
# import math


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


def prob_C():
    N, M = getIntList()
    dmp((N, M))
    BA = zeros(N)
    for i in range(N):
        BA[i] = getIntList()
    dmp(BA, 'BA')
    BA.sort()
    dmp(BA, 'BA')
    count = 0
    yen = 0
    for i in range(N):
        buyCount = min(BA[i][1], M-count)
        yen += buyCount * BA[i][0]
        count += buyCount
        dmp((buyCount, count, yen), 'buyCount, count, yen')
        if buyCount >= M:
            break
    dmp(yen, 'yen')
    return yen


debug = False  # True False
ans = prob_C()
print(ans)
#for row in ans:
#    print(row)


