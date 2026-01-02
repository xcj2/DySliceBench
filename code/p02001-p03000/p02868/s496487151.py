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


class SegmentTree:
    def __init__(self, n, ide_ele, op, init_val=[]):
        self.n = 2 ** (n - 1).bit_length()
        self.ide_ele = ide_ele
        self.op = op
        self.seg = [ide_ele] * 2 * self.n
        if init_val:
            for i in range(n):
                self.seg[i + self.n - 1] = init_val[i]
            for i in range(self.n - 2, -1, -1):
                self.seg[i] = self.op(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.n - 1
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.op(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, p, q):
        # qは含まない
        if q <= p:
            return self.ide_ele
        p += self.n - 1
        q += self.n - 2
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

    def display(self):
        return self.seg[self.n - 1: -1]
    
    def query_point(self, p):
        return self.seg[p + self.n - 1]


n, m = LI()
lrc_list = sorted(LIR(m))
st = SegmentTree(n, INF, min)
st.update(0, 0)
for l, r, c in lrc_list:
    l_dist = st.query(l - 1, r)
    st.update(r - 1, min(st.query_point(r - 1), l_dist + c))
    # dis = st.display()

if st.query_point(n - 1) == INF:
    print(-1)
else:
    print(st.query_point(n - 1))




