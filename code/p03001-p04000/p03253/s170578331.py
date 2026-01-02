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


n, m = LI()


def mod_comb(n, r, mod=10 ** 9 + 7):
    fact = 1
    for i in range(n - r + 1, n + 1):
        fact = fact * i % mod

    divisor = 1
    for j in range(1, r + 1):
        divisor = divisor * j % mod

    return fact * pow(divisor, mod - 2, mod) % mod


def prime_fac(n):
    table =[]
    i = 2
    while n >= i**2:
    # nのその数自身を除いた素因数は√n以下であることから。
        while n % i == 0:
            table.append(i)
            n //= i
        i += 1
    if n > 1:
        table.append(n)
# 最後に残った、最大の素因数をリストに入れる。
    return table


ans = 1
for k, v in Counter(prime_fac(m)).items():
    ans = ans * mod_comb(v + n - 1, n - 1) % mod



print(ans)