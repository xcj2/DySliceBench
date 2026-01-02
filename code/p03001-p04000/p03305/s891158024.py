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


n,m,s,t=map(int,input().split())
uvab=[list(map(int,input().split())) for i in range(m)]

def dijkstra(s,e):
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

e1 = [[] for _ in range(n)]
e2 = [[] for _ in range(n)]
for i in range(m):
    a,b,en,su = uvab[i]
    a,b = a-1, b-1
    e1[a].append((en, b))
    e1[b].append((en, a))
    e2[a].append((su, b))
    e2[b].append((su, a))

c1=dijkstra(s-1,e1)
c2=dijkstra(t-1,e2)
# print(c1)
# print(c2)
hlst=[]
for i in range(n):
    hlst.append((c1[i]+c2[i],i))
# print(hlst)
heapq.heapify(hlst)
# print(hlst)
for i in range(n):
    while hlst[0][1]<i:
        heapq.heappop(hlst)
    print(10**15-hlst[0][0])