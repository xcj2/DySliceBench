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

def calc(lst):
    ret = 0
    for a, b, c, d in abcd:
        if lst[b-1] - lst[a-1] == c:
            ret += d
    return ret

def dfs(lst):
    if len(lst) == n:
        return calc(lst)
    
    x = lst[-1]
    ret = 0
    for i in range(x, m+1):
        ret = max(ret, dfs(lst + [i]))
    return ret

n, m, q = LI()
abcd = [LI() for _ in range(q)]
ans = dfs([1])
print(ans)