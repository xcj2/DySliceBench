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
# S=numpp.assaray(S)=="#"
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LLS(): return [list(sys.stdin.readline().rstrip()) for _ in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()



def main():
    A,B=LI()
    out=1
    num=A
    if B<=1:
        print("0")
        exit()
    while num<B:
        num+=(A-1)
        out+=1
    print(out)


if __name__ == "__main__":
    main()