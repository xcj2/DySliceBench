#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/7
Update on 2019/3/
Solved on 2019/3/  
@author: shinjisu
"""


# Educational Dynamic Programming
# import math
#import numpy as np
#import sys
#sys.setrecursionlimit(10**6)


def getInt(): return int(input())


def getIntList(): return [int(x) for x in input().split()]
# def getIntList(): return np.array(input().split(), dtype=np.longlong)


def zeros(n): return [0]*n
# def zeros(n): return np.zeros(n, dtype=np.longlong)


def getIntLines(n): return [int(input()) for i in range(n)]
def getIntLines(n):
    data = zeros(n)
    for i in range(n):
        data[i] = getInt()
    return data


def getIntMat(n, m):  # n行に渡って、1行にm個の整数
    mat = zeros((n, m))
    #dmp(mat)
    for i in range(n):
        mat[i] = getIntList()
    return mat


def zeros2(n, m): return [zeros(m) for i in range(n)] # obsoleted zeros((n, m))で代替

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


def prob_H_v1():  # Grid 1    AC 10  TLE 6
    H, W = getIntList()
    dmp((H, W), 'H, W')
    a = []
    for i in range(H):
        a.append(input())
    dmp(a)
    WALL = '#'
    BLANK = '.'
    dp = zeros((H+1, W+1))
    dp[1, 1] = 1
    dmp(dp, 'dp initial')
    for i in range(H):
        for j in range(W):
            if a[i][j] == BLANK and (i > 0 or j > 0):
                dp[i+1, j+1] = (dp[i, j+1] + dp[i+1, j]) % N1097

    dmp(dp, 'dp')
    return dp[H, W]


def prob_H_v2():  # Grid 1  AC 11  TLE 5
    H, W = getIntList()
    dmp((H, W), 'H, W')
    a = []
    for i in range(H):
        a.append(input())
    dmp(a)
    WALL = '#'
    BLANK = '.'
    dp = zeros((H+1, W+1))
    dp[1, 1] = 1
    dmp(dp, 'dp initial')
    for i in range(1, H):
        if a[i][0] == BLANK:
            dp[i+1, 1] = dp[i, 1]
    for j in range(1, W):
        if a[0][j] == BLANK:
            dp[1, j+1] = dp[1, j]
    for i in range(1, H):
        for j in range(1, W):
            if a[i][j] == BLANK:
                dp[i+1, j+1] = (dp[i, j+1] + dp[i+1, j]) % N1097

    dmp(dp, 'dp')
    return dp[H, W]




def prob_H():  # Grid 1    AC 11  TLE 5
    H, W = getIntList()
    dmp((H, W), 'H, W')
    a = []
    for i in range(H):
        a.append(input())
    dmp(a)
    WALL = '#'
    BLANK = '.'
    dp = zeros2(H+1, W+1)
    dp[0][1] = 1  # [1,1]ではないことがポイント
    dmp(dp, 'dp initial')
    for i in range(H):
        for j in range(W):
            if a[i][j] == WALL:
                continue
            dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][ j]) % N1097

    dmp(dp, 'dp')
    return dp[H][ W]


debug = False  # True False
ans = prob_H()
print(ans)
#for row in ans:
#    print(row)

