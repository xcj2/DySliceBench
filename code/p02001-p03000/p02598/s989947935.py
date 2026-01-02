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

def f(x):
    cnt = k
    for i in a:
        tmp = math.ceil(i / x)
        cnt -= tmp - 1
        if cnt < 0:
            return False
    return True

n, k = LI()
a = LI()
a.sort(reverse=True)
ok = sum(a)
ng = 0
while ok - ng > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)