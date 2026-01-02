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

n = I()
a = LI()
b = LI()
a = [(a[i],i) for i in range(n)]
b = [(b[i],i) for i in range(n)]
a.sort()
b.sort()
for i in range(n):
    if b[i][0] < a[i][0]:
        print('No')
        quit()

edges = [None]*n
for i in range(n):
    edges[a[i][1]] = b[i][1]

lst = [None]*n

def dfs(s):
    if lst[s] == None:
        lst[s] = tmp
        dfs(edges[s])
    return

tmp = 0
for i in range(n):
    if lst[i] == None:
        dfs(i)
        tmp += 1

lst = list(Counter(lst).values())
if len(lst) >= 2:
    print('Yes')
    quit()

for i in range(n-1):
    if b[i][0] >= a[i+1][0]:
        print('Yes')
        quit()

print('No')
