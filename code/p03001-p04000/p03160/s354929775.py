#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/2
Solved on 2019/3/
@author: shinjisu
"""


# Educational Dynamic Programming
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


debug = False  # True False
ans = prob_A()
print(ans)
#for row in ans:
#    print(row)
