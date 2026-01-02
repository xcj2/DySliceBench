#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/2
Solved on 2019/3/
@author: shinjisu
"""


# Educational Dynamic Programming
# import math
import numpy as np


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


def prob_A():  # Frog 1
    N = getInt()
    H = getIntList()
    dmp((N, H), 'N, H')
    c = zeros(N)
    c[1] = abs(H[1]-H[0])
    for i in range(2, N):
        c[i] = min(c[i-1] + abs(H[i]-H[i-1]),
                   c[i-2] + abs(H[i]-H[i-2]))
    dmp(c, 'c')
    return c[N-1]


def prob_B_TLE():  # Frog 2 3/16 TLE
    N, K = getIntList()
    H = getIntList()
    dmp((N, K, H), 'N, K, H')
    c = np.zeros(N)
    c[0] = 0
    for i in range(1, N):
        #c[i] = INF
        for j in range(max(0, i-K), i):
            c[i] = min(c[i], c[j] + abs(H[i]-H[j]))
    dmp(c, 'c')
    return c[N-1]


def prob_B():  # Frog 2 3/16 TLE
    N, K = getIntList()
    H = np.array(input().split(), dtype='int')
    dmp((N, K, H), 'N, K, H')
    c = np.zeros(N, dtype='int')
    c[0] = 0
    for i in range(1, N):
        c[i] = np.min(c[max(0, i-K):i] + np.abs(H[max(0, i-K):i] - H[i]))
    dmp(c, 'c')
    return c[N-1]


debug = False  # True False
ans = prob_B()
print(ans)
#for row in ans:
#    print(row)
