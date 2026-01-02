#!/usr/bin/env python3
#ABC127 E

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
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

def C(n,r):
    return fact[n]*pow(fact[n-r],mod-2,mod)*pow(fact[r],mod-2,mod) % mod

n,m,k = LI()

fact = [1]*(n*m+1)
for i in range(1,n*m+1):
    fact[i] = i*fact[i-1]
    fact[i] %= mod

ans = 0
"""xの差"""
for d in range(1,m):
    ans += d*(m-d)*n*n
    ans %= mod

"""yの差"""
for d in range(1,n):
    ans += d*(n-d)*m*m
    ans %= mod

ans *= C(n*m-2,k-2)
ans %= mod
print(ans)
