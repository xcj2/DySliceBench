import sys
from collections import Counter, deque, defaultdict
from math import factorial
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n, e, s, t = MAP()
s-= 1
t-= 1    
G1 = [[]for i in range(n)]
G2 = [[]for i in range(n)]       

for i in range(e):
    fr, to, w1, w2 = MAP()
    G1[fr-1].append((w1, to -1))
    G1[to-1].append((w1, fr -1))
    G2[fr-1].append((w2, to -1))
    G2[to-1].append((w2, fr -1))


def djkstra(s,G):
    visited = [False]*n     #その頂点を確定したかどうか
    d = [INF]*n
    que = []
    heapq.heapify(que)
    heapq.heappush(que, (0,s))

    while(len(que)>0):
        vs = heapq.heappop(que)
        distance = vs[0]
        vertex = vs[1]
        if visited[vertex]:
            continue
        d[vertex] = distance
        visited[vertex] = True
        for Gs in G[vertex]:
            if d[Gs[1]] <= distance+Gs[0]:
                continue
            heapq.heappush(que,(distance+Gs[0], Gs[1]))
    
    return d

d_yen = djkstra(s,G1)
d_snuuk = djkstra(t,G2)

d_sum = [0]*n

for i in range(n):
    d_sum[i] = d_yen[i] + d_snuuk[i]

d_sum.reverse()
d_ans = [0]*n
d_ans[0] = d_sum[0]
for i in range(1,n):
    d_ans[i] = min(d_ans[i-1],d_sum[i])

for i in range(n-1,-1,-1):
    print(10**15 - d_ans[i])

