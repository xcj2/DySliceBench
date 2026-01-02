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


def main():
    N=I()
    A = list(map(int,input().split()))
    B=LI()
    bef=0
    out=0
    for i in range(N):
        if A[i]>bef:
            en=A[i]-bef
            out+=bef
            if en>B[i]:
                bef=0
                out+=B[i]
            else:
                bef=B[i]-en
                out+=en
        else:
            out+=A[i]
            bef=B[i]
    i=N
    if A[N]>bef:
        en=A[N]-bef
        out+=bef
    else:
        out+=A[N]
        # bef=B[N]

    print(out)

if __name__ == "__main__":
    main()