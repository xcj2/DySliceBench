#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/2/16
Solved on 2019/2/16
@author: shinjisu
"""


# ABC 118
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


def dmp(x):
    global debug
    if debug:
        print(x)
    return x


def gcd(x, y):  # 最大公約数
    m = max(x, y)
    n = min(x, y)
    while m % n != 0:
        w = m % n
        m = n
        n = w
    return n


def probC():
    N = getInt()
    A = getIntList()
    dmp((N, A))
    hp = A[N-1]
    for i in range(N-1):
        hp = gcd(hp, A[i])
        dmp(hp)
    return hp


debug = False  # True False
print(probC())


def probD():
    N = getInt()
    A = getIntList()
    dmp((N, A))
    return 123


def probA():
    A, B = getIntList()
    dmp((A, B))
    if B % A == 0:
        return A+B
    else:
        return B-A


def probB():
    N, M = getIntList()
    A = getIntMat(N)
    dmp((N, M))
    dmp(A)
    food = set([])
    food = set(A[0][1:])
    dmp(food)
    for i in range(N):
        food2 = set(A[i][1:])
        food = food & food2
        dmp(food)
    return len(food)


