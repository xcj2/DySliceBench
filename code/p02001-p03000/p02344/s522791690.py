#!/usr/bin/env python3

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

def root(x):
    if par[x] == x:
        return x
    else:
        r = root(par[x])
        weight[x] += weight[par[x]]
        par[x] = r
        return r

def union(x,y,w):
    rx = root(x)
    ry = root(y)
    if rank[rx] < rank[ry]:
        par[rx] = ry
        weight[rx] = w - weight[x] + weight[y]
    else:
        par[ry] = rx
        weight[ry] = - w - weight[y] + weight[x]
        if rank[rx] == rank[ry]:
            rank[rx] += 1
def same(x,y):
    return root(x) == root(y)

def diff(x,y):
    return weight[x] - weight[y]

n,q = LI()
par = [i for i in range(n)]
weight = [0]*n
rank = [0]*n
for _ in range(q):
    lst = LI()
    if lst[0] == 0:
        x,y,z = lst[1:4]
        if not same(x,y):
            union(x,y,z)
    else:
        x,y = lst[1:3]
        if not same(x,y):
            print('?')
        else:
            print(diff(x,y))

