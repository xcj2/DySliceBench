from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
from re import split
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy
import re

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
mod = 10 ** 9 + 7


h, w = LI()
L = SR(h)
dp = [[INF] * w for _ in range(h)]
dp[0][0] = 1 if L[0][0] == '#' else 0
for y in range(h):
    for x in range(w):
        if y:
            if L[y][x] == '.' or L[y - 1][x] == '#':
                dp[y][x] = dp[y - 1][x]
            else:
                dp[y][x] = dp[y - 1][x] + 1
        if x:
            if L[y][x] == '.' or L[y][x - 1] == '#':
                dp[y][x] = min(dp[y][x], dp[y][x - 1])
            else:
                dp[y][x] = min(dp[y][x], dp[y][x - 1] + 1)


print(dp[h - 1][w - 1])