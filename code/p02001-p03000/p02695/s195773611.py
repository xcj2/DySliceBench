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

def check(num):
    res = 0
    for a,b,c,d in abcd:
        if num[b-1] - num[a-1] == c:
            res += d
    return res

def dfs(x, y, z, res):
    if y == n:
        res = max(res, check(x))
        return res
    for i in range(z, m+1):
        res = max(res, dfs(x + [i], y+1, i, res))
    return res

n, m, q = LI()
abcd = [LI() for _ in range(q)]
ans = dfs([1], 0, 1, 0)
print(ans)
        

    