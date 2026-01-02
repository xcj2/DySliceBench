#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
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
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007
class SegmentTree:
    def __init__(self, size, f=max, default=0):
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

    def get(self, a, b=None):
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
    n,k = LI()
    a = IR(n)
    m = max(a)
    s = SegmentTree(m+1)
    ans = 1

    for i in a:
        l = max(0,i-k)
        r = min(m+1,i+k+1)
        p = s.get(l,r)+1
        s.update(i,p)
        if ans < p:
            ans = p
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
