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

    def unite(self, x, y):
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



def z_algorithm(S):
    l = len(S)
    A = [0] * l
    i = 1; j = 0
    while i < l:
        while i + j < l and S[j] == S[i + j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l - i > k < j - A[k]:
            A[i + k] = A[k]
            k += 1
        i += k; j -= k
    return A



s = S()
t = S()
s_len= len(s)
t_len = len(t)
if s_len < t_len:
    s *= (t_len // s_len + 1)
s *= 2


A = z_algorithm(t + '?' + s)[t_len + 1: ]
graph = [[] for _ in range(s_len)]
U = UnionFind(s_len)

flag = False
for i in range(s_len):
    if A[i] == t_len:
        if U.is_same(i, (i + t_len) % s_len):
            flag = True
            break
        U.unite(i, (i + t_len) % s_len)


if flag:
    print(-1)
else:
    print(max(U.size) - 1)