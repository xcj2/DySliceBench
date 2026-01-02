#!/usr/bin/env python3

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

n = I()
a = LI()
edges = [[] for _ in range(n)]
dp = [10**10]*n
for _ in range(n-1):
    u,v = LI()
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

ans = [None]*n
ans[0] = 1
dp[0] = a[0]
def dfs(k, p, dp):
    flag = False
    for v in edges[k]:
        if v != p:
            l = bl(dp, a[v])
            if dp[l] > a[v]:
                idx = l
                tmp = dp[l]
                dp[l] = a[v]
                flag = True
                if tmp == 10**10:
                    ans[v] = ans[k] + 1
                else:
                    ans[v] = ans[k]
            else:
                ans[v] = ans[k]
            dfs(v, k, dp)
            if flag:
                dp[idx] = tmp
                flag = False
    return 
dfs(0, -1, dp)
for i in ans:
    print(i)


