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

N,Q = II()
S = str(input())
l,r = Line(Q)

a = [0]*N
for i in range(N-1)[::-1]:
    if S[i:i+2] == 'AC':
        a[i] = a[i+1]+1
    else:
        a[i] = a[i+1]

for i in range(Q):
    print(a[l[i]-1]-a[r[i]-1])