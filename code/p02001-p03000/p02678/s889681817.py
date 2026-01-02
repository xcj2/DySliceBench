import sys
from math import factorial
from collections import Counter
from fractions import Fraction
import heapq, bisect, fractions
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
MOD = 10**9 + 7

n, e =MAP()  #頂点数、辺数
G = [[]for i in range(n)]
for i in range(e):
    fr, to = MAP()#辺の端点、重み
    G[fr-1].append([1,to -1])
    G[to-1].append([1,fr -1])

def djkstra(s,G):
    visited = [False]*n#すでに計算したかどうか 
    d = [INF]*n#最短距離
    former = [INF]*n#経路の一つ前の頂点を記憶
    que = []
    heapq.heappush(que, (0,s,-1))
    while(len(que)>0):
        vs = heapq.heappop(que)
        distance = vs[0]
        vertex = vs[1]
        f = vs[2]
        if visited[vertex]:
            continue
        d[vertex] = distance
        visited[vertex] = True
        former[vertex] = f
        for Gs in G[vertex]:
            if d[Gs[1]] <= distance+Gs[0]:
                continue
            heapq.heappush(que,(distance+Gs[0], Gs[1], vertex))

    return d,former

d, former = djkstra(0,G)
print('Yes')
for i in range(n-1):
    print(former[i+1]+1)
