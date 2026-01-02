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



s = S()
d = len(s)
dp = [[0] * 13 for _ in range(d + 1)]
dp[0][0] = 1
for i in range(d):
    for j in range(13):
        if s[i] != '?':
            dp[i + 1][(j * 10 + int(s[i])) % 13] = (dp[i + 1][(j * 10 + int(s[i])) % 13] + dp[i][j]) % mod
        else:
            for k in range(10):
                dp[i + 1][(j * 10 + k) % 13] = (dp[i + 1][(j * 10 + k) % 13] + dp[i][j]) % mod


print(dp[d][5])