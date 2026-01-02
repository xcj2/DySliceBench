from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
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


h, w = LI()
A = LIR(h)
B = LIR(h)
dp = [[0] * w for _ in range(h)]
m = 80 * 160
dp[0][0] = (1 << m) << abs(A[0][0] - B[0][0])
dp[0][0] |= (1 << m) >> abs(A[0][0] - B[0][0])
for y in range(h):
    for x in range(w):
        if y + 1 < h:
            dp[y + 1][x] |= dp[y][x] << abs(A[y + 1][x] - B[y + 1][x])
            dp[y + 1][x] |= dp[y][x] >> abs(A[y + 1][x] - B[y + 1][x])
        if x + 1 < w:
            dp[y][x + 1] |= dp[y][x] << abs(A[y][x + 1] - B[y][x + 1])
            dp[y][x + 1] |= dp[y][x] >> abs(A[y][x + 1] - B[y][x + 1])


ans = INF
for j in range(m * 2):
    if dp[h - 1][w - 1] >> j & 1:
        ans = min(ans, abs(j - m))


print(ans)



