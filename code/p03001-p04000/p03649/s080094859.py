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
a=list(map(int,input().split()))

ok,ng=(10**16+1000)*n,-1
while ok-ng>1:
    mid=(ok+ng)//2
    cnt=0
    for i in range(n):
        cnt+=celi(a[i]+mid-n+1,n+1)
    if cnt<=mid:
        ok=mid
    else:
        ng=mid
    # print(ok,ng)
# print(ok)
# print(sum(a)-(n-1)*n)
tmp=sum(a)-(n-1)*n
for i in range(max(0,tmp),ok+1):
    cnt=0
    for j in range(n):
        cnt+=celi(a[j]+i-n+1,n+1)
    if cnt<=i:
        print(i)
        break