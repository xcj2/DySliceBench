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
a = III()

x = defaultdict(int)

for i in range(N):
    x[a[i]] += 1

ans = 0
for k in x.keys():
    if x[k]<k:
        ans += x[k]
    else:
        ans += x[k]-k

print(ans)