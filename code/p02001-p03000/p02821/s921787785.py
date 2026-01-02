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
    cnt = 0
    for i in a:
        idx = bl(a,x-i)
        cnt += n - idx
        if cnt >= m:
            return True
    return False

n,m = LI()
a = LI()
a.sort()
ok,ng = 2*max(a)+1,2
while ok - ng > 1:
    mid = (ok+ng) // 2
    if f(mid):
        ng = mid
    else:
        ok = mid

ans = 0
tmp = 0
b = [0] + list(accumulate(a))
for i in a:
    idx = bl(a,ng-i)
    ans += i*(n - idx) + (b[-1] - b[idx])
    tmp += n - idx
ans = ans - (tmp - m)*ng
print(ans)