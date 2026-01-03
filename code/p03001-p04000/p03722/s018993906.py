#!/usr/bin/env python3
#ABC61 D

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

def Bellman_Ford(edges,start):
    dist = [-inf for _ in range(n)]
    dist[start] = 0
    for cnt in range(n+1):
        for edge in edges:
            e_from, e_to, e_cost = edge
            if dist[e_to] < dist[e_from] + e_cost:
                dist[e_to] = dist[e_from] + e_cost
        if cnt == n - 1:
            d = dist[:]
    if d[-1] < dist[-1]:
        print('inf')
        quit()
    else:
        return d[-1]

n,m = LI()
edges = []
for _ in range(m):
    a,b,c = LI()
    edges.append([a-1,b-1,c])

ans = Bellman_Ford(edges,0)
print(ans)
