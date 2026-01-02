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
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): pass
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


n = I()
dp = [[0] * 3 for _ in range(n)]
for i in range(n):
    a, b, c = LI()
    if i:
        dp[i][0] = max(dp[i - 1][1] + a, dp[i - 1][2] + a)
        dp[i][1] = max(dp[i - 1][0] + b, dp[i - 1][2] + b)
        dp[i][2] = max(dp[i - 1][0] + c, dp[i - 1][1] + c)
    else:
        dp[0] = a, b, c

print(max(dp[-1]))