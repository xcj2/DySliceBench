#!/usr/bin/env python3
#ABC125 C

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

n = I()
a = LI()
l,r = [0]*n,[0]*n
l[0] = a[0]
r[-1] = a[-1]
for i in range(1,n):
    l[i] = gcd(l[i-1],a[i])
for i in range(n-1)[::-1]:
    r[i] = gcd(r[i+1],a[i])
ans = 0
l = [0] + l + [0]
r = [0] + r + [0]
for i in range(1,n+1):
    ans = max(ans,gcd(l[i-1],r[i+1]))
print(ans)
