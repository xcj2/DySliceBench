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
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


h, w = LI()
s = [input() for _ in range(h)]
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue
        if i and s[i-1][j] == ".":
            dp[i][j] += dp[i-1][j]
        if j and s[i][j-1] == ".":
            dp[i][j] += dp[i][j-1]
        dp[i][j] %=mod

print(dp[h-1][w-1])