import sys
import math
import itertools
import bisect
from copy import copy,deepcopy
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

H,W,K = I()
maze = [list(s()) for _ in range(H)]
cnty = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            cnty += 1
h = [i for i in range(H)]
w = [i for i in range(W)]
ans = 0
for i in range(H):
    for j in range(W):
        mazey = copy(maze)
        hc = list(itertools.combinations(h,i))
        wc = list(itertools.combinations(w,j))
        for k in range(len(hc)):
            for l in range(len(wc)):
                mazey = copy(maze)
                cnt = 0
                if hc[k]:
                    for m in hc[k]:
                        cnt += mazey[m].count('#')
                        mazey[m] = ['.']*W
                if wc[l]:
                    for m in wc[l]:
                        for n in range(H):
                            if mazey[n][m] == '#':
                                cnt += 1
                if cnty - cnt == K:
                    ans += 1
print(ans)