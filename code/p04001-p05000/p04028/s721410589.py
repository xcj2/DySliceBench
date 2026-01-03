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
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


n = I()
s = len(input())
dp = [0] * (n + 2)
dp[0] = 1
for i in range(1, n + 1):
    ndp = [0] * (n + 2)
    for j in range(n + 1):
        if j:
            ndp[j] = (dp[j - 1] * 2 + dp[j + 1]) % mod
        else:
            ndp[j] = (dp[j] + dp[j + 1]) % mod
    dp = ndp


print(dp[s] * pow(pow(2, s, mod), mod - 2, mod) % mod)
