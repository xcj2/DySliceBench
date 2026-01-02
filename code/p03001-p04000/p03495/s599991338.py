#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/16
Solved on 2019/3/
@author: shinjisu
"""


# ABC 081 C Not so Diverse
#import math
#import numpy as np

def getInt(): return int(input())

def getIntList(): return [int(x) for x in input().split()]
# def getIntList(): return np.array(input().split(), dtype=np.longlong)

def zeros(n): return [0]*n
# def zeros(n): return np.zeros(n, dtype=np.longlong)

def getIntLines(n): return [int(input()) for i in range(n)]

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
    N, K = getIntList()
    d.dmp((N, K), 'N, K')
    A = getIntList()
    d.dmp((A), 'A')
    dic = {}
    for e in A:
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1
    d.dmp(dic,'dic')
    val = list(dic.values())
    count = 0
    val.sort()
    d.dmp(val,'val')
    for i in range(len(val)-K):
        count += val[i]
    return count


ans = prob()
if ans is None:
    pass
elif type(ans) == tuple and ans[0] == 1:  # 1,ans
    for elm in ans[1]:
        print(elm)
else:
    print(ans)
