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

N, K = MAP()
R, S, P = MAP()
T = list(input())

T2 = [[] for i in range(K)]
for i, t in enumerate(T):
    T2[i%K].append(t)

ans = 0
for k in range(K):
    dp = list2d(len(T2[k])+1, 3, 0)
    for i, t in enumerate(T2[k]):
        for j in range(3):
            for l in range(3):
                if i != 0 and j == l:
                    continue
                nxt = 0
                if t == 'r' and l == 2:
                    nxt = P
                elif t == 's' and l == 0:
                    nxt = R
                elif t == 'p' and l == 1:
                    nxt = S
                dp[i+1][l] = max(dp[i+1][l], dp[i][j] + nxt)
    ans += max(dp[len(T2[k])])
print(ans)
