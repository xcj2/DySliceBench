#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/
Solved on 2019/3/
@author: shinjisu
"""


# ABC 076 C Explanation
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


def getIntMat(n, m):  # n行に渡って、1行にm個の整数
    mat = zeros((n, m))
    dmp(mat)
    for i in range(n):
        mat[i] = getIntList()
    return mat


# def zeros2(n, m): return [zeros(m)]*n # obsoleted zeros((n, m))で代替


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


def prob_B():
    x1, y1, x2, y2 = getIntList()
    dmp((x1, y1, x2, y2))
    dx = x2-x1
    dy = y2-y1
    dmp((dx, dy), 'dx, dy')
    dx, dy = -dy, dx
    dmp((dx, dy), 'dx, dy')
    x3, y3 = x2+dx, y2+dy
    dmp((x3, y3), 'x3, y3')
    dx, dy = -dy, dx
    x4, y4 = x3+dx, y3+dy
    return x3, y3, x4, y4


debug = False  # True False
ans = prob_B()
#print(ans)
#for row in ans:
#    print(row)
for elm in ans:
    print(elm, end=' ')
