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

from bisect import bisect_left

N,K = II()
x = III()
y = []
for i in range(N):
    if x[i]!=0:
        y.append(x[i])
    else:
        K -= 1
        N -= 1

minus = bisect_left(x,0)
ans = float('inf')

for i in range(min(minus+1,K+1)):
    if i==0: a=0
    else: a = y[minus-1-i+1]
    if K-i==0: b=0
    else:
        if minus+K-i-1<=N-1: 
            b = y[minus+K-i-1]
        else:
            continue
    temp = min(b-2*a,2*b-a)
    if temp<ans:
        ans = temp

print(ans)