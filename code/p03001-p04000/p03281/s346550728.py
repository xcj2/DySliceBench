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

def f(x):
    res = 0
    for i in range(1,x+1):
        if x % i == 0:
            res += 1
    return res
 
n = I()
ans = 0
for i in range(1,n+1):
    if i % 2:
        if f(i) == 8:
            ans += 1
print(ans)