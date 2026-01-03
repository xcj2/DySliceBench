#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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
    a = [input() for i in range(h)]
    q = deque([(0,0)])
    bfs = [[0]*w for i in range(h)]
    bfs[0][0] = 1
    while q:
        y,x = q.popleft()
        if q:
            print("Impossible")
            return
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if 0 <= ny < h and 0 <= nx < w:
                if a[ny][nx] != ".":
                    if not bfs[ny][nx]:
                        bfs[ny][nx] = 1
                        q.append((ny,nx))
    for y in range(h):
        for x in range(w):
            if a[y][x] != "." and not bfs[y][x]:
                print("Impossible")
                return
    print("Possible")
    return

#Solve
if __name__ == "__main__":
    solve()
