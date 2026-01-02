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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a




class SegmentTree:
    def __init__(self, init_val, ide_ele, op):
        n = len(init_val)
        self.num = 2 ** (n - 1).bit_length()
        self.seg = [ide_ele] * 2 * self.num
        self.ide_ele = ide_ele
        self.op = op
        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]
            # built
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.op(self.seg[2 * i + 1], self.seg[2 * i + 2])


    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while k + 1:
            k = (k - 1) // 2
            self.seg[k] = self.op(self.seg[k * 2 + 1], self.seg[k * 2 + 2])


    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.op(res, self.seg[p])
            if q & 1 == 1:
                res = self.op(res, self.seg[q])
            p = p // 2
            q = (q - 2) // 2
        if p == q:
            res = self.op(res, self.seg[p])
        else:
            res = self.op(self.seg[p], self.op(res, self.seg[q]))
        return res



n = I()
L = LI()
ST = SegmentTree(L, 0, gcd)
print(max([gcd(ST.query(0, i), ST.query(i + 1, n)) for i in range(n)]))