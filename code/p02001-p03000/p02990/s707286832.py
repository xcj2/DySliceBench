# -*- coding: utf-8 -*-
"""
AtCoder A
"""

import sys, math, random
import numpy as np

# N = int(input())
# A = list(map(int,input().split())) # N row 1 column
# A = [int(input()) for _ in range(N)] # 1 row N column
# S = str(input()) # str(input()) == input() -> 'abc'
# S = list(input()) # abc -> ['a','b','c']
# S.replace('ABC','X') # "testABCABC" -> "testXX"
 
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
 
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def P(n, r):
    return math.factorial(n)//math.factorial(n-r)

def C(n, r):
    return P(n, r)//math.factorial(r)


def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def main():
    N, K = list(map(int,input().split()))
    for k in range(K):
        # print(N-K+1,k+1,K-1,k)
        if (N-K+1<k+1):
            print("0")
            continue
        tmp= cmb(N-K+1,k+1)
        tmp2=cmb(K-1,k)
        print(tmp*tmp2%mod)
    
if __name__ == "__main__":
    main()