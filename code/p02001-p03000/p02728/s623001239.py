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

def dfs_1(s,p): #部分木のサイズを数えるdfs
    par[s] = p
    for v in edges[s]:
        if v == p:
            continue
        size[s] += dfs_1(v,s)
    return size[s]

def dfs_2(s,p): #1を根としたときに進む向きのdp計算用dfs
    dp1[s] = fact[size[s]-1]
    for v in edges[s]:
        if v == p:
            continue
        dp1[s] = (dp1[s]*dfs_2(v,s))%mod
        dp1[s] = (dp1[s]*pow(fact[size[v]], mod-2, mod))%mod
    return dp1[s]

def comb(n,r):
    return fact[n]*pow(fact[r],mod-2,mod)*pow(fact[n-r],mod-2,mod) % mod

def bfs(s):
    que = deque()
    que.append((s,-1))
    while que:
        v,p = que.popleft()
        if v == 0:
            dp2[v] = dp1[v]
        else:
            inv = (dp2[p]*pow((dp1[v]*comb(n-1,size[v]))%mod,mod-2,mod)) % mod
            dp2[v] = (dp1[v]*inv*comb(n-1,size[v]-1)) % mod
        for u in edges[v]:
            if u == p:
                continue
            que.append((u,v))
n = I()
fact = [1]*(n+1)
par = [None]*n
for i in range(1,n+1):
    fact[i] = i*fact[i-1]
    fact[i] %= mod

edges = [[] for _ in range(n)]
size = [1]*n
dp1 = [0]*n #1を根としたときに進む向きのdp
for _ in range(n-1):
    a,b = LI()
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

dfs_1(0,-1)
dfs_2(0,-1)
dp2 = [0]*n
bfs(0)
for i in dp2:
    print(i)


