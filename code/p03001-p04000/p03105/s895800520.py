#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/3
Solved on 2019/3/3
@author: shinjisu
"""


# ABC 120
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


def prob_A():
    A, B, C = getIntList()
    dmp((A, B, C))
    count = min(B // A, C)
    return count


debug = False  # True False
ans = prob_A()
print(ans)
#for row in ans:
#    print(row)


def prob_B():
    N = getInt()
    A = getIntList()
    dmp((N, A))
    return 123


def prob_C():
    N = getInt()
    A = getIntList()
    dmp((N, A))
    return 123


def prob_D():
    N = getInt()
    A = getIntList()
    dmp((N, A))
    return 123


