# coding=utf-8
from math import floor, ceil, sqrt, factorial, log, gcd
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heappushpop, heapify
import copy
import sys
INF = float('inf')
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)


def lcm(a, b): return a * b / gcd(a, b)

# 1 2 3
# a, b, c = LI()


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))

# a = I()


def I(): return int(sys.stdin.buffer.readline())

# abc def
# a, b = LS()


def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

# a = S()


def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')

# 2
# 1
# 2
# [1, 2]


def IR(n): return [I() for i in range(n)]

# 2
# 1 2 3
# 4 5 6
# [[1,2,3], [4,5,6]]


def LIR(n): return [LI() for i in range(n)]

# 2
# abc
# def
# [abc, def]


def SR(n): return [S() for i in range(n)]

# 2
# abc def
# ghi jkl
# [[abc,def], [ghi,jkl]]


def LSR(n): return [LS() for i in range(n)]

# 2
# abcd
# efgh
# [[a,b,c,d], [e,f,g,h]]


def SRL(n): return [list(S()) for i in range(n)]


# n, k = LI()
# s = set()
# for i in range(k):
#     l, r = LI()
#     s |= set(range(l, r + 1))

# # a = len(s)
# dp = [0] * (n + 1)
# dp[1] = 1

# for i in range(1, n+1):
#     for j in range(1, i):
#         if i-j in s:
#             dp[i] += dp[j] % 998244353
#             # dp[i] += dp[j]
# print(dp[n] % 998244353)

# 配るDP
n, k = map(int, input().split())
lr = []
for _ in range(k):
    l, r = map(int, input().split())
    lr.append((l, r))
mod = 998244353
dp = [0]*(2*n+1)
dp[0] = 1
dp[1] = -1
now = 1
for i in range(n-1):
    for l, r in lr:
        # 始点に足して終点は引く
        # imos法というらしい
        dp[i+l] += now
        dp[i+r+1] -= now
    now += dp[i+1]
    now %= mod
print(now)
