# -*- coding: utf-8 -*-

import sys
from collections import Counter
from functools import reduce
from operator import xor

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
A=[INT() for i in range(N)]

mnbit=[0]*N
for i, a in enumerate(A):
    bina=format(a, 'b')
    mnbit[i]=len(bina)-bina.rfind('1')
C=Counter(mnbit)

res=reduce(xor, A, 0)
ln=len(format(res, 'b'))
cnt=0
for i in range(ln):
    idx=ln-i
    if res>>(idx-1)&1:
        if C[idx]:
            res^=(1<<idx)-1
            cnt+=1
        else:
            print(-1)
            exit()
print(cnt)
