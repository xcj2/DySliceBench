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


# def getIntLines(n): return [int(input()) for i in range(n)]
def getIntLines(n):
    data = zeros(n)
    for i in range(n):
        data[i] = getInt()
    return data


def getIntMat(n):  # obsoleted
    mat = []
    for i in range(n):
        mat.append(getIntList())
    return mat
def getIntMat(n, m): # n行に渡って、1行にm個の整数
    mat = zeros((n, m))
    for i in range(n):
        mat[i] = getIntList()
    return mat


def zeros2(n, m): return [zeros(m)]*n # obsoleted zeros((n, m))で代替


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


def prob_D_incomplete():  # Knapsack 1
    N, W = getIntList()
    w = zeros(N)
    v = zeros(N)
    for i in range(N):
        w[i], v[i] = getIntList()
    dmp((N, W), 'N, W')
    dmp(w, 'w')
    dmp(v, 'v')
    dpw = zeros(N)
    dpv = [0]*N
    knap = zeros(N)  # ナップに入っているか否か
    dpw[0] = w[0]
    dpv[0] = v[0]
    knap[0] = 1
    for i in range(1, N):
        if dpw[i-1]+w[i] <= W:
            dpw[i] = dpw[i-1] + w[i]
            dpv[i] = dpv[i-1] + v[i]
            knap[i] = 1
            continue
        swap = -1
        maxV = -INF
        minW = INF
        for j in range(0, i):
            if v[i] > v[j] and knap[j] == 1 and dpw[i-1]-w[j]+w[i] <= W:
                if v[j] >= maxV:
                    maxV = v[j]
                    swap = j
            elif v[i] == v[j] and knap[j] == 1 \
                    and dpw[i-1]-w[j]+w[i] <= W and w[i] < w[j]:
                if w[j] <= minW:
                    minW = w[j]
                    swap = j
        if swap > 0:
            dpw[i] = dpw[i-1] - w[j] + w[i]
            dpv[i] = dpv[i-1] - v[j] + v[i]
            knap[i] = 1
            knap[j] = 0
        else:
            dpw[i] = dpw[i-1]
            dpv[i] = dpv[i-1]

    dmp(dpw, 'dpw')
    dmp(dpv, 'dpv')
    dmp(knap, 'knap')
    return dpv[N-1]


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
        dmp(w[i], 'w[i]')
        dp[w[i]:] = np.maximum(dp[w[i]:],
                               dp[:W-w[i]+1] + v[i])
    dmp(dp, 'dp')
    return dp[W]


def prob_E():  # Knapsack 2
    N, W = getIntList()
    w, v = zeros(N), zeros(N)
    dmp((N, W))
    for i in range(N):
        w[i], v[i] = getIntList()
    dmp(w, 'weight')
    dmp(v, 'value')
    dp = zeros(v.sum()+1)
    dp += w.sum()+1
    dp[0] = 0
    dmp(dp.size, 'dp.size')
    for i in range(N):
        dmp((w[i], v[i], dp), 'w[i], v[i], dp')
        #dp[v[i]:] = np.maximum(dp[v[i]:],
        #                       dp[:v.sum()-v[i]+1] + w[i])
        """
        for j in range(v[i], v.sum()+1):
            # dmp((j, dp[j]), 'j, dp[j]')
            if dp[j] == 0:
                dp[j] = dp[j-v[i]] + w[i]
                dmp((j,dp), '0-dp')
            elif dp[j] > dp[j-v[i]] + w[i]:
                dp[j] = dp[j-v[i]] + w[i]
                dmp((j,dp), 'dp')
        """
        dp[v[i]:] = np.minimum(dp[v[i]:],
                               dp[:v.sum()-v[i]+1] + w[i])
    dmp(dp, 'final dp')
    maxVal = 0
    minWeight = INF
    for i in range(len(dp)):
        if dp[i] <= W and i >= maxVal:
            maxVal = i
    dmp(maxVal)
    return maxVal


debug = False  # True False
ans = prob_E()
print(ans)
#for row in ans:
#    print(row)

