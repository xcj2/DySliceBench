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

d = [(1,0),(0,1)]
def solve():
    h,w = LI()
    s = [input() for i in range(h)]
    bfs = [[float("inf")]*w for i in range(h)]
    bfs[0][0] = 1&(s[0][0] == "#")
    q = [(bfs[0][0],0,0)]
    while q:
        b,y,x = heappop(q)
        if (y,x) == (h-1,w-1):
            print(b)
            return
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if 0 <= ny < h and 0 <= nx < w:
                if s[ny][nx] == "#" and s[y][x] != "#":
                    nb = b+1
                else:
                    nb = b
                if nb < bfs[ny][nx]:
                    bfs[ny][nx] = nb
                    heappush(q,(nb,ny,nx))
    return

#Solve
if __name__ == "__main__":
    solve()
