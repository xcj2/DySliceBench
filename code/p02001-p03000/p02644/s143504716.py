from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce
from operator import mul
from pprint import pprint



sys.setrecursionlimit(2147483647)
INF = 10 ** 20
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
mod = 1000000007

h, w, k = LI()
sy, sx, gy, gx = LI()
cost = [[INF] * w for _ in range(h)]
cost[sy - 1][sx - 1] = 0
grid = SR(h)
q = deque([(sy - 1, sx - 1)])
while q:
    cy, cx = q.popleft()
    for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        for l in range(1, k + 1):
            ny, nx = cy + i * l, cx + j * l
            if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] == "." and cost[ny][nx] >= cost[cy][cx] + 1:
                if cost[ny][nx] == INF:
                    q.append((ny, nx))
                cost[ny][nx] = cost[cy][cx] + 1
            else:
                break


print(cost[gy - 1][gx - 1] if cost[gy - 1][gx - 1] != INF else -1)








