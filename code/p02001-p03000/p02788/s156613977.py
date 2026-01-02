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
mod = 1000000007

import operator
class SegmentTree:
    def __init__(self, size, default, op = operator.add):
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

    def get(self, a, b = None):
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

def solve():

    n,d,a = LI()
    p = LIR(n)
    ans = 0
    p.sort()
    X = [p[i][0] for i in range(n)]
    s = SegmentTree(n,0)
    for i in range(n):
        x,h = p[i]
        j = bisect.bisect_left(X,x-2*d)
        if i != j:
            su = s.get(j,i)
            h -=  s.get(j,i)
        if h > 0:
            l = x
            k = math.ceil(h/a)
            ans += k
            s.update(i,k*a)
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
