#!/usr/bin/env python3
#ABC138 D

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

n,q = LI()
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = LI()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
cnt = [0]*n
for _ in range(q):
    p,x = LI()
    cnt[p-1] += x
#オイラーツアー
def dfs(x,p):
    for i in graph[x]:
        if i != p:
            cnt[i] += cnt[x]
            dfs(i,x)
dfs(0,-1)
print(*cnt)
