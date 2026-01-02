#!/usr/bin/env python3
#エクサウィザーズ2019 C

import sys
import math
import bisect
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

def f(x,f):
    for i,j in td:
        if s[x] == i:
            if j == 'R':
                x += 1
                if x == n and f == 0:
                    return True
                elif x == n and f == 1:
                    return False
            else:
                x -= 1
                if x == -1 and f == 1:
                    return True
                elif x == -1 and f == 0:
                    return False
    return False

n,q = LI()
s = input()
td = [list(map(str,input().split())) for _ in range(q)]
ng,ok = -1,n
while abs(ok - ng) > 1:
    mid = (ok + ng)//2
    if f(mid,0):
        ok = mid
    else:
        ng = mid
R = ok
ng,ok = -1,n
while abs(ok - ng) > 1:
    mid = (ok + ng)//2
    if f(mid,1):
        ng = mid
    else:
        ok = mid
L = ng
print(R-L-1)
