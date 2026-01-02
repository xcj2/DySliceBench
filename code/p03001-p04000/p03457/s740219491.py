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
t,x,y = Line(N)

t0 = 0
x0 = 0
y0 = 0

for i in range(N):
    d = abs(x[i]-x0) + abs(y[i]-y0)
    a = t[i]-t0-d
    if a>=0 and a%2==0:
        t0 = t[i]
        x0 = x[i]
        y0 = y[i]
    else:
        print('No')
        exit()

print('Yes')