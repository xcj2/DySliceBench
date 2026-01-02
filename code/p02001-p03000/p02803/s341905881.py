import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10**9)
mod = 10**9+7

H,W = I()
maze = [list(s()) for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            continue
        dist = [[-1]*W for _ in range(H)]
        dist[i][j] = 0
        que = deque([[i,j]])
        while que:
            h,w = que.pop()
            for dh,dw in [[1,0],[0,1],[-1,0],[0,-1]]:
                nh = h+dh
                nw = w+dw
                if nh < 0 or nw < 0 or nh >= H or nw >= W:
                    continue
                if maze[nh][nw] == '#':
                    continue
                if dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w]+1
                    que.appendleft([nh,nw])
        ans = max(ans,max([max(d) for d in dist]))
print(ans)
