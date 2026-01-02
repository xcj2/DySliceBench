#!/usr/bin/env python3
#CADDi C

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

def trial_division(n):
    factor = []
    tmp = int(math.sqrt(n)) + 1
    for i in range(2,tmp):
        while n % i == 0:
            n //= i
            factor.append(i)
    if n != 1:
        factor.append(n)
    factor.sort()
    return factor
n,p = LI()
P = trial_division(p)
P = list(Counter(P).items())
ans = 1
for i,j in P:
    ans *= i**(math.floor(j/n))
print(ans)
