#!/usr/bin/env python3
#ABC143 E

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

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
  
n,m,l = LI()
graph = [[] for _ in range(n)]
d = [[inf]*n for _ in range(n)]
for _ in range(m):
    a,b,c = LI()
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))
    d[a-1][b-1] = c
    d[b-1][a-1] = c

for i in range(n):
    d[i][i] = 0

d = warshall_floyd(d)

d2 = [[inf]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][j] <= l:
            d2[i][j] = 1

d2 = warshall_floyd(d2) 
q = I()
for _ in range(q):
    s,t = LI()
    if d2[s-1][t-1] == inf:
        print(-1)
    else:
        print(d2[s-1][t-1]-1)
