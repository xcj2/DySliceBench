#!/usr/bin/env python3
#ABC137 C

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

def comb(n,r):
    return math.factorial(n)//math.factorial(n-r)//math.factorial(r)
n = I()
s = [input() for _ in range(n)]
x = [list(Counter(s[i]).items()) for i in range(n)]
for i in x:
    i.sort()

y = [tuple(i) for i in x]
f = defaultdict(lambda : 0)
for i in range(n):
    f[y[i]] += 1
ans = 0
for i in f.values():
    if i < 2:
        continue
    ans += comb(i,2)
print(ans)
