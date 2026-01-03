# -*- coding: utf-8 -*-

import sys
from itertools import combinations, accumulate

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

N,K=MAP()
A=LIST()

acc=list(accumulate(A, max))

ans=INF
for comb in combinations(range(N), K):
    sm=0
    for i, n in enumerate(comb):
        if i==0:
            cost=max(acc[n]-A[n], 0)
            if n!=0 and acc[n-1]==acc[n]:
                cost+=1
        else:
            cost=max(prev-A[n]+1, acc[n-1]-A[n]+1, 0)
        sm+=cost
        prev=A[n]+cost
    ans=min(ans, sm)
print(ans)
