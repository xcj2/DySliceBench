#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/21
Solved on 2019/3/
@author: shinjisu
"""


# ABC 082 C Good Sequence
#import math
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
    A = getIntList()
    d.dmp((A), 'A')
    A.sort()
    d.dmp((A), 'A')
    i = 0
    dlt = 0
    while i < N:
        k = 1
        while i+k < N and A[i] == A[i+k]:
            k += 1
            if i+k == N:
                break
        if A[i] < k:
            dlt += k - A[i]
        elif A[i] > k:
            dlt += k
        i += k   
        d.dmp((dlt), 'dlt')
    return dlt


ans = prob()
if ans is None:
    pass
elif type(ans) == tuple and ans[0] == 1:  # 1,ans
    for elm in ans[1]:
        print(elm)
else:
    print(ans)
