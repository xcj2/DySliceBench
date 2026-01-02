# coding=utf-8
from math import floor, ceil, sqrt, factorial, log, gcd, log10
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement, chain
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heappushpop, heapify
from copy import copy, deepcopy
import sys
INF = float('inf')
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)


def lcm(a, b): return a * b / gcd(a, b)


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
# 1 2 3
# a, b, c = LI()


def I(): return int(sys.stdin.buffer.readline())
# a = I()


def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
# abc def
# a, b = LS()


def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
# a = S()


def IR(n): return [I() for i in range(n)]
# 2
# 1
# 2
# [1, 2]


def LIR(n): return [LI() for i in range(n)]
# 2
# 1 2 3
# 4 5 6
# [[1,2,3], [4,5,6]]


def SR(n): return [S() for i in range(n)]
# 2
# abc
# def
# [abc, def]


def LSR(n): return [LS() for i in range(n)]
# 2
# abc def
# ghi jkl
# [[abc,def], [ghi,jkl]]


def SRL(n): return [list(S()) for i in range(n)]
# 2
# abcd
# efgh
# [[a,b,c,d], [e,f,g,h]]


k = I()
print("ACL"*k)
