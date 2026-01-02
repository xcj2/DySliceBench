#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    m = [(1,0),(-1,0),(0,1),(0,-1)]
    def bfs(sx,sy):
        d = [[float("inf")]*h for i in range(w)]
        d[sx][sy] = 0
        q = deque([(sx,sy)])
        res = 0
        while q:
            x,y = q.popleft()
            nd = d[x][y]+1
            for dx,dy in m:
                nx,ny = x+dx,y+dy
                if 0 <= nx < w and 0 <= ny < h:
                    if s[ny][nx] == "#":
                        continue
                    if nd < d[nx][ny]:
                        d[nx][ny] = nd
                        q.append((nx,ny))
                        res = nd
        return res
    h,w = LI()
    s = [input() for i in range(h)]
    ans = 0
    for y in range(h):
        for x in range(w):
            if  s[y][x] == ".":
                res = bfs(x,y)
                if ans < res:
                    ans = res
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
