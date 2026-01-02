import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
import collections
from collections import deque 

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# ---------------------------------------

mod = 10**9 + 7

H, W = inpl()
a = []
flag = [[False] * W for i in range(H)]
for i in range(H):
    a.append(input().strip())
_debug(a)
dp = [[0] * (W+1) for i in range(H+1)]
dp[0][0] = 1

for i in range(max(H, W)):
    if i < H:
        for j in range(W):
            if a[i][j] == "#" or flag[i][j]:
                continue
            flag[i][j] = True
            for x, y in ((0, 1), (1, 0)):
                dp[i+x][j+y] += dp[i][j]
                dp[i+x][j+y] %= mod
    if i < W:
        for j in range(H):
            if a[j][i] == "#" or flag[j][i]:
                continue
            flag[j][i] = True
            for x, y in ((0, 1), (1, 0)):
                dp[j+x][i+y] += dp[j][i]
                dp[j+x][i+y] %= mod
    
print(dp[H-1][W-1])