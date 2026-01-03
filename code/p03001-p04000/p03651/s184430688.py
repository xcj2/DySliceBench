#!/usr/bin/env python3
#AGC18 A

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


def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m,n%m)

n,k = LI()
a = LI()
if k in a:
    print('POSSIBLE')
    quit()
if max(a) < k:
    print('IMPOSSIBLE')
    quit()
g = a[0]
for i in range(1,n):
    g = gcd(g,a[i])
if k % g != 0:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
