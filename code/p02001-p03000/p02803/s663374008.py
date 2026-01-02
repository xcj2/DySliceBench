import sys
from math import factorial
from fractions import Fraction
import heapq, bisect, fractions
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**9 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
MOD = 10**9 + 7

h, w = MAP()
maze = [[]for i in range(h)]
for i in range(h):
    si = list(input())
    maze[i] = si

ans = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(sx, sy):
    q = []
    d = [[INF]*w for i in range(h)]
    heapq.heappush(q, [0, sx, sy])
    d[sx][sy] = 0
    res = 0
    while len(q) >0:
        p = heapq.heappop(q)
        for i in range(4):
            nx = p[1] + dx[i]
            ny = p[2] + dy[i]
            if 0<=nx<h and 0<=ny<w and maze[nx][ny] == '.' and d[nx][ny] == INF:
                heapq.heappush(q, [d[p[1]][p[2]] + 1, nx, ny])
                d[nx][ny] = d[p[1]][p[2]] + 1
                if d[nx][ny] > res:
                    res = d[nx][ny]
    return res

for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            ans.append(dfs(i, j))

print(max(ans))
