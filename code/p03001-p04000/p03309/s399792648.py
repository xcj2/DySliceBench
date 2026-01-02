#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/2
Solved on 2019/3/
@author: shinjisu
"""


# ABC 102 C Linear Approximation
import statistics


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


def probC_WA_TLE():
    N = getInt()
    A = getIntList()
    dmp((N, A))
    a = [A[i]-i-1 for i in range(N)]
    dmp(a, 'a')
    m = int(statistics.mean(a))
    dmp(m, 'mean')
    s = int(statistics.pstdev(a)) + 2
    dmp(s, 'std dev')
    minSum = sum([abs(a[j]) for j in range(N)])
    dmp(minSum, 'minSum')
    for i in range(1, s):
        aSum = sum([abs(a[j]-m+i) for j in range(N)])
        dmp((aSum, -m+i), 'aSum, -m+i')
        minSum = min(minSum, aSum)
        aSum = sum([abs(a[j]-m-i) for j in range(N)])
        minSum = min(minSum, aSum)
        dmp((aSum, -m-i), 'aSum, -m-i')
        dmp(minSum, 'minSum')
    dmp(minSum, 'minSum')
    return minSum


def probC():
    N = getInt()
    A = getIntList()
    dmp((N, A))
    a = [A[i]-i-1 for i in range(N)]
    dmp(a, 'a')
    m = int(statistics.median(a))
    dmp(m, 'median')
    minSum = sum([abs(a[i]-m) for i in range(N)])
    dmp(minSum, 'minSum')
    return minSum


debug = False  # True False
ans = probC()
print(ans)
#for row in ans:
#    print(row)
