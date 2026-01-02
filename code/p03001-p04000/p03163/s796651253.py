#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/2
Update on 2019/3/5
Solved on 2019/3/
@author: shinjisu
"""


# Educational Dynamic Programming
# import math
import numpy as np


def getInt(): return int(input())


# def getIntList(): return [int(x) for x in input().split()]
def getIntList(): return np.array(input().split(), dtype=np.longlong)


# def zeros(n): return [0]*n
def zeros(n): return np.zeros(n, dtype=np.longlong)


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
INF = 10**18


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


def prob_B():  # Frog 2
    N, K = getIntList()
    H = np.array(input().split(), dtype='int')
    dmp((N, K, H), 'N, K, H')
    c = np.zeros(N, dtype=np.longlong)
    c[0] = 0
    for i in range(1, N):
        c[i] = np.min(c[max(0, i-K):i] + np.abs(H[max(0, i-K):i] - H[i]))
    dmp(c, 'c')
    return c[N-1]


def prob_C():  # Vacation
    N = getInt()
    a = zeros(N)
    b = zeros(N)
    c = zeros(N)
    for i in range(N):
        a[i], b[i], c[i] = getIntList()
    dmp(N, 'N')
    dmp(a, 'a')
    dmp(b, 'b')
    dmp(c, 'c')
    dpa = zeros(N)
    dpb = zeros(N)
    dpc = zeros(N)
    dpa[0] = a[0]
    dpb[0] = b[0]
    dpc[0] = c[0]
    for i in range(1, N):
        dpa[i] += max(dpb[i-1], dpc[i-1]) + a[i]
        dpb[i] += max(dpc[i-1], dpa[i-1]) + b[i]
        dpc[i] += max(dpa[i-1], dpb[i-1]) + c[i]
    dmp(dpa, 'dpa')
    dmp(dpb, 'dpb')
    dmp(dpc, 'dpc')
    return max(dpa[N-1], dpb[N-1], dpc[N-1])


def prob_D():  # Knapsack 1
    N, W = getIntList()
    w, v = zeros(N), zeros(N)
    dmp((N, W))
    for i in range(N):
        w[i], v[i] = getIntList()
    dmp(w, 'weight')
    dmp(v, 'value')
    dp = zeros(W+1)
    dmp(dp.size)
    for i in range(N):
        dmp(dp, 'dp')
        dmp(w[i],'w[i]')
        #prevIdx = max(0, i-w[i])
        #dmp(prevIdx,'prevIdx')
        dmp(w[i],'w[i]')
        dp[w[i]:] = np.maximum(dp[w[i]:], 
                                  dp[:W-w[i]+1] + v[i])
    dmp(dp, 'dp')
    return dp[W]


debug = False  # True False
ans = prob_D()
print(ans)
#for row in ans:
#    print(row)

