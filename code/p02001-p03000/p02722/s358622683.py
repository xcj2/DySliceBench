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
mod = 10**9+7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n = I()
def check(x,m):
    if m % x:
        return m % x == 1
    return check(x,m//x)

def count(n):
    cnt = 1
    f = defaultdict(int)
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0 and f[i] == 0:
            cnt += 1
            f[i] = 1
            if f[n//i] == 0:
                cnt += 1
                f[n//i] = 1
    return cnt

def count2(n):
    cnt = 1
    f = defaultdict(int)
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            if check(i,n) and f[i] == 0:
                cnt += 1
                f[i] = 1
            if check(n//i,n) and f[n//i] == 0:
                cnt += 1
                f[n//i] = 1
    return cnt

if n == 2:
    print(1)
    quit()
ans = count(n-1)
ans += count2(n)
print(ans)
