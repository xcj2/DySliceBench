# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:50:41 2019

@author: shinjisu
"""

#import numpy as np
#import math
def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]

def zeros(n): return [0]*n
def zeros2(n, m): return [zeros(m)]*n # obsoleted zeros((n, m))で代替

def getIntLines(n): return [int(input()) for i in range(n)]

def getIntMat(n, m):  # n行に渡って、1行にm個の整数
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


def digitSum(n):
    ds = 0
    while n > 0:
        ds += n % 10
        n //= 10
    return ds


def prob():
    d = Debug()
    d.off()
    N = getInt()
    minSum = INF
    for i in range(1, N//2+1):
        minSum = min(minSum, digitSum(i)+digitSum(N-i))
#        d.dmp(minSum)
    return minSum


ans = prob()
if ans is None:
    pass
else:
    print(ans)
#elif ans[0] == 'col':
#    for elm in ans[1]:
#        print(elm)
