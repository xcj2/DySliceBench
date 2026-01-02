#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/2
Solved on 2019/3/
@author: shinjisu
"""


# ABC 108 C Triangular Relationship
def getInt(): return int(input())


def getIntList(): return [int(x) for x in input().split()]


def dmp(x, cmt=''):
    global debug
    if debug:
        if cmt != '':
            print(cmt, ':  ', end='')
        print(x)
    return x


def probC():
    N, K = getIntList()
    dmp((N, K))
    n = N // K
    if K % 2 == 0:
        h = n + (N % K) // (K//2)
    else:
        h = 0
    dmp((n, h), 'n,h')
    cn = n**3
    ch = h**3
    dmp((cn, ch), 'n**3,h**3')
    return cn + ch


debug = False  # True False
print(probC())
