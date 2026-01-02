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

from itertools import product

N = I()
F = [[[0]*2 for _ in range(5)] for _ in range(N)]
P = []
for i in range(N):
    temp = III()
    for j in range(5):
        for k in range(2):
            F[i][j][k] = temp[j*2+k]
for _ in range(N):
    P.append(III())

ans = -float('inf')
A = list(product([True, False],repeat=10))
for a in A:
    if a == (False,)*10:
        continue
    val = 0
    for i in range(N):
        count = 0
        for j in range(5):
            for k in range(2):
                if a[2*j+k]==True and F[i][j][k]==1:
                    count += 1
        val += P[i][count]
    if val > ans:
        ans = val

print(ans)