# -*- coding: utf-8 -*-

import sys
from itertools import combinations
from collections import Counter

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

if N==1:
    print(1)
    exit()

xy=[]
for i in range(N):
    x,y=MAP()
    xy.append((x, y))

C=Counter()
for comb in combinations(xy, 2):
    a,b=comb
    if a[0]-b[0]==0:
        key=INF
    else:
        key=(a[1]-b[1])/(a[0]-b[0])
    C[(key, abs(a[0]-b[0]), abs(a[1]-b[1]))]+=1

mx=max(C.values())
print(N-mx)
