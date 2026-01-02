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
    N,M=LI()
    A=[]
    for i in range(M):
        A.append(I())

    tmp1=0
    tmp2=0
    tmp3=0
    out=1
    for n in range(N+1):
        # print(n)
        # print(n,A,tmp3)
        if A:
            if n==1 and A[0]==n:
                tmp1=0
                tmp2=0
                tmp3=0
                del A[0]
                if A:
                    if A[0]==n+1:
                        print("0")
                        exit()
                continue
            elif n!=0 and A[0]==n:
                out*=tmp3
                tmp1=0
                tmp2=0
                tmp3=0
                del A[0]
                if A:
                    if A[0]==n+1:
                        print("0")
                        exit()
                continue
        if tmp3==0:
            tmp3=1
        else:
            tmp1=tmp2
            tmp2=tmp3
            tmp3=tmp1+tmp2
        # print("outttt",A,n,tmp3)
    if tmp3>0:
        out*=tmp3
    print(out%1000000007)
if __name__ == "__main__":
    main()
