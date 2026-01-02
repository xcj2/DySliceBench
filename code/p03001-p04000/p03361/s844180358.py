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
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

H,W = I()
maze = [list(s()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            F = 0
            if i != 0 :
                if maze[i-1][j] == '#':
                    F = 1
            if i != H-1:
                if maze[i+1][j] == '#':
                    F = 1
            if j != 0:
                if maze[i][j-1] == '#':
                    F = 1
            if j != W-1:
                if maze[i][j+1] == '#':
                    F = 1
            if not F:
                print('No')
                exit()
print('Yes')