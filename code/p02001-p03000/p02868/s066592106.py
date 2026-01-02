#!/usr/bin/env python3
#第二回全国統一プログラミング王決定戦予選 D

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000)
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

n,m = LI()
lrc = [LI() for _ in range(m)]
edge = [[] for _ in range(n)]
for l,r,c in lrc:
    edge[l-1].append((r-1,c))
for i in range(n-1):
    edge[i+1].append((i,0))
d = dijkstra(0,edge)
if d[-1] == inf:
    print(-1)
else:
    print(d[-1])