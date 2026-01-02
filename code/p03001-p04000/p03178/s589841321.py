from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce
from operator import mul
from pprint import pprint



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


def digit_dp(n, f):
    dp = [[[0] * f for _ in range(2)] for _ in range(10002)]
    dp[0][0][0] = 1
    l = len(n)
    for i in range(l):
        max_d = int(n[i])
        for j in range(2):
            for ki in range(f):
                for di in range(10 if j else max_d + 1):
                    dp[i + 1][j or (di < max_d)][(ki + di) % f] += dp[i][j][ki]
                    dp[i + 1][j or (di < max_d)][(ki + di) % f] %= mod
    return dp[l][0][0] + dp[l][1][0] - 1


k = input()
d = int(input())
print(digit_dp(k, d) % mod)
