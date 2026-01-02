#!/usr/bin/env python3
#AGC20 B

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
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
    for i in a:
        if x < i:
            x = 0
            break
        x = x - (x % i)
    return x
k = I()
a = LI()
high,low = 10**20,0
while (high - low) > 1:
    mid = (high + low) // 2 
    if f(mid) >= 2:
        high = mid
    else:
        low = mid
ans1 = high
high,low = 10**20,0
while (high - low) > 1:
    mid = (high + low) // 2
    if f(mid) > 2:
        high = mid
    else:
        low = mid
ans2 = low
if ans1 > ans2:
    print(-1)
else:
    if f(ans1) != 2 or f(ans2) != 2:
        print(-1)
    else:
        print(ans1,ans2)
