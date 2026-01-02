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


N,M = I()
links = [[] for _ in range(N)]
link = []
for i in range(M):
    a,b = I()
    links[a-1].append(b-1)
    links[b-1].append(a-1)
    link.append((a-1,b-1))
def dfs(n):
    if visited[n] == 1:
        return
    visited[n] = 1
    L = linky[n]
    for l in L:
        dfs(l)
ans = 0
for i in range(M):
    visited = [0]*N
    linky = deepcopy(links)
    a,b = link[i]
    linky[a].remove(b)
    linky[b].remove(a)
    dfs(0)
    if 0 in visited:
        ans += 1
print(ans)