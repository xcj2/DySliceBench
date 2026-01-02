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

def lucas(n, k):
    return (n&k) == k

N = INT()
A = [a-1 for a in list(map(int, input()))]

def check(A):
    mod2 = 0
    for i, a in enumerate(A):
        if a == 1:
            mod2 += lucas(N-1, i)
            mod2 %= 2
    return mod2

res = check(A)
if res == 1:
    print(1)
    exit()

if A.count(1):
    print(0)
    exit()

A = [a//2 for a in A]
res = check(A)
if res == 1:
    print(2)
else:
    print(0)
