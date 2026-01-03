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

def WF(E,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                E[i][j]=min(E[i][j],E[i][k]+E[k][j])
    return E

N,M = II()
a,b,c = Line(M,3)

E = [[10**30]*N for _ in range(N)]
for i in range(N):
    E[i][i] = 0         #自分との距離は0にしておく
for i in range(M):
    E[a[i]-1][b[i]-1] = c[i]
    E[b[i]-1][a[i]-1] = c[i]     #無向枝の場合両方格納

E2 = WF(E,N)

ans = 0
for i in range(M):
    if E2[a[i]-1][b[i]-1]<c[i]:
        ans += 1

print(ans)