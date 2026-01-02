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

def C(n,r):
    return f[n]*pow(f[n-r],mod-2,mod)*pow(f[r],mod-2,mod) % mod

n,k = LI()
a = LI()
a.sort()
f = [1]*(n+1)
for i in range(1,n+1):
    f[i] = i*f[i-1]
    f[i] %= mod

ans = 0
for i in range(n):
    if k-1 <= i <= n-k:
        ans += C(i,k-1)*a[i]
        ans %= mod
        ans -= C(n-(i+1),k-1)*a[i]
        ans %= mod
    elif i < k-1 and i+k-1 < n:
        ans -= C(n-(i+1),k-1)*a[i]
        ans %= mod
    elif i > n-k and i-(k-1) >= 0:
        ans += C(i,k-1)*a[i]
        ans %= mod
print(ans)
