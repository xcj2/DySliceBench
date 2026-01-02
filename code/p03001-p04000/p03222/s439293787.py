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



def fib(n):
    a, b = 1, 1
    fib_list = [1] * n
    for i in range(n - 2):
        a, b = a + b, a
        fib_list[i + 2] = a
    return fib_list



h, w, k = LI()
L = [0] + fib(w + 1)
dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j] * L[j] * L[w - j]) % mod
        if j + 1 < w:
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] * L[j + 1] * L[w - j - 1]) % mod
        dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * L[j + 1] * L[w - j]) % mod



print(dp[-1][k - 1])

