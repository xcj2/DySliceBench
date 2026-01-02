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

cnt = 1
def dfs(x):
    global cnt
    if s[x] == None:
        s[x] = cnt
        cnt += 1
    for v in edges[x]:
        if s[v] == None:
            dfs(v)
    g[x] = cnt
    cnt += 1
    return 

n = I()
edges = [[] for _ in range(n)]
for i in range(n):
    edges[i] = list(map(lambda x:x-1,LI()[2:]))

s = [None]*n
g = [None]*n
for i in range(n):
    if s[i] == None:
        dfs(i)
for i in range(n):
    print(i+1,s[i],g[i])
    
    

