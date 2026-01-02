#!/usr/bin/env python3
#AGC39 B

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
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

def dfs(v,color):
    colors[v] = color
    for to in es[v]:
        if colors[to] == color:
            return False
        if colors[to] == 0 and not dfs(to, -color):
            return False
    return True

def is_bipartite():
    return dfs(0,1)

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

n = I()
S = [input() for _ in range(n)]
dist = [[inf]*n for _ in range(n)]
colors = [0]*n
es = [[] for _ in range(n)]
for i in range(n):
    s = S[i]
    for j in range(i+1,n):
        if s[j] == '1':
            dist[i][j] = 1
            dist[j][i] = 1
            es[i].append(j)
            es[j].append(i)

for i in range(n):
    dist[i][i] = 0
d = warshall_floyd(dist)
flg = is_bipartite()
if not flg:
    print(-1)
    quit()
ans = 0
for i in range(n):
    ans = max(ans,max(d[i]))
print(ans+1)

