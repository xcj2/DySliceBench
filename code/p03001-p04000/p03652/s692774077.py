#!/usr/bin/env python3
#AGC18 B

import sys
import math
import copy
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

def f(flag):
    global ans
    cnt = [0]*m
    for i in range(n):
        for j in range(m):
            if flag[a[i][j]-1]:
                cnt[a[i][j]-1] += 1
                break
        else:
            return
    flag[cnt.index(max(cnt))] = False
    ans = min(ans,max(cnt))
    f(flag)
n,m = LI()
a = [LI() for _ in range(n)]
flag = [True]*m
ans = inf
f(flag)
print(ans)