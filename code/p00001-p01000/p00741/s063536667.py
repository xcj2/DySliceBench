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

D = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
def solve(w,h):
    def bfs(y,x):
        q = deque([(y,x)])
        while q:
            y,x = q.popleft()
            for dx,dy in D:
                ny,nx = y+dy,x+dx
                if 0 <= ny < h and 0 <= nx < w:
                    if c[ny][nx] and not d[ny][nx]:
                        d[ny][nx] = 1
                        q.append((ny,nx))
    c = LIR(h)
    d = [[0]*w for i in range(h)]
    ans = 0
    for y in range(h):
        for x in range(w):
            if c[y][x] and not d[y][x]:
                ans += 1
                d[y][x] = 1
                bfs(y,x)
    print(ans)
    return

#Solve
if __name__ == "__main__":
    while 1:
        w,h = LI()
        if w == h == 0:
            break
        solve(w,h)

