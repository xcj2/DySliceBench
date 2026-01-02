#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/23
Solved on 2019/3/
@author: shinjisu
"""


# ABC 0xx C xxx
#import math
#import numpy as np

def getInt(): return int(input())

def getIntList(): return [int(x) for x in input().split()]
# def getIntList(): return np.array(input().split(), dtype=np.longlong)

def zeros(n): return [0]*n
# def zeros(n): return np.zeros(n, dtype=np.longlong)

def getIntLines(n): return [int(input()) for i in range(n)]


def zeros2(n, m): return [zeros(m) for i in range(n)] # obsoleted zeros((n, m))で代替


class Debug():
    def __init__(self):
        self.debug = True
 
    def off(self):
        self.debug = False
 
    def dmp(self, x, cmt=''):
        if self.debug:
            if cmt != '':
                print(cmt, ':  ', end='')
            print(x)
        return x


def prob():
    d = Debug()
    d.off()
    N = getInt()
    d.dmp((N), 'N')
    A = getIntList()
    d.dmp((A), 'A')
    dic = {}
    for e in A:
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1
    d.dmp((dic), 'dic')
    side = []
    for k in dic.keys():
        if dic[k] >= 4:
            side.append(k)
            side.append(k)
        elif dic[k] >= 2:
            side.append(k)
    side.sort()
    d.dmp((side), 'side')
    if len(side) >= 2:
        return side[-1]*side[-2]
    else:
        return 0


ans = prob()
print(ans)
