#!/usr/bin/env python3
#ABC144 E

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
from itertools import product
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

def f_x(x):
    s = 0
    for A,F in zip(a,f):
        s += max(0,A - x//F)
    if s <= k:
        return True
    return False


n,k = LI()
a = LI()
f = LI()
a.sort()
f.sort(reverse = True)
ok = 0
for A,F in zip(a,f):
    ok = max(ok,A*F)
ng = -1
while ok - ng > 1:
    mid = (ok + ng)//2
    if f_x(mid):
        ok = mid
    else:
        ng = mid
print(ok)