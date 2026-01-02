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
A,B = Line(N)
c = []
for i in range(N):
    c.append([A[i],B[i]])

c.sort()
ans = 0
count = 0

for i in range(N):
    x = min(c[i][1], M-count)
    ans += x*c[i][0]
    count += x
    if count==M:
        break

print(ans)