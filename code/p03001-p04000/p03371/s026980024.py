#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/16
Solved on 2019/3/
@author: shinjisu
"""


# ABC 095 C Half and Half
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

def zeros2(n, m): return [zeros(m)]*n # obsoleted zeros((n, m))で代替

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
    A, B, C, X, Y = getIntList()
    d.dmp((A, B, C, X, Y),'A, B, C, X, Y')
    pt1 = A*X + B*Y
    pt2 = A*X + C*2*Y
    pt3 = C*2*X + B*Y
    pt4 = C*2*min(X, Y)+ C*2*(max(X, Y)-min(X, Y))
    if X > Y:
        pt5 = C*2*min(X, Y)+ A*(X-min(X, Y))
    else:
        pt5 = C*2*min(X, Y)+ B*(Y-min(X, Y))

    yen = min(pt1, pt2, pt3, pt4, pt5)
    d.dmp((pt1, pt2, pt3, pt4, pt5), 'pt1, pt2, pt3, pt4, p5')
    d.dmp(yen, 'yen')
    return yen


ans = prob()
if ans is None:
    pass
elif type(ans) == tuple and ans[0] == 1:  # 1,ans
    for elm in ans[1]:
        print(elm)
else:
    print(ans)
