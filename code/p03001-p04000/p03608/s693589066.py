#!/usr/bin/env python3
#ABC73 D

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

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

n,m,R = LI()
r = LI()
d = [[inf]*n for _ in range(n)]
for _ in range(m):
    a,b,c = LI()
    d[a-1][b-1] = c
    d[b-1][a-1] = c

d = warshall_floyd(d)
ans = inf
for i in permutations(r,R):
    tmp = 0
    for j in range(R-1):
        tmp += d[i[j]-1][i[j+1]-1]
    ans = min(ans,tmp)
print(ans)
