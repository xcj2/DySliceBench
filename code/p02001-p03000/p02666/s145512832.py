from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import ceil, floor, cos, radians, pi, sin
from operator import mul
from functools import reduce
from operator import mul
from functools import lru_cache

mod = 10 ** 9 + 7
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


@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    else:
        return (n*factorial(n-1)) % mod


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


n = I()
P = LI()

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


U = UnionFind(n)
for i in range(n):
    if P[i] != -1:
        U.union(P[i] - 1, i)

k = 0
L = []
for j in range(n):
    if P[j] == -1:
        L += [U.size(j)]
        k += 1

dp = [0]*(k+1)
dp[0] = 1
dp_new = dp[:]
for i in range(1, k+1):
    for j in range(i):
        dp_new[j+1] += dp[j]*L[i-1]
    dp = dp_new[:]


if k:
    dp[1] = sum(L) - len(L)

cycle_count = 0
for i in range(1, k + 1):
    # i個のグループからなるサイクルがひとつできる
    buf = dp[i] * factorial(i - 1)
    buf %= mod
    buf *= pow(n - 1, k - i, mod)
    buf %= mod
    cycle_count += buf


# すでに固定サイクルがあれば数える
cycle_count += (U.group_count() - k) * pow(n - 1, k, mod)
ans = n * pow(n - 1, k, mod)
ans %= mod
ans = ans - cycle_count
ans %= mod
print(ans)