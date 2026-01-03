#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/24
Solved on 2019/3/
@author: shinjisu
"""


# ABC 056 C - Go Home
def getInt(): return int(input())
def zeros(n): return [0]*n
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
    X = getInt()
    d.dmp((X), 'X')
    sm = 0
    for i in range(1, 10**9+1):
        sm += i
        if X <= sm:
            break
    return i


ans = prob()
if ans is None:
    pass
elif type(ans) == tuple and ans[0] == 1:  # 1,ans
    for elm in ans[1]:
        print(elm)
else:
    print(ans)
