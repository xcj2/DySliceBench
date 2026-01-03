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
mod = 1000000007


n, a_ratio, b_ratio = LI()
L = LIR(n)
A, B, cost = [[L[i][j] for i in range(n)] for j in range(3)]
dp = [[INF] * 401 for _ in range(401)]
dp[0][0] = 0
for i in range(n):
    for j in range(401, -1, -1):
        for k in range(401, -1, -1):
            if 0 <= j + A[i] <= 400 and 0 <= k + B[i] <= 400:
                dp[j + A[i]][k + B[i]] = min(dp[j + A[i]][k + B[i]], dp[j][k] + cost[i])



ans = INF
for l in range(1, min(400 // b_ratio, 400 // a_ratio)):
    ans = min(ans, dp[a_ratio * l][b_ratio * l])


if ans == INF:
    print(-1)
else:
    print(ans)
