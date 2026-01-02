#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
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

n,x,y = LI()
ans = [0]*n
edge = [[] for _ in range(n)]
for i in range(n-1):
    edge[i].append([i+1,1])
    edge[i+1].append([i,1])

edge[x-1].append([y-1,1])
edge[y-1].append([x-1,1])
for i in range(n):
    d = dijkstra(i, edge)
    for j in range(i+1,n):
        ans[d[j]] += 1
for k in range(1,n):
    print(ans[k])