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
x,y,h = Line(N)

for i in range(N):
    if h[i]!=0:
        x0,y0,h0 = x[i],y[i],h[i]
        break

for cx in range(101):
    for cy in range(101):
        H = abs(x0-cx)+abs(y0-cy)+h0
        flag = True
        for i in range(N):
            if max(H-abs(x[i]-cx)-abs(y[i]-cy),0)!=h[i]:
                flag = False
                break
        if flag:
            break
    else:
        continue
    break

print(cx,cy,H)