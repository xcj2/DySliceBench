#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 06:50:02 2019

@author: shinjisu
"""


def getIntList(): return [int(x) for x in input().split()]


def getIntMat(n):
    mat = []
    for i in range(n):
        mat.append(getIntList())
    return mat


def db(x):
    global debug
    if debug:
        print(x)


def solve():
    if c[1][0] - c[0][0] != c[1][1] - c[0][1] or \
        c[1][0] - c[0][0] != c[1][2] - c[0][2]:
        return False
    if c[2][0] - c[0][0] != c[2][1] - c[0][1] or \
        c[2][0] - c[0][0] != c[2][2] - c[0][2]:
        return False
    return True


debug = False
c = getIntMat(3)
db(c)
if solve():
    print('Yes')
else:
    print('No')
