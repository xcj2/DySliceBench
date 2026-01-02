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

d = [(1,0),(-1,0),(0,1),(0,-1)]
def solve():
    def rotate(dice,d):
        d1,d2,d3,d4,d5,d6 = dice
        if d == (0,1):
            return (d4,d2,d1,d6,d5,d3)
        elif d == (0,-1):
            return (d3,d2,d6,d1,d5,d4)
        elif d == (1,0):
            return (d5,d1,d3,d4,d6,d2)
        else:
            return (d2,d6,d3,d4,d1,d5)
    h,w = LI()
    s = [input() for i in range(h)]
    bfs = [[0 for i in range(w)] for j in range(h)]
    bfs[0][0] = 1
    q = deque([(0,0,(1,2,3,4,5,6))])
    while q:
        y,x,dice = q.popleft()
        if y == h-1 and x == w-1:
            print("YES")
            return
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if 0 <= ny < h and 0 <= nx < w:
                nd = rotate(dice,(dy,dx))
                if not bfs[ny][nx] and str(nd[-1]) == s[ny][nx]:
                    bfs[ny][nx] = 1
                    q.append((ny,nx,nd))
    print("NO")
    return

#Solve
if __name__ == "__main__":
    solve()

