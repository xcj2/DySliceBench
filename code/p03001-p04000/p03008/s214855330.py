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


n = I()
#　最初はaでのやつが価値に当たる。
weight = LI()
value = LI()
dp = list(range(n + 1))
for i in range(3):
    for j in range(weight[i], n + 1):
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])


n = dp[-1]
weight, value = value, weight
dp = list(range(n + 1))
for i in range(3):
    for j in range(weight[i], n + 1):
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

print(dp[-1])



