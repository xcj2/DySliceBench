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

def bit_add(i,w):
    x = i+1
    while x <= n:
        bit[x-1] += w
        x += x & -x
    return

def bit_sum(i):
    res = 0
    x = i+1
    while x > 0:
        res += bit[x-1]
        x -= x & -x
    return res

n,d,a = LI()
bit = [0]*(n+1)
xh = [LI() for _ in range(n)]
xh.sort()
X = [x for x,_ in xh]
lst = []
for x,h in xh:
    r = br(X,x+2*d)
    lst.append((x,h,r))

ans = 0
for i in range(n):
    x,h,r = lst[i]
    tmp = max(0,math.ceil((h - bit_sum(i))/a))
    ans += tmp
    bit_add(r,-tmp*a)
    bit_add(i,tmp*a)
print(ans)
