#!/usr/bin/env python3
#EDPC G

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

def dfs(s):
    if dp[s] != -1:
        return dp[s]
    elif len(edge[s]) == 0:
        return 0
    else:
        res = 0
        for v in edge[s]: 
            res = max(res,dfs(v)+1)
        dp[s] = res
        return res
n,m = LI()
dp = [-1]*n
edge = [[] for _ in range(n)]
for _ in range(m):
    x,y = LI()
    x -= 1
    y -= 1
    edge[x].append(y)

for i in range(n):
    dfs(i)
print(max(dp))