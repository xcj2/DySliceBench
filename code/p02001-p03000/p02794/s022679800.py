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

def dfs(s,g,p):
    global tmp
    if s == g:
        tmp = []
        return True
    for (v,i) in edge[s]:
        if v == p:
            continue
        if dfs(v,g,s):
            tmp.append(i)
            return True
    return False

n = I()
edge = [[] for i in range(n)]
for i in range(n-1):
    a,b = LI()
    a -= 1
    b -= 1
    edge[a].append((b,i))
    edge[b].append((a,i))

m = I()
lst = []
tmp = []
for _ in range(m):
    u,v = LI()
    u -= 1
    v -= 1
    dfs(u,v,-1)
    lst.append(tmp)

"""m個の制約がどの辺を通るかbitで管理"""
e = [0]*m
for i in range(m):
    x = 0
    for j in lst[i]:
        x |= 1<<j
    e[i] = x

"""包除原理"""
ans = 0
for i in range(1<<m):
    black = 0 #制約の通る辺をbitで管理
    cnt = 0 #使う制約の個数
    """どの制約を使うか"""
    for j in range(m):
        if i>>j & 1:
            cnt += 1
            black |= e[j]

    cnt2 = 0 #制約内の辺の本数
    for j in range(n-1):
        if black >> j & 1:
            cnt2 += 1
    if cnt % 2: #制約奇数個の場合
        ans -= 1<<(n-1-cnt2) #-2**((n-1本の辺)-(制約内の辺の本数))
    else:
        ans += 1<<(n-1-cnt2) #+2**((n-1本の辺)-(制約内の辺の本数))
print(ans)