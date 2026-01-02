# -*- coding: utf-8 -*-

import sys

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

X,Y,Z,K=MAP()
A=LIST()
B=LIST()
C=LIST()

AB=[]
for i in range(X):
    for j in range(Y):
        AB.append(A[i]+B[j])
AB.sort(reverse=True)
AB=AB[:3000]

ABC=[]
for i in range(len(AB)):
    for j in range(Z):
        ABC.append(AB[i]+C[j])
ABC.sort(reverse=True)

for i in range(K):
    print(ABC[i])
