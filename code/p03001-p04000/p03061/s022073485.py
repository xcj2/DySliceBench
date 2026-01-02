# -*- coding: utf-8 -*-

import sys
if sys.version_info.minor >= 5: from math import gcd
else: from fractions import gcd

def input(): return sys.stdin.readline().strip()
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

N=INT()
A=LIST()

# 予め左右から累積GCDを取っておく
L=[0]*(N+2)
for i in range(N):
    L[i+1]=gcd(L[i], A[i])
R=[0]*(N+2)
for i in range(N-1, -1, -1):
    R[i+1]=gcd(R[i+2], A[i])

# 1箇所除いてどうなるかを全部試しても、各回GCD1回ずつで済む
ans=0
for i in range(N):
    ans=max(ans, gcd(L[i], R[i+2]))
print(ans)
