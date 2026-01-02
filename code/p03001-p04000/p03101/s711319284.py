#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/9
Solved on 2019/3/9
@author: shinjisu
"""


# ABC 121
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
    H, W = getIntList()
    h, w = getIntList()
    dmp((H, W))
    dmp((h, w))
    ans = (H-h)*(W-w)
    return ans


debug = False  # True False
ans = prob_A()
print(ans)
#for row in ans:
#    print(row)


def prob_B():
    A, B, K = getIntList()
    dmp((A, B, K))
    count = 0
    i = 100
    while count < K:
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                break
        i -= 1
    return i


def prob_C():
    S = input()
    red = 0
    blue = 0
    for cube in S:
        if cube == '0':
            red += 1
        else:
            blue += 1
    dmp((red, blue))
    return min(red, blue)*2


def prob_D():
    global N, M, A, B
    N, M = getIntList()
    dmp((N, M))
    A = zeros(M)
    B = zeros(M)
    for i in range(M):
        A[i], B[i] = getIntList()
    dmp(A, 'A')
    dmp(B, 'B')
    count = dmp(countInconv(), 'orginal')
    for i in range(M):
        A[i] = -1
        B[i] = -1
        dmp(A, 'A')
        dmp(B, 'B')
        print(countInconv())
    return count


