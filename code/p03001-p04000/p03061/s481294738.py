# -*- coding: utf-8 -*-

import sys
if sys.version_info.minor >= 5: from math import gcd
else: from fractions import gcd
from functools import reduce

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def gcd_list(nums): return reduce(gcd, nums, nums[0])
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

L=[0]*N
L[0]=A[0]
for i in range(1, N):
    L[i]=gcd(L[i-1], A[i])
R=[0]*N
R[-1]=A[-1]
for i in range(N-2, -1, -1):
    R[i]=gcd(R[i+1], A[i])

ans=0
for i in range(N):
    if i==0:
        ans=max(ans, R[1])
    elif i==N-1:
        ans=max(ans, L[-2])
    else:
        ans=max(ans, gcd(L[i-1], R[i+1]))
print(ans)
