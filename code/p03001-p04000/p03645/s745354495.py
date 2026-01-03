#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/23
Solved on 2019/3/
@author: shinjisu
"""


# ABC 068 C - Cat Snuke and a Voyage
import bisect
#import numpy as np

def getInt(): return int(input())

def getIntList(): return [int(x) for x in input().split()]
# def getIntList(): return np.array(input().split(), dtype=np.longlong)

def zeros(n): return [0]*n
# def zeros(n): return np.zeros(n, dtype=np.longlong)

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
    N, M = getIntList()
    d.dmp((N, M), 'N, M')
    ship = set()
    for i in range(M):
        a, b = getIntList()
        ship.add((a, b))
    d.dmp((ship), 'ship')
    for i in range(2, N):
        if ((1, i) in ship or (i, 1) in ship) and\
             ((i, N) in ship or (N, 1) in ship):
            return 'POSSIBLE'
    return 'IMPOSSIBLE'


ans = prob()
if ans is None:
    pass
elif type(ans) == tuple and ans[0] == 1:  # 1,ans
    for elm in ans[1]:
        print(elm)
else:
    print(ans)
