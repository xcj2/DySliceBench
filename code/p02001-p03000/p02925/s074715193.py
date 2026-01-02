#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

N = I()
A = []
for _ in range(N):
    A.append(III())

S = []
for i in range(N):
    j = A[i][0]-1
    if i==A[j][0]-1:
        if i<j:
            S.append((i,j))

c = [0]*N
ans = 0
while S:
    q = []
    for i,j in S:
        c[i] += 1
        c[j] += 1
        if c[i] <= N-2:
            x = A[i][c[i]]-1
            if A[x][c[x]]-1==i:
                q.append((min(i,x), max(i,x)))
        if c[j] <= N-2:
            y = A[j][c[j]]-1
            if A[y][c[y]]-1==j:
                q.append((min(j,y), max(j,y)))
    S = q
    ans += 1

for i in range(N):
    if c[i] != N-1:
        print(-1)
        exit()

print(ans)