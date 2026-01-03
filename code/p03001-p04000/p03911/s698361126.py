#!/usr/bin/env python3
#CODEFESTIVAL2016Final C

import sys
import math
import bisect
import time
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

def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def union(x,y):
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

n,m = LI()
par = [i for i in range(n)]
rank = [0]*n
language = [[] for _ in range(m)]
for i in range(n):
    a = LI()
    k = a[0]
    for j in range(1,k+1):
        language[a[j]-1].append(i)
for i in range(m):
    l = len(language[i])
    for j in range(l-1):
        if root(language[i][j]) != root(language[i][j+1]):
                union(language[i][j],language[i][j+1])
for i in range(m)[::-1]:
    l = len(language[i])
    for j in range(l-1):
        if root(language[i][j]) != root(language[i][j+1]):
            union(language[i][j],language[i][j+1])
for i in range(n-1):
    if par[i] != par[i+1]:
        print('NO')
        quit()
print('YES')
