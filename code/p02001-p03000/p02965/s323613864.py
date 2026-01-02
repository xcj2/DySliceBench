from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 15
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
mod = 998244353

n, m = LI()
a = n + 3 * m
fac = [1] * (a + 1)
inv = [1] * (a + 1)
for j in range(1, a + 1):
    fac[j] = fac[j-1] * j % mod

inv[a] = pow(fac[a], mod-2, mod)
for j in range(a-1, -1, -1):
    inv[j] = inv[j+1] * (j+1) % mod

def comb(x, y):
    if y > x or x < 0 or y < 0:
        return 0
    return fac[x] * inv[x - y] * inv[y] % mod

ans = 0
for i in range(min(m + 1, n + 1)):
    if (m - i) % 2:
        continue
    ans += comb(n, i) * comb((m * 3 - i) // 2 + n - 1, n - 1)
    ans %= mod

print((ans - n * comb(m - 1 + n - 1, n - 1)) % mod)