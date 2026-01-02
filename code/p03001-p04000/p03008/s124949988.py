# -*- coding: utf-8 -*-

import sys
from itertools import accumulate

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
B = LIST()

S1 = []
S2 = []
for i in range(3):
    if A[i] < B[i]:
        S1.append(i)
    else:
        S2.append(i)
        A[i], B[i] = B[i], A[i]

def calc(cnt, i):
    d = cnt // A[i]
    m = cnt % A[i]
    return d * B[i] + m

def count(S, N):
    if len(S) == 0:
        return N
    elif len(S) == 1:
        return calc(N, S[0])
    elif len(S) == 2:
        res = 0
        for x in range(N+1):
            y = N - x
            if y < 0:
                break
            cnt = calc(x, S[0]) + calc(y, S[1])
            res = max(res, cnt)
        return res
    else:
        res = 0
        for x in range(N+1):
            for y in range(N+1):
                z = N - x - y
                if z < 0:
                    break
                cnt = calc(x, S[0]) + calc(y, S[1]) + calc(z, S[2])
                res = max(res, cnt)
        return res

N2 = count(S1, N)
ans = count(S2, N2)
print(ans)
