#!/usr/bin/env python3
#E

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

def comb(n, r):
    return fact[n]*pow(fact[n-r], mod-2, mod)*pow(fact[r], mod-2, mod) % mod
n = I()
ab = [LI() for _ in range(n)]

fact = [1]*(n+1)
for i in range(1, n+1):
    fact[i] = i * fact[i-1]
    fact[i] %= mod

x = defaultdict(lambda : 0)
y = defaultdict(lambda : 0)
z = defaultdict(lambda : 0)
tmp = 0
for a, b in ab:
    if a == 0 and b == 0:
        tmp += 1
    elif a == 0:
        x[0] += 1
        z[0] = 1
    elif b == 0:
        y[0] += 1
        z[0] = 1
    else:
        if a * b > 0:
            g = math.gcd(a, b)
            a //= g
            b //= g
            x[(abs(a), abs(b))] += 1
            z[(abs(a), abs(b))] = 1
        else:
            g = math.gcd(a, b)
            a //= g
            b //= g
            y[(abs(b), abs(a))] += 1
            z[(abs(b), abs(a))] = 1

ans = 1
for i in z.keys():
    ans *= (2**x[i] + 2**y[i] - 1)
    ans %= mod
ans -= 1
ans += tmp
ans %= mod
print(ans)




