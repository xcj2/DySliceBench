# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
from bisect import bisect_right

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

S = input()
T = input()
N = len(S)

d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)
for k, v in d.items():
    d[k].append(INF)

cur = -1
ans = 0
for i, t in enumerate(T):
    if t not in d:
        print(-1)
        exit()
    idx = bisect_right(d[t], cur)
    if d[t][idx] == INF:
        ans += N
        cur = d[t][0]
    else:
        cur = d[t][idx]
ans += cur+1
print(ans)
