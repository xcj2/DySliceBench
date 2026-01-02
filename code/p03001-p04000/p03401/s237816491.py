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
A = III()

d = abs(A[0])
for i in range(N-1):
    d += abs(A[i]-A[i+1])
d += abs(A[N-1])

for i in range(N):
    if 1<=i<=N-2:
        print(d-abs(A[i-1]-A[i])-abs(A[i]-A[i+1])+abs(A[i-1]-A[i+1]))
    elif i==0:
        print(d-abs(-A[i])-abs(A[i]-A[i+1])+abs(-A[i+1]))
    else:
        print(d-abs(A[i-1]-A[i])-abs(A[i])+abs(A[i-1]))