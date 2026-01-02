# -*- coding: utf-8 -*-

import sys
from itertools import accumulate
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

N, P = MAP()
A = list(map(int, input()))

if P == 2 or P == 5:
    ans = 0
    for i, a in enumerate(A):
        if a % P == 0:
            ans += i + 1
    print(ans)
    exit()

acc = [0] * N
cur = A[-1] % P
acc[-1] = cur
k = 1
for i in range(N-2, -1, -1):
    cur += pow(10, k, P) * A[i]
    cur %= P
    acc[i] = cur
    k += 1
acc = acc + [0]

C = Counter(acc)
ans = 0
for v in C.values():
    ans += v * (v-1) // 2
print(ans)
