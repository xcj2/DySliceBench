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

"""
[求めたいもの]
Σ(r1<=i<=r2)Σ(c1<=j<=c2) f(i,j)

g(R,C) := Σ(0<=i<=R)Σ(0<=j<=C)f(i,j) とすると
ans = g(r2,c2) - g(r2,c1-1) - g(r1-1,c2) + g(r1-1,c1-1)

[性質(パスカルの三角形)]
・f(r+1,c) = f(r,c) + f(r,c-1) + ... + f(r,0)
・g(R,C) = Σ(0<=i<=R)f(i+1,C)
       = f(R+1,C+1) - 1

g(r2,c2) = f(r2+1+c2+1,r2+1) - 1
g(r2,c1-1) = f(r2+1+c1,r2+1) - 1
g(r1-1,c2) = f(r1+c2+1,c2+1) - 1
g(r1-1,c1-1) = f(r1+c1,r1) - 1
"""
def nCr(n,r):
    return fact[n]*pow(fact[n-r],mod-2,mod)*pow(fact[r],mod-2,mod) % mod

r1,c1,r2,c2 = LI()

n = r2+c2+2
fact = [1]*(n+1)
for i in range(1,n+1):
    fact[i] = i*fact[i-1]
    fact[i] %= mod

ans = nCr(r2+c2+2,r2+1) -1
ans -= nCr(r2+c1+1,r2+1) - 1
ans -= nCr(r1+c2+1,c2+1) - 1
ans += nCr(r1+c1,c1) - 1
ans %= mod
print(ans)