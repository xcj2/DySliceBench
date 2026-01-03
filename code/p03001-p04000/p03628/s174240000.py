#!/usr/bin/env python3
#ARC81 D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n = I()
s1 = input()
s2 = input()
ans = 0
flg = 0
fact = [1]*53
for i in range(1,53):
    fact[i] = fact[i-1]*i

def comb(n,r):
    return fact[n] // fact[n-r] // fact[r]

if s1[0] == s2[0]:
    ans += 3
    flg = 0
    i = 1
else:
    ans += comb(3,2)*2
    ans %= mod
    flg = 1
    i = 2
while i < n:
    if flg == 0 and s1[i] == s2[i]:
         ans *= 2
         ans %= mod
         i += 1
    elif flg == 1 and s1[i] == s2[i]:
        ans *= 1
        flg = 0
        i += 1
    elif flg == 0 and s1[i] != s2[i]:
        ans *= 2
        ans %= mod
        flg = 1
        i += 2
    elif flg == 1 and s1[i] != s2[i]:
        ans *= 3
        ans %= mod
        i += 2
print(ans)
