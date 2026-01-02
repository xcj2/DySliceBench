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

for i in range(N):
    A[i] -= i

A.sort()

if N%2==0:
    A = list(map(lambda x: x-A[N//2], A))
else:
    A = list(map(lambda x: x-A[(N-1)//2], A))


A = list(map(abs,A))

print(sum(A))