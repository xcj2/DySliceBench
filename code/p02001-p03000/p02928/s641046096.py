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

N,K = II()
A = III()

r = [0]*N
l = [0]*N

for i in range(N):
    for j in range(i+1,N):
        if A[j]<A[i]:
            r[i] += 1
    for j in range(i):
        if A[j]<A[i]:
            l[i] += 1

ans = 0

for i in range(N):
    ans += r[i]*K*(K+1)//2
    ans %= mod
    ans += l[i]*(K-1)*K//2
    ans %= mod

print(ans)