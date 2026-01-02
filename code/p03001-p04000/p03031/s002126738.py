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


n,m=map(int,input().split())
ks=[list(map(int,input().split())) for i in range(m)]
p=list(map(int,input().split()))

bit=list(product(range(2),repeat=n))
ans=0
for bi in bit:
    plst=[0]*m
    for j in range(m):
        for k in range(ks[j][0]):
            plst[j]+=bi[ks[j][1+k]-1]
    
    for j in range(m):
        if plst[j]%2!=p[j]:
            break
    else:
        ans+=1
print(ans)