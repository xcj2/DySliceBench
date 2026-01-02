# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:50:41 2019

@author: shinjisu
"""


import math


def getInt(): return int(input())


def getIntList(): return [int(x) for x in input().split()]


def zeros(n): return [0]*n


def getIntLines(n): return [int(input()) for i in range(n)]


def getIntMat(n):
    mat = []
    for i in range(n):
        mat.append(getIntList())
    return mat


def dmp(x):
    global debug
    if debug:
        print(x)


# ABC 100 B Ringo's Favorite Numbers
def abc100b():
    D, N = getIntList()
    if N % 100 == 0:
        return (N+1) * 100**D  # WA N==100のとき正しくない 101*100**D
    else:
        return N * 100**D


# ABC 101 B digit sum
def abc101b():
    N = getInt()
    sm = 0
    n = N
    while n > 0:
        sm += n % 10
        n //= 10
    if N % sm == 0:
        return 'Yes'
    else:
        return 'No'


debug = False  # True False
print(abc101b())
