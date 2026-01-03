from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left, bisect_right
import random
from itertools import permutations, accumulate, combinations
import sys
import string



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
mod = 10 ** 9 + 7


n  = bin(I())[2:]
dp0, dp1, dp2 = 1, 0, 0
for d in n:
    if d == '1':
        dp0, dp1, dp2 = dp0 % mod, (dp0 + dp1) % mod, (dp1 * 2 + dp2 * 3) % mod
    else:
        dp0, dp1, dp2 = (dp0 + dp1) % mod, dp1 % mod, (dp1 + dp2 * 3) % mod



print((dp0 + dp1 + dp2) % mod)

