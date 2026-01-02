import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

import copy

N,M,L = II()
A,B,C = Line(M,3)
Q = I()
s,t = Line(Q,2)

E = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    E[i][i] = 0
for i in range(M):
    E[A[i]-1][B[i]-1] = C[i]
    E[B[i]-1][A[i]-1] = C[i]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if E[i][j] > E[i][k]+E[k][j]:
                E[i][j] = E[i][k]+E[k][j]

E2 = [[float('inf')]*N for _ in range(N)]

for i in range(N):
    E2[i][i] = 0
for i in range(N):
    for j in range(N):
        if E[i][j]<=L:
            E2[i][j] = 1
            E2[j][i] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if E2[i][j] > E2[i][k]+E2[k][j]:
                E2[i][j] = E2[i][k]+E2[k][j]

for i in range(Q):
    if E2[s[i]-1][t[i]-1] == float('inf'):
        print(-1)
    else:
        print(E2[s[i]-1][t[i]-1]-1)