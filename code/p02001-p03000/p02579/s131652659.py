#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
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
    h,w = LI()
    cy,cx = LI()
    gy,gx = LI()
    s = [input() for _ in range(h)]
    cy -= 1
    cx -= 1
    gy -= 1
    gx -= 1
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    bfs = [[float("inf")]*w for i in range(h)]#コスト
    bfs[cy][cx] = 0
    q = deque([(cy,cx)])
    while q:
        y,x = q.popleft()
        b = bfs[y][x]
        if (y,x) == (gy,gx):
            print(b)
            return
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if 0 <= ny < h and 0 <= nx < w and s[ny][nx] != "#" and b < bfs[ny][nx]:
                bfs[ny][nx] = b
                q.appendleft((ny,nx))
        nb = b+1
        for dy in range(-2,3):
            for dx in range(-2,3):
                ny,nx = y+dy,x+dx
                if 0 <= ny < h and 0 <= nx < w and s[ny][nx] != "#" and nb < bfs[ny][nx]:
                    bfs[ny][nx] = nb
                    q.append((ny,nx))
    print(-1)
    return

#Solve
if __name__ == "__main__":
    solve()
