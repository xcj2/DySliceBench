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
h = [I() for _ in range(N)]
h.sort()

ans = float('inf')

for i in range(N-K+1):
    temp = h[i+K-1]-h[i]
    if temp < ans:
        ans = temp

print(ans)