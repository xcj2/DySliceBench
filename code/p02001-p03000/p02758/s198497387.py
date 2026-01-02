#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 998244353
import operator
class SegmentTree:
    def __init__(self, size, default, f = operator.add):
        self.size = 2**(size-1).bit_length()
        self.default = default
        self.dat = [default]*(self.size*2)
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def add(self, i, x):
        i += self.size
        self.dat[i] = self.f(self.dat[i], x)
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i], x)

    def get(self, a, b = None):
        if b is None:
            b = a + 1
        l, r = a + self.size, b + self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres)
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res
def solve():
    n = I()
    a = LIR(n)
    a.sort()
    ans = [None]*(n+1)
    s = SegmentTree(n,0,max)
    ans[n] = 1
    X = [i[0] for i in a]
    for i in range(n)[::-1]:
        x,d = a[i]
        k = x+d
        j = bisect.bisect_left(X,k)
        b = s.get(i,j)
        if j < b:
            j = b
        s.update(i,j)
        ans[i] = ans[j]+ans[i+1]
        ans[i] %= mod
    print(ans[0])
    return

#Solve
if __name__ == "__main__":
    solve()
