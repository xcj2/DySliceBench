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
import pprint



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

k = I()
s = S()
l = len(s)
n = k + l + 1
fac = [1] * (n + 1)
inv = [1] * (n + 1)
twentyFive = [1] * (n + 1)
twentySix = [1] * (n + 1)
for j in range(1, n + 1):
    fac[j] = fac[j-1] * j % mod
    twentyFive[j] = twentyFive[j - 1] * 25 % mod
    twentySix[j] = twentySix[j - 1] * 26 % mod


inv[n] = pow(fac[n], mod-2, mod)
for j in range(n-1, -1, -1):
    inv[j] = inv[j+1] * (j+1) % mod


def comb(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return fac[n] * inv[n - r] * inv[r] % mod




ans = 0
for i in range(k + 1):
    ans += comb(l - 1 + i, i) * twentyFive[i] % mod * twentySix[k - i] % mod
    ans %= mod

print(ans)

