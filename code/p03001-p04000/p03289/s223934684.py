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
    return x


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


# ABC 102 B Maximum Difference
def abc102b():
    N = getInt()
    A = getIntList()
    return max(A) - min(A)


# ABC 104 B AcCepted
def abc104b():
    S = input()
    WA = 'WA'
    AC = 'AC'
    ALPHABET = [chr(i+ord('a')) for i in range(26)]
    dmp(ALPHABET)

    if S[0] != 'A':
        dmp(('A',WA))
        return WA

    cFound = False
    for i in range(1, len(S)):
        if S[i] in ALPHABET:
            pass
        elif S[i] == 'C':
            if i >= 2 and i <= len(S)-2 and not cFound:
                cFound = True
            else:
                dmp(('C',WA))
                return WA
        else:
            dmp(('alpha',WA))
            return WA
    else:
        if cFound:
            return AC
        else:
            return WA


debug = False  # True False
print(abc104b())
