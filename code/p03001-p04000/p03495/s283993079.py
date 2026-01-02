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

x = defaultdict(int)

for i in range(N):
    x[A[i]] += 1

num = len(x.keys())

if num<=K:
    print(0)
else:
    x2 = list(x.values())
    x2.sort()
    n = num-K
    ans = 0
    for i in range(n):
        ans += x2[i]
    print(ans)