from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd, sqrt
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


n, m = LI()

fac = [1] * (m + 1)
inv = [1] * (m + 1)
for j in range(1, m + 1):
    fac[j] = fac[j-1] * j % mod


inv[m] = pow(fac[m], mod-2, mod)
for j in range(m-1, -1, -1):
    inv[j] = inv[j+1] * (j+1) % mod


def comb(m, r):
    if r > m or m < 0 or r < 0:
        return 0
    return fac[m] * inv[m - r] * inv[r] % mod

ret = 0
for i in range(n + 1):
    c = comb(m, i) * comb(n, i) % mod * fac[i] % mod * pow(comb(m - i, (n - i)) * fac[n - i] % mod, 2, mod) % mod
    if i % 2:
        ret -= c
    else:
        ret += c
    ret %= mod

print(ret)





