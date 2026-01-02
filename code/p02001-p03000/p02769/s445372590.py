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
    return fact[n] * pow(fact[n-r],mod-2,mod) * pow(fact[r],mod-2,mod) % mod


n,k = LI()

fact = [1]*(n+1)
for i in range(1,n+1):
    fact[i] = i*fact[i-1]
    fact[i] %= mod

ans = 0

for i in range(min(n,k+1)):
    ans += C(n,i) * C(n-1,n-i-1)
    ans %= mod
print(ans)