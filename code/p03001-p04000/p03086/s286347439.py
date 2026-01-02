#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/24
@author: shinjisu
"""


# ABC 122
# import math
def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
# def getIntList(): return np.array(input().split(), dtype=np.longlong)
def getIntLines(n): return [int(input()) for i in range(n)]
def getIntMat(n, m):  # n行に渡って、1行にm個の整数
    #mat = zeros((n, m))
    mat = zeros2(n, m)
    for i in range(n):
        mat[i] = getIntList()
    return mat

def zeros(n): return [0]*n
# def zeros(n): return np.zeros(n, dtype=np.longlong)
def zeros2(n, m): return [zeros(m) for i in range(n)] # obsoleted zeros((n, m))で代替

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
    T = input()
    d.dmp((T), 'T')
    AGCT = ('A', 'T', 'C', 'G', )
    mx = 0
    for i in range(len(T)):
        for j in range(i, len(T)):
            count = 0
            for k in range(i, j+1):
                if T[k] in AGCT:
                    count += 1
                else:
                    break
            mx = max(mx, count)
            #d.dmp((mx, count),'mx, count')
    return mx

ans = prob()
if ans is None:
    pass
elif type(ans) == tuple and ans[0] == 1:  # 1,ans
    for elm in ans[1]:
        print(elm)
else:
    print(ans)
    



