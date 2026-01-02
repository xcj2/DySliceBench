#!/usr/bin/env python3
#D

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
ab = [LI() for _ in range(m)]
ans = 0
for i in range(m):
    par = [i for i in range(n)]
    rank = [0] * n
    for j in range(m):
        if i == j:
            continue
        a, b = ab[j]
        if root(a-1) != root(b-1):
            union(a-1, b-1)
    cnt = len(set([root(i) for i in range(n)]))
    if cnt > 1:
        ans += 1
print(ans)