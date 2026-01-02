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
P,Y = Line(M)

a = defaultdict(list)
for i in range(M):
    a[P[i]].append([Y[i],i])

for p in a.keys():
    a[p].sort(key = lambda x:x[0])

b = []
for p in a.keys():
    for i,y in enumerate(a[p]):
        b.append([str(p).zfill(6)+str(i+1).zfill(6),y[1]])

b.sort(key = lambda x: x[1])
for i in range(M):
    print(b[i][0])