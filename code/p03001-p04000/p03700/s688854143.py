#!/usr/bin/env python3
#ABC63 D

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

def f(t):
    lst = list(map(lambda x: max(0, math.ceil((x-b*t)/(a-b))),h))
    if sum(lst) <= t:
        return True
    return False

n,a,b = LI()
h = [I() for _ in range(n)]
maxh = max(h)
ok,ng = math.ceil(maxh/b),0
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)
