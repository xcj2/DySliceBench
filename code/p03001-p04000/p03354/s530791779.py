#!/usr/bin/env python3
#ABC97 D

import sys
import math
import bisect
import time
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

def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def union(x,y):
    x = root(x)
    y = root(y)

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
n,m = LI()
p = LI()
par = [i for i in range(n)]
rank = [0 for _ in range(n)]
for _ in range(m):
    x,y = LI()
    if root(x-1) != root(y-1):
        union(x-1,y-1)

ans = 0
for i in range(n):
    if root(p[i]-1) == root(i):
        ans += 1
print(ans)
