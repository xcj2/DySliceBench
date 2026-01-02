# -*- coding: utf-8 -*-

import sys
from collections import Counter
from copy import copy

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

N=INT()
D=LIST()

L=[0]

C=Counter(D)
S=[]
for k, v in C.items():
    if v>=3:
        print(0)
        exit()
    elif v>=2:
        L.append(k)
        L.append(24-k)
    else:
        S.append(k)

mx=0
for i in range(1<<len(S)):
    L2=copy(L)
    for j in range(len(S)):
        if i>>j&1:
            L2.append(S[j])
        else:
            L2.append(24-S[j])
    L2.sort()
    L2=L2+[l+24 for l in L2]
    mn=INF
    for i in range(1, len(L2)):
        mn=min(mn, abs(L2[i-1]-L2[i])%24)
    mx=max(mx, mn)
print(mx)
