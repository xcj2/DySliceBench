from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy

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
mod = 998244353


n, s = LI()
A = LI()
dp = [[0] * (s + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(1, s + 1):
        if j == A[i]:
            dp[i + 1][j] += i + 1
        elif j > A[i]:
            dp[i + 1][j] += dp[i][j - A[i]]
        if j == s:
            dp[i + 1][j] = dp[i + 1][j] * (n - i) % mod
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= mod


print(dp[n][s])
