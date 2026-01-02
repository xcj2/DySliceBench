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


n,m = LI()
def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def same(x,y):
    return root(x) == root(y)

def union(x,y):
    x = root(x)
    y = root(y)

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

par = [i for i in range(n)]
rank = [0 for _ in range(n)]

xyz = [LI() for _ in range(m)]
for x,y,z in xyz:
    if root(x-1) != root(y-1):
        union(x-1,y-1)
f = defaultdict(lambda :0)
ans = 0
for i in range(n):
    if f[root(i)] == 0:
        ans += 1
        f[root(i)] = 1

print(ans)


