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

def comb(a, b):
    return fact[a] * pow(fact[a-b], mod-2, mod) * pow(fact[b], mod-2, mod) % mod
n, m = LI()
fact = [1] * (max(n, m) + 1)
for i in range(1, max(n, m)+1):
    fact[i] = i * fact[i-1]
    fact[i] %= mod

ret = 0
for x in range(n+1):
    if x % 2:
        ret -= comb(n, x) * fact[m-x] * pow(fact[m-x-(n-x)], mod-2, mod)
        ret %= mod
    else:
        ret += comb(n, x) * fact[m-x] * pow(fact[m-x-(n-x)], mod-2, mod)
        ret %= mod

ans = fact[m] * pow(fact[m-n], mod-2, mod) * ret
ans %= mod
print(ans)