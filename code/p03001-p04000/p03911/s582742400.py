from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce


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
mod = 10 ** 9 + 7

class UnionFind:
    def __init__(self, n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
        self.table = [-1] * n
        self.size = [1] * n
        self.group_num = n

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
        self.group_num -= 1



n, m = LI()
lan = [[] for _ in range(m)]
uf = UnionFind(n)
for j in range(n):
    L = LI()
    k = L[0]
    for i in range(1, k + 1):
        lan[L[i] - 1] += [j]


for ll in lan:
    for s in range(len(ll)):
        uf.union(ll[s], ll[s - 1])

if uf.group_num == 1:
    print('YES')
else:
    print('NO')
