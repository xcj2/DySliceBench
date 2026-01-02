#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/22
Solved on 2019/3/
@author: shinjisu
"""


# ABC 077 C Festival
import collections
#import numpy as np

def getInt(): return int(input())

def getIntList(): return [int(x) for x in input().split()]
# def getIntList(): return np.array(input().split(), dtype=np.longlong)

def zeros(n): return [0]*n
# def zeros(n): return np.zeros(n, dtype=np.longlong)

def getIntLines(n): return [int(input()) for i in range(n)]
"""
def getIntLines(n):
    data = zeros(n)
    for i in range(n):
        data[i] = getInt()
    return data
"""

def zeros2(n, m): return [zeros(m) for i in range(n)] # obsoleted zeros((n, m))で代替

def getIntMat(n, m):  # n行に渡って、1行にm個の整数
    #mat = zeros((n, m))
    mat = zeros2(n, m)
    for i in range(n):
        mat[i] = getIntList()
    return mat

ALPHABET = [chr(i+ord('a')) for i in range(26)]
DIGIT = [chr(i+ord('0')) for i in range(10)]
N1097 = 10**9 + 7
INF = 10**18

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
    aParts = getIntList()
    bParts = getIntList()
    cParts = getIntList()
    aParts.sort()
    bParts.sort()
    cParts .sort()
    d.dmp((aParts), 'A')
    d.dmp((bParts), 'B')
    d.dmp((cParts), 'C')
    combAB = zeros(N)  # Aのi番めのパーツが組み合わせられる数
    combBC = zeros(N)
    j = 0
    for i in range(N):
        while j < N and bParts[j] <= aParts[i]:
            j += 1
            #d.dmp((i,j),'in while')
        combAB[i] = N-j
        #d.dmp((i,j),'in for')
    d.dmp((combAB), 'combAB')
    j = 0
    for i in range(N):
        while j < N and cParts[j] <= bParts[i]:
            j += 1
        combBC[i] = N-j
    d.dmp((combBC), 'combBC')
    sm = zeros(N+1)
    for i in range(N):
        sm[-2-i] = combBC[-1-i]+sm[-1-i]
    d.dmp((sm), 'sm')
    count = 0
    for i in range(N):
#        count += sum(combBC[N-combAB[i]:])
        count += sm[N-combAB[i]]
    return count


ans = prob()
if ans is None:
    pass
elif type(ans) == tuple and ans[0] == 1:  # 1,ans
    for elm in ans[1]:
        print(elm)
else:
    print(ans)
