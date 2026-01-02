import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m,s=map(int,input().split())
uvab=[list(map(int,input().split())) for i in range(m)]
cd=[list(map(int,input().split())) for i in range(n)]

def dijkstra(s,n):
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost


e = [[] for _ in range(10000*(n+1))]
for i in range(n):
    c,d=cd[i]
    for j in range(2500):
        e[10000*i+j].append((d,10000*i+min(j+c,2500)))
    
for i in range(m):
    u,v,a,b=uvab[i]
    u,v = u-1, v-1
    for j in range(2500):
        if j-a>=0:
            e[10000*v+j].append((b,10000*u+j-a))
            e[10000*u+j].append((b,10000*v+j-a))
# print(e)
s=min(2499,s)
# print(s)
lst=dijkstra(s,10000*(n+1))
# print(lst)
for i in range(1,n):
    ans=float('inf')
    for j in range(2500):
        ans=min(ans,lst[10000*i+j])
    print(ans)