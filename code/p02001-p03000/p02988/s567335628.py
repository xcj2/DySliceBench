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

n = I()
p = III()

count = 0
for i in range(1,n-1):
    if max(p[i-1],p[i],p[i+1])!=p[i] and min(p[i-1],p[i],p[i+1])!=p[i]:
        count += 1

print(count)