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
import pprint
sys.setrecursionlimit(10 ** 9)


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


n, c = LI()
A = LI()
B = LI()

pre_compute = [[0] * 401 for _ in range(401)]
for ii in range(401):
    for jj in range(401):
        pre_compute[ii][jj] = pre_compute[ii - 1][jj]
        pre_compute[ii][jj] += pow(ii, jj, mod)
        pre_compute[ii][jj] %= mod


dp = [[0] * (c + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(c + 1):
        for k in range(j + 1):
            dp[i+1][j] += dp[i][k] * (pre_compute[B[i]][j - k] - pre_compute[A[i] - 1][j - k]) % mod
            # print((pre_compute[j - k][B[i]] - pre_compute[j - k][A[i] - 1]))
            dp[i+1][j] %= mod



print(dp[n][c])




