#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

class SegmentTree:
    def __init__(self, size, default, op=max):
        self.size = 2**size.bit_length()
        self.dat = [default]*(self.size*2)
        self.op = op

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.op(self.dat[i*2], self.dat[i*2+1])

    def add(self, i, x):
        i += self.size
        self.dat[i] = self.op(self.dat[i], x)
        while i > 0:
            i >>= 1
            self.dat[i] = self.op(self.dat[i], x)

    def get(self, a, b=None):
        if b is None:
            b = a + 1
        l, r = a + self.size, b + self.size
        res = None
        while l < r:
            if l & 1:
                if res is None:
                    res = self.dat[l]
                else:
                    res = self.op(res, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                if res is None:
                    res = self.dat[r]
                else:
                    res = self.op(res, self.dat[r])
            l >>= 1
            r >>= 1
        return res

#solve
def solve():
    n = II()
    h = LI()
    a = LI()
    dp = SegmentTree(n + 1, 0)
    for i in range(n):
        hi, ai = h[i], a[i]
        ma = dp.get(0, hi)
        dp.update(hi, ma + ai)
    print(dp.get(0, n + 1))
    return


#main
if __name__ == '__main__':
    solve()
