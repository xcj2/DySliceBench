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


def prob096():  # Maximum Sum
    X = getIntList()
    K = getInt()
    dmp((X, K))
    total = sum(X) - max(X) + max(X)*2**K
    return total


def prob097():  # Exponential
    X = getInt()
    dmp(X)
    if X == 1:
        return 1
    for n in range(X, 0, -1):
        dmp(n)
        for b in range(2, int(math.sqrt(X))+1):
            a = n
            exp = True
            while a > 1:
                if a % b != 0:
                    exp = False
                    break
                a //= b
            if exp:
                break
        if exp:
            break
    return n


def prob098():  # Cut and Count
    N = getInt()
    S = input()
    dmp((N, S))
    maxChCount = 0
    for i in range(1, N):
        before = S[:i]
        after = S[i:]
        dmp((before, after))
        chCount = 0
        for j in range(26):
            ch = chr(ord('a')+j)
            if ch in before and ch in after:
                chCount += 1
        maxChCount = max(maxChCount, chCount)
    return maxChCount


debug = False  # True False
print(prob098())
