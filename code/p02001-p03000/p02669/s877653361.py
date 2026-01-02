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


t = I()
for _ in range(t):
    n, a, b, c, d = LI()
    memo = {0: 0, 1: d}
    def dfs(x):
        if x in memo:
            return memo[x]
        ret = x * d
        ret = min(ret, min(dfs(x // 2), dfs((x - 1) // 2 + 1)) + a + d * (x % 2))
        if (x % 3) < (-x % 3):
            ret = min(ret, b + dfs(x // 3) + d * (x % 3))
        else:
            ret = min(ret, b + dfs((x - 1) // 3 + 1) + d * (-x % 3))
        if (x % 5) < (-x % 5):
            ret = min(ret, c + dfs(x // 5) + d * (x % 5))
        else:
            ret = min(ret, c + dfs((x - 1) // 5 + 1) + d * (-x % 5))

        memo[x] = ret
        return ret

    print(dfs(n))
    