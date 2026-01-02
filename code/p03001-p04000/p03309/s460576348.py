# -*- coding: utf-8 -*-

import sys

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

def check(m):
    sm = 0
    for i, a in enumerate(A):
        sm += abs(a - (m+i+1))
    return sm

# 三分探索
low = -INF
hi = INF
while low+2 < hi:
    m1 = (low*2+hi) // 3
    m2 = (low+hi*2) // 3
    res1 = check(m1)
    res2 = check(m2)
    # 今回は下に凸な関数なので値の小さい方に向かって狭めていく
    if res1 <= res2:
        hi = m2
    else:
        low = m1

ans = INF
for i in range(low, low+2):
    ans = min(ans, check(i))
print(ans)
