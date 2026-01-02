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

n,x,m=map(int,input().split())


cnt=1
now=x
ans=x
jisyo=defaultdict(list)
jisyo[now]=[ans,cnt]
while cnt<n:
    nex=now**2%m
    cnt+=1
    ans+=nex
    now=nex
    if nex in jisyo:
        tmp=jisyo[nex]
        # print(tmp)
        ans+=(ans-tmp[0])*((n-cnt)//(cnt-tmp[1]))
        cnt=n-(n-cnt)%(cnt-tmp[1])
        break
    else:
        jisyo[now]=[ans,cnt]
    # print(ans,cnt,now)
for i in range(n-cnt):
    now=now**2%m
    ans+=now
print(ans)