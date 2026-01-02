#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 05:38:56 2019

@author: shinjisu
"""


# ABC 200点問題
import math


def getInt(): return int(input())


def getIntList(): return [int(x) for x in input().split()]


def zeros(n): return [0]*n


def dmp(x):
    global debug
    if debug:
        print(x)


debug = True


def getIntLines(n): return [int(input()) for i in range(n)]


def getIntMat(n):
    mat = []
    for i in range(n):
        mat.append(getIntList())
    return mat


def zeros2(n, m): return [zeros(m)]*n


def prob095():
    X = getIntList()
    K = getInt()
    dmp((X, K))
    total = sum(X) - max(X) + max(X)*2**K
    return total


debug = False
print(prob095())
