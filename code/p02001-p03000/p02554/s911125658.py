import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
if n<1:
    print(0)
    exit()

zero=pow(10,n,mod)-pow(9,n,mod)
nine=pow(10,n,mod)-pow(9,n,mod)
ans=zero+nine-(pow(10,n,mod)-pow(8,n,mod))
print(ans%mod)