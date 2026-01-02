import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

H,W = LI()
c = []
for i in range(10):
    temp = LI()
    c.append(temp)

A = []
for i in range(H):
    temp = LI()
    A.append(temp)

def WF(E,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                E[i][j] = min(E[i][j],E[i][k]+E[k][j])
    return E

E = [[float('inf')]*10 for _ in range(10)]
for i in range(10):
    E[i][i] = 0         #自分との距離は0にしておく
for i in range(10):
    for j in range(10):
        E[i][j] = c[i][j]

dist = WF(E,10)

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] != -1:
            ans += dist[A[i][j]][1]

print(ans)