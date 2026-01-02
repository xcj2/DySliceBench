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

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

n,a,b,c = LI()
l = [I() for _ in range(n)]

s = a+b+c
ans = inf
for i in range(1<<n):
    lst = []
    t = 0
    for j in range(n):
        if i >> j & 1:
            t += 1
            lst.append(l[j])
    if t < 3:
        continue
    for j in range(3**t):
        tmp = '0'*t + Base_10_to_n(j,3)
        tmp = tmp[-t:]
        B = [0]*t
        for k in range(t):
            if str(tmp[k]) == '1':
                B[k] = 1
            elif str(tmp[k]) == '2':
                B[k] = 2
        X = [[],[],[]]
        for k in range(t):
            X[B[k]].append(lst[k])
        if len(X[0]) == 0:
            continue
        if len(X[1]) == 0:
            continue
        if len(X[2]) == 0:
            continue
        cost = abs(sum(X[0])-a)
        cost += abs(sum(X[1])-b)
        cost += abs(sum(X[2])-c)
        cost += 10*(len(X[0])-1)
        cost += 10*(len(X[1])-1)
        cost += 10*(len(X[2])-1)
        ans = min(ans,cost)
print(ans)