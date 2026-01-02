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
a,b = Line(N)
c,d = Line(N)

x = []
for i in range(N):
    x.append([a[i],b[i],0])
    x.append([c[i],d[i],1])

x.sort(key=lambda x: x[0])

use = {}
for i in range(2*N):
    use[i] = False

ans = 0
for i in range(2*N)[::-1]:
    if x[i][2] != 0:
        continue
    else:
        index = 2*N
        val = float('inf')
        for j in range(i+1,2*N):
            if x[j][1]>x[i][1] and x[j][1]<val and use[j]!=True and x[j][2]==1:
                index = j
                val = x[j][1]
        if index != 2*N:
            ans += 1
            use[index] = True

print(ans)