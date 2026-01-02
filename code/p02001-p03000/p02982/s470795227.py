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

N,D = II()

X = []
for i in range(N):
    X.append(III())

ans = 0
for i in range(N):
    for j in range(i+1,N):
        l = 0
        for k in range(D):
            l += (X[i][k]-X[j][k])**2
        if math.sqrt(l) == int(math.sqrt(l)):
            ans += 1

print(ans)