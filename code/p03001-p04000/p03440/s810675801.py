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
A = [(a, i) for i, a in enumerate(LI())]
heapify(A)
uf = UnionFind(n)
for x, y in LIR(m):
    uf.union(x, y)

k = uf.group_num
if (k - 1) * 2 > n:
    print('Impossible')
else:
    ans = 0
    ret = 0
    ret2 = 0
    D = defaultdict(int)
    while ret + ret2 < (k - 1) * 2:
        a, i = heappop(A)
        r = uf.root(i)
        if not D[r]:
            D[r] = 1
            ret += 1
            ans += a
        else:
            if ret2 < (k - 1) * 2 - k:
                ret2 += 1
                ans += a
    print(ans)

