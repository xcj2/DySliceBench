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

N,Q = II()
a = [0]*(N-1)
b = [0]*(N-1)
p = [0]*Q
x = [0]*Q

for i in range(N-1):
    a1,b1 = II()
    a[i] = a1-1
    b[i] = b1-1

for i in range(Q):
    p1,x1 = II()
    p[i] = p1-1
    x[i] = x1


parent = defaultdict(list)
for i in range(N-1):
    parent[b[i]].append(a[i])

val = [0]*N
for i in range(Q):
    val[p[i]] += x[i]

for i in range(1,N):
    val[i] += val[parent[i][0]]

print(*val)