from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007



def main():
    h, w = LI()
    grid = SRL(h)
    cnt = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '.':
                cnt += 1
                grid[y][x] = INF



    que = deque([(0, 0)])
    grid[0][0] = 1
    while que:
        x, y = que.pop()
        cost = grid[y][x]
        for i, j in [(0,1),(1,0),(-1,0),(0,-1)]:
            nxt_x, nxt_y = x + i, y + j
            if not (0<=nxt_x<w and 0<=nxt_y<h):
                continue
            elif grid[nxt_y][nxt_x] != '#' and grid[nxt_y][nxt_x] > cost + 1:
                grid[nxt_y][nxt_x] = cost + 1
                que += [(nxt_x, nxt_y)]


    if grid[h-1][w-1] == INF:
        return -1


    return cnt - grid[h-1][w-1]







print(main())