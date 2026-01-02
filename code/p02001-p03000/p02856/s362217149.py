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

# (nxt, cnt)
D = {
    0: (0, 1),
    1: (2, 1),
    2: (4, 1),
    3: (6, 1),
    4: (8, 1),
    5: (1, 2),
    6: (3, 2),
    7: (5, 2),
    8: (7, 2),
    9: (9, 2),
}

M = INT()
C = Counter()
for i in range(M):
    d, c = MAP()
    C[d] += c

def calc(a, cnt):
    sm = 0
    odd = []
    while cnt > 1:
        if cnt % 2 == 1:
            odd.append(a)
            cnt -= 1
        cnt //= 2
        sm += cnt * D[a][1]
        a = D[a][0]
    for b in odd:
        a += b
        sm += 1
        if a >= 10:
            a = int(str(a)[0]) + int(str(a)[1])
            sm += 1
    return (a, sm)

ans = 0
A = []
for k, v in C.items():
    a, sm = calc(k, v)
    ans += sm
    A.append(a)

for i in range(1, len(A)):
    A[i] += A[i-1]
    ans += 1
    if A[i] >= 10:
        A[i] = int(str(A[i])[0]) + int(str(A[i])[1])
        ans += 1
print(ans)
