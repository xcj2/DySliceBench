#!/usr/bin/env python3
#ABC87 D
#重み付きUnion-Find

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

def root(x):
    if x == par[x]:
        return par[x]
    y = root(par[x])
    wei[x] += wei[par[x]]
    par[x] = y
    return y

def union(x,y,w):
    rx = root(x)
    ry = root(y)
    if rank[rx] < rank[ry]:
        par[rx] = ry
        wei[rx] = w - wei[x] + wei[y]
    else:
        par[ry] = rx
        wei[ry] = -w - wei[y] + wei[x]
        if rank[rx] == rank[ry]:
            rank[rx] += 1


n,m = LI()
par = [i for i in range(n)]
rank = [0]*n
wei = [0]*n
for i in range(m):
    l,r,w = LI()
    if root(l-1) != root(r-1):
        union(l-1,r-1,w)
    else:
        if wei[l-1] - wei[r-1] != w:
            print('No')
            quit()
print('Yes')
