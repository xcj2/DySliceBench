# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:50:41 2019

@author: shinjisu
"""


import math


def getInt(): return int(input())


def getIntList(): return [int(x) for x in input().split()]


def zeros(n): return [0]*n


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
        return N * 100**D  # WA N==100のとき正しくない 101*100**D


debug = False  # True False
print(abc100b())
