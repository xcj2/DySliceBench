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
N,M = II()
k = [0]*M
p = [0]*M
s = []
for i in range(M):
    a = III()
    k[i] = a[0]
    temp = a[1:]
    temp = list(map(lambda x:x-1,temp))
    s.append(temp)

p = III()

x=list(product([0,1],repeat=N))
count = 0

for i in range(len(x)):
    for j in range(M):
        scount = 0
        for k in s[j]:
            if x[i][k]==1:
                scount += 1
        if scount%2 != p[j]:
            break
        if j==M-1:
            count += 1

print(count)