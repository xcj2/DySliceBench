# -*- coding: utf-8 -*-

import sys
from heapq import heappop, heappush, heapify

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

K,T=MAP()
A=LIST()
A=[(-A[i], i) for i in range(T)]
heapify(A)

prev=-1
while len(A):
    v,i=heappop(A)
    if i!=prev:
        v+=1
        prev=i
        if v!=0:
            heappush(A, (v, i))
    else:
        if len(A)==0:
            print(-v)
            exit()
        v2,i2=heappop(A)
        v2+=1
        prev=i2
        if v2!=0:
            heappush(A, (v2, i2))
        heappush(A, (v, i))
print(0)
