#!/usr/bin/env python3

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

def C(n,r):
    return fact[n]*pow(fact[n-r],mod-2,mod)*pow(fact[r],mod-2,mod) % mod

x,y = LI()

fact = [1]*(x+y)
for i in range(1,x+y):
    fact[i] = i*fact[i-1]
    fact[i] %= mod

if (x+y) % 3 != 0:
    print(0)
else:
    if 2*y-x < 0 or (2*y-x) % 3 != 0:
        print(0)
    elif 2*x-y < 0 or (2*x-y) % 3 != 0:
        print(0)
    else:
        print(C((x+y)//3,(2*x-y)//3))