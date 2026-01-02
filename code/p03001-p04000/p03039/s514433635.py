from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from functools import reduce



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
mod = 1000000007


def mod_combination(n, r, mod=10 ** 9 + 7):
    fact = 1
    for i in range(n - r + 1, n + 1):
        fact = fact * i % mod

    divisor = 1
    for j in range(1, r + 1):
        divisor = divisor * j % mod

    return fact * pow(divisor, mod - 2, mod) % mod


def main():
    mod = 10**9+7
    n, m, k = LI()
    # 　ある配置を固定した時、その2つの配置でmanhattan距離が計算される回数は、他の組み合わせ数。
    combination = mod_combination(n*m-2, k-2)
    x=y=0
    for i in range(1, n):
        x += i * (n-i)
    for j in range(1, m):
        y += j * (m-j)
    return (((m ** 2) % mod * x % mod) + ((n ** 2) % mod * y % mod)) * combination % mod


print(main())