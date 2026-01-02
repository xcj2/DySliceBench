#!/usr/bin/env python3

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

"""
"""

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

n,m,l = LI()

dist = [[inf]*n for _ in range(n)]
dist2 = [[inf]*n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0
    dist2[i][i] = 0
for _ in range(m):
    a,b,c = LI()
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c

dist = warshall_floyd(dist)

for i in range(n):
    for j in range(n):
        if dist[i][j] > l:
            dist2[i][j] = inf
        else:
            dist2[i][j] = 1

dist2 = warshall_floyd(dist2)
q = I()
ans = []
for _ in range(q):
    s,t = LI()
    if dist2[s-1][t-1] == inf:
        print(-1)
    else:
        print(dist2[s-1][t-1]-1)

