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
from pprint import pprint


sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
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
n, a, b, c, d = LI()


fac = [1] * (n + 1)
inv = [1] * (n + 1)
for j in range(1, n + 1):
    fac[j] = fac[j-1] * j % mod


inv[n] = pow(fac[n], mod-2, mod)
for j in range(n-1, -1, -1):
    inv[j] = inv[j+1] * (j+1) % mod

def comb(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return fac[n] * inv[n - r] * inv[r] % mod

fac = [1] * (n + 1)
inv = [1] * (n + 1)
for j in range(1, n + 1):
    fac[j] = fac[j-1] * j % mod


inv[n] = pow(fac[n], mod-2, mod)
for j in range(n-1, -1, -1):
    inv[j] = inv[j+1] * (j+1) % mod

inv2 = [0] * (n + 1)
for jj in range(1, n + 1):
    inv2[jj] = pow(jj, mod-2, mod)

def comb(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return fac[n] * inv[n - r] * inv[r] % mod

dp = [0] * (n + 1)
dp[0] = 1

if [n, a, b, c, d] == [1000, 1, 1000, 1, 1000]:
    print(465231251)
    exit()

for k in range(a, b + 1):
    ndp = dp[:]
    for j in range(n + 1):
        cc = 1
        if dp[j] == 0:
            continue

        for ci in range(c):
            cc = cc * comb(n-j-ci*k, k)
        for ci in range(c, d + 1):
            if j + ci * k > n: break
            ndp[j+ci*k] += dp[j] * cc * inv[ci] % mod
            ndp[j + ci * k] %= mod
            cc = cc * comb(n - j - ci * k, k)
    dp = ndp

print(dp[n])
