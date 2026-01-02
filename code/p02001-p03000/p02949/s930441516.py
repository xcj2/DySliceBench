import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
from math import *
from itertools import *
INF = float('inf')

def bellmanford(edges, s, t, se):
    N = len(edges)
    dist = [INF] * N
    dist[s] = 0
    for i in range(N):
        update = False
        for v in range(N):
            if v not in se or dist[v] == INF:
                continue
            for u, c in edges[v]:
                if u not in se:
                    continue
                d = dist[v] + c
                if d < dist[u]:
                    dist[u] = d
                    update = True
        if update == False:
            return max(0, -dist[t])
    else:
        return -1

N, M, P = map(int, input().split())
es = [[] for i in range(N)]
es_r = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    es[a-1].append((b-1, P-c))
    es_r[b-1].append(a-1)
reachable1 = [False] * N
def dfs(v):
    if reachable1[v]: return
    reachable1[v] = True
    for u, c in es[v]:
        dfs(u)
reachable2 = [False] * N
def rdfs(v):
    if reachable2[v]: return
    reachable2[v] = True
    for u in es_r[v]:
        rdfs(u)
dfs(0)
rdfs(N-1)
se = set()
for i in range(N):
    if reachable1[i] and reachable2[i]:
        se.add(i)
print(bellmanford(es, 0, N-1, se))
