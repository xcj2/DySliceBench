from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = float('INF')
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


h, w = LI()
maze = SRL(h)


def solve(sy, sx):
    min_cost = deepcopy(maze)
    min_cost[sy][sx] = 0
    que = deque([(sy, sx)])
    max_c = 0
    while que:
        cy, cx = que.popleft()
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny = cy + i
            nx = cx + j
            if 0 <= ny < h and 0 <= nx < w:
                if min_cost[ny][nx] == '.':
                    min_cost[ny][nx] = min_cost[cy][cx] + 1
                    que += [(ny, nx)]
                    max_c = max(max_c, min_cost[ny][nx])
    return max_c



ans = 0
for y in range(h):
    for x in range(w):
        if maze[y][x] == '#':
            continue
        else:
            max_c = solve(y, x)
            ans = max(max_c, ans)


print(ans)