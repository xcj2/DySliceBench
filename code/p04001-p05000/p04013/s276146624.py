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



n, a = LI()
L = LI()
L = [i - a for i in L]
dp = defaultdict(int)
dp[0] = 1
for i in range(n):
    if L[i] <= 0:
        for j in range(-2500, 2501):
            dp[j] += dp[j - L[i]]
    else:
        for j in range(2500, -2501, -1):
            dp[j] += dp[j - L[i]]


print(dp[0] - 1)