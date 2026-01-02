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

N,A,B,C = II()
l = [I() for _ in range(N)]
inf = float('inf')

def solve(cur,a,b,c):
    if cur==N:
        return abs(a-A)+abs(b-B)+abs(c-C)-30 if min(a,b,c)>0 else inf
    ret0 = solve(cur+1,a,b,c)
    ret1 = solve(cur+1,a+l[cur],b,c)+10
    ret2 = solve(cur+1,a,b+l[cur],c)+10
    ret3 = solve(cur+1,a,b,c+l[cur])+10
    return min(ret0,ret1,ret2,ret3)

print(solve(0,0,0,0))