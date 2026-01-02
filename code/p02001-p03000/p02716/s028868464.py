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
from operator import mul


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


n = I()
A = LI()
dp = [[defaultdict(lambda:-INF) for _ in range(2)] for _ in range(n + 1)]
dp[0][0][0] = 0
for i in range(n):
    for j in range(2):
        for k, e in dp[i][j].items():
            if i // 2 <= k <= i // 2 + 1:
                dp[i + 1][0][k] = max(dp[i + 1][0][k], e)
            if i // 2 <= k + 1 <= i // 2 + 1 and j == 0:
                dp[i + 1][1][k + 1] = max(dp[i + 1][1][k + 1], e + A[i])

print(max(dp[n][0][n // 2], dp[n][1][n // 2]))