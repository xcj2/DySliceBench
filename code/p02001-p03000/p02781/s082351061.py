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


INF = 10 ** 13
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


n = str(I())
K = I()
digit_len = len(n)
dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(digit_len + 1)]
dp[0][0][0] = 1
for i in range(digit_len):
    d = int(n[i])
    for j in range(2):
        for k in range(K + 1):
            for l in range(10 if j else d + 1):
                if k + bool(l) <= K:
                    dp[i + 1][j or (l < d)][k + bool(l)] += dp[i][j][k]



print(dp[digit_len][0][K] + dp[digit_len][1][K])



