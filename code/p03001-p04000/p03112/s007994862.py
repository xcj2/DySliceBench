import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush,heapify
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7
INF = 10**18

A,B,Q = MAP()
s = [-INF] + [INT() for _ in range(A)] + [INF]
t = [-INF] + [INT() for _ in range(B)] + [INF]

for i in range(Q):
    cur = INT()
    s_idx = bisect.bisect_right(s,cur)
    t_idx = bisect.bisect_right(t,cur)
    res = INF
    for S in [s[s_idx-1],s[s_idx]]:
        for T in [t[t_idx-1],t[t_idx]]:
            d1,d2 = abs(S-cur) + abs(T-S),abs(T-cur)+abs(S-T)
            res = min(res,d1,d2)
    print(res)