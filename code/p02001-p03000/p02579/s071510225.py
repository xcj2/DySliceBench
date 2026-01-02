from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left, bisect_right
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from copy import deepcopy

INF = float('inf')


def LI(): return list(map(int, sys.stdin.readline().split()))


def I(): return int(sys.stdin.readline())


def LS(): return sys.stdin.readline().split()


def S(): return sys.stdin.readline().strip()


def IR(n): return [I() for i in range(n)]


def LIR(n): return [LI() for i in range(n)]


def SR(n): return [S() for i in range(n)]


def LSR(n): return [LS() for i in range(n)]


def SRL(n): return [list(S()) for i in range(n)]


def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]


mod = 10 ** 9 + 7

h, w = LI()
sy, sx = LI()
gy, gx = LI()
sy -= 1
sx -= 1
gy -= 1
gx -= 1
grid = SR(h)
dp = [[INF] * w for _ in range(h)]
q = deque([(sy, sx)])
dp[sy][sx] = 0
while q:
    uy, ux = q.popleft()
    for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ny = uy + i
        nx = ux + j
        if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "." and dp[ny][nx] > dp[uy][ux]:
            dp[ny][nx] = dp[uy][ux]
            q.appendleft((ny,nx))
    for i in range(-2, 3):
        for j in range(-2, 3):
            ny = uy + i
            nx = ux + j
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "." and dp[ny][nx] > dp[uy][ux] + 1:
                dp[ny][nx] = dp[uy][ux] + 1
                q.append((ny, nx))


print(dp[gy][gx] if dp[gy][gx] != INF else -1)
