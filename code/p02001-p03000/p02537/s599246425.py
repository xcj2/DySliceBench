from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from math import gcd
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]

mod=10**9+7

class Segtree:
    def __init__(self, A, ide_ele, segfunc):
        self.n = len(A)
        self.size = 2 ** (self.n - 1).bit_length()
        self.ide_ele = ide_ele
        self.segfunc = segfunc
        self.data = [ide_ele] * self.size + A + [ide_ele] * (self.size - self.n)
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def update(self, k, x):
        k += self.size
        self.data[k] = max(x, self.data[k])
        while k:
            k = k >> 1
            self.data[k] = self.segfunc(self.data[2 * k], self.data[2 * k + 1])

    def query(self, l, r):
        L, R = l + self.size, r + self.size
        s = self.ide_ele
        while L < R:
            if R & 1:
                R -= 1
                s = self.segfunc(s, self.data[R])
            if L & 1:
                s = self.segfunc(s, self.data[L])
                L += 1
            L >>= 1
            R >>= 1
        return s

n,k=LI()
seg=Segtree([0]*300010, -INF, max)
for _ in range(n):
    v=I()
    m=seg.query(max(v-k,0),min(300001,v+k+1))+1
    seg.update(v,m)

print(seg.query(0,300002))

