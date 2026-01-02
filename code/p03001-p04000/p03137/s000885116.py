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

N,M = II()
X = III()

if N>=M:
    print(0)
    exit()

X.sort()
d = []
for i in range(M-1):
    d.append(X[i+1]-X[i])

d.sort(reverse=True)
print(X[M-1]-X[0]-sum(d[:N-1]))