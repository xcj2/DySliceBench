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
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 18
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


def main():
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

        def is_same(self, x, y):
            return self.root(x) == self.root(y)

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


    n = I()
    A = LI()
    B = LI()
    a_sort = sorted([(a, i) for i, a in enumerate(A)])
    b_sort = sorted([(b, i) for i, b in enumerate(B)])
    U = UnionFind(n)
    for i in range(n):
        if a_sort[i][0] > b_sort[i][0]:
            return 'No'
    for j in range(n):
        if j != 0 and a_sort[j][0] <= b_sort[j - 1][0]:
            return 'Yes'
    b_ind_to_a_ind = {}
    for i in range(n):
        b_ind_to_a_ind[b_sort[i][1]] = a_sort[i][1]
    for j in range(n):
        U.union(j, b_ind_to_a_ind[j])
    if U.group_num == 1:
        return 'No'
    else:
        return 'Yes'



print(main())

