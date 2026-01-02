import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(1000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
a=list(map(int,input().split()))
uv=[list(map(int,input().split())) for i in range(n-1)]
edge=defaultdict(list)
for i in range(n-1):
    u,v=uv[i]
    edge[u].append(v)
    edge[v].append(u)
# print(edge)

itta=[0]*(n+1)
# lislist=[0]*(n+1)

def dfs(now,lis):
    stk=0
    if a[now-1]>lis[-1]:
        lis.append(a[now-1])
        stk="pop"
    else:
        tmp=bisect.bisect_left(lis, a[now-1])
        stk=[tmp,lis[tmp]]
        lis[tmp]=a[now-1]
    
    # print(now,lis)
    itta[now]=len(lis)
    for i in edge[now]:
        if itta[i]==0:
            dfs(i,lis)
    
    if stk=="pop":
        lis.pop()
    else:
        lis[stk[0]]=stk[1]

dfs(1,[float('inf')])

# print(itta)
for i in range(n):
    print(itta[i+1])