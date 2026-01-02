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
from operator import mul


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
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
        # self.group_num = n

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
        return self.root(x) == self.root(y)

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
        # self.group_num -= 1

n, m, k = LI()
U = UnionFind(n)
G1 = [[] for _ in range(n)]
for _ in range(m):
    a, b = LI()
    G1[a - 1] += [b - 1]
    G1[b - 1] += [a - 1]
    U.union(a - 1, b - 1)

G2 = [[] for _ in range(n)]
for _ in range(k):
    c, d = LI()
    G2[c - 1] += [d - 1]
    G2[d - 1] += [c - 1]

for i in range(n):
    ret = U.get_size(i) - 1 - len(G1[i])
    for j in G2[i]:
        if U.is_same(i, j):
            ret -= 1
    print(ret, end=" ")