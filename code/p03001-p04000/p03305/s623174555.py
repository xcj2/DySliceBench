#!/usr/bin/env python3
#SoundHound D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n,m,s,t = LI()
graph1 = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]
for _ in range(m):
    u,v,a,b = LI()
    graph1[u-1].append((v-1,a))
    graph1[v-1].append((u-1,a))
    graph2[u-1].append((v-1,b))
    graph2[v-1].append((u-1,b))

def dijkstra(s,graph):
    d = [inf]*n
    d[s] = 0
    h = [(0,s)]
    while h:
        c,v = heappop(h)
        if d[v] < c:
            continue
        for t,cost in graph[v]:
            if d[v] + cost < d[t]:
                d[t] = d[v] + cost
                heappush(h,(d[t],t))
    return d

c1 = dijkstra(s-1,graph1)
c2 = dijkstra(t-1,graph2)
c = [c1[i] + c2[i] for i in range(n)]
money = 10**15
mi = c[-1]
for i in range(n-1)[::-1]:
    mi = min(mi,c[i])
    c[i] = mi
for i in range(n):
    print(money - c[i])
