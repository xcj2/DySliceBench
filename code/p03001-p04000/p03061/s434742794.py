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

def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m,n%m)

n = I()
a = LI()
l = [0]*n
r = [0]*n
l[0] = a[0]
for i in range(1,n):
    l[i] = gcd(l[i-1],a[i])
r[-1] = a[-1]
for i in range(n-1)[::-1]:
    r[i] = gcd(r[i+1],a[i])

ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans,r[i+1])
    elif i == n-1:
        ans = max(ans,l[-2])
    else:
        ans = max(ans,gcd(l[i-1],r[i+1]))
print(ans)

