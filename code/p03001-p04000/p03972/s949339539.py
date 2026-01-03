#!/usr/bin/env python3
#CODE FESTIVAL 2016 qual B C
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
w,h = LI()
p = [I() for _ in range(w)]
q = [I() for _ in range(h)]
hq = []
for i in p:
    heappush(hq,(i,0))
for i in q:
    heappush(hq,(i,1))
ans = 0
w += 1
h += 1
while hq:
    v,flg = heappop(hq)
    if flg:
        ans += v*w
        h -= 1
    else:
        ans += v*h
        w -= 1
print(ans)