# -*- coding: utf-8 -*-

import sys
from collections import Counter

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

N = INT()
A = LIST()

li = [{1: N}]
for i in range(1, N-1):
    li.append({i: i, i+1: min(N-i+max(N-i-2, 0), N)})
li.append({N-1: N})

C = Counter(A)
for d in li:
    cnt = 0
    for k, v in d.items():
        if C[k] <= v:
            cnt += C[k]
        else:
            break
    else:
        if cnt == N:
            Yes()
            exit()
No()
