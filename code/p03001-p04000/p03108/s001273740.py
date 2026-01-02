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


class UnionFind:
    def __init__(self, n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
        self.table = [-1] * n
        self.size = [1] * n

    def root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.root(self.table[x])
            return self.table[x]


    def get_size(self, x):
        r = self.root(x)
        return self.size[r]


    def is_same(self, x, y):
        if self.root(x) == self.root(y):
            return True
        else:
            return False

    def union(self, x, y):
        r1 = self.root(x)
        r2 = self.root(y)
        if r1 == r2:
            return
        # ランクの取得
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.size[r1] += self.size[r2]
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2
            self.size[r2] += self.size[r1]


def comb(n, r):
    if r > n:
        return 0
    fact = 1
    for i in range(n-r+1, n+1):
        fact = fact * i
    divisor = 1
    for j in range(1, r+1):
        divisor = divisor * j
    return fact//divisor



n, m = LI()
U = UnionFind(n)
ret = 0
L = LIR(m)
ans = [0] * m
ans[m - 1] = comb(n, 2)
for i in range(m - 1, 0, -1):
    u, v = L[i]
    ans[i - 1] = ans[i]
    if not U.is_same(u - 1, v - 1):
        ans[i - 1] -= U.get_size(u - 1) * U.get_size(v - 1)
        U.union(u - 1, v - 1)



for i in ans:
    print(i)