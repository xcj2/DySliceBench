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

s=int(input())
dp=[-1]*2010

for i in range(3):
    dp[i]=0
for i in range(3,6):
    dp[i]=1

def solve(n):
    # print(n)
    if dp[n]!=-1:
        return dp[n]
    cnt=1
    for i in range(3,n-2):
        cnt+=solve(i)
        cnt%=mod
    # print(n,cnt)
    dp[n]=cnt%mod
    return dp[n]

print(solve(s))
# print(dp[:10])