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


n, m, q = LI()
L = LIR(m)
query = LIR(q)
dp = [[0] * (n + 1) for _ in range(n + 1)]
for l, r in L:
    dp[l][r] += 1


cumsum = [list(accumulate(l)) for l in dp]
cumsum = list(zip(*[list(accumulate(l)) for l in zip(*cumsum)]))
for l, r in query:
    print(cumsum[r][r] - cumsum[l - 1][r] - cumsum[r][l - 1] + cumsum[l - 1][l - 1])