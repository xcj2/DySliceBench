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
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

N,M = I()
maze1 = [list(s()) for _ in range(N)]
maze2 = [list(s()) for _ in range(M)]
L = [[-1]*N for _ in range(N)]
def dfs(x,y):
    if x == N or y == N:
        return
    if x-i == M or y-j == M:
        return
    if maze1[x][y] != maze2[x-i][y-j]:
        L[i][j] = 0
        return
    dfs(x+1,y)
    dfs(x,y+1)
for i in range(N-M+1):
    for j in range(N-M+1):
        dfs(i,j)
        if L[i][j] == -1:
            print('Yes')
            exit()
print('No')