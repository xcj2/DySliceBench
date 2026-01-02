import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush,heapify
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

def comb(n, r, mod=10**9+7):
    n1, r = n+1, min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod
x,y = MAP()

if (x+y)%3!=0:
    print(0)
    exit()

n = (2*y - x)//3
m = (2*x -y)//3
if n<0 or m<0:
    print(0)
    exit()
print(comb(n+m,min(n,m),MOD))