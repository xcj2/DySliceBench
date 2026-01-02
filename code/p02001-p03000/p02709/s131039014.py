from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 9
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

n = I()
A = LI()
S = sorted([(A[k], k + 1) for k in range(n)], reverse=True)
ans = 0
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        if i and i <= S[i + j - 1][1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + S[i + j - 1][0] * abs(i - S[i + j - 1][1]))
        if j and S[i + j - 1][1] <= n - j + 1:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + S[i + j - 1][0] * abs(n - j + 1 - S[i + j - 1][1]))
        if i + j == n:
            ans = max(ans, dp[i][j])
            break

print(ans)


