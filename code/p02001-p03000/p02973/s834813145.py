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

N = I()
A = [0]*N
for i in range(N):
    A[i] = I()

val = [-1]*N
for i in range(N):
    temp = bisect_left(val,A[i])
    val[temp-1] = A[i]

ans = 0
for i in range(N):
    if val[i]!=-1:
        ans += 1

print(ans)