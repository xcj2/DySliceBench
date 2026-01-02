import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

from itertools import permutations

N,M,R = LI()
r = LI()
A,B,C = MI(M,3)

def WF(E,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                E[i][j] = min(E[i][j],E[i][k]+E[k][j])
    return E

E = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    E[i][i] = 0         #自分との距離は0にしておく
for i in range(M):
    E[A[i]-1][B[i]-1] = C[i]
    E[B[i]-1][A[i]-1] = C[i]     #無向枝の場合両方格納

E2 = WF(E,N) #全ての点の組み合わせの距離を2次元配列で返す

X = list(permutations(r))
ans = float('inf')

for x in X:
    now = 0
    for i in range(1,len(x)):
        now += E2[x[i-1]-1][x[i]-1]
    if now < ans:
        ans = now

print(ans)