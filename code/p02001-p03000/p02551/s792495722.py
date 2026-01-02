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
from math import log2, ceil


class SegmentTree:
    def __init__(self, n, default):
        self.n = n
        tn = 2 ** ceil(log2(n))
        self.a = [default] * (tn * 2)
        self.tn = tn

    def find(self, s, t):
        return self.__find(1, 0, self.tn - 1, s, t)

    def __find(self, c, l, r, s, t):
        if self.a[c] == -1:
            return self.a[c // 2]
        if s <= l and r <= t:
            return self.a[c]
        mid = (l + r) // 2
        if t <= mid:
            return self.__find(c * 2, l, mid, s, t)
        elif s > mid:
            return self.__find(c * 2 + 1, mid + 1, r, s, t)
        else:
            return min(
                self.__find(c * 2, l, mid, s, mid),
                self.__find(c * 2 + 1, mid + 1, r, mid + 1, t))

    def update(self, s, t, x):
        self.__update(1, 0, self.tn - 1, s, t, x)

    def __update(self, c, l, r, s, t, x, f=None):

        if f is None and self.a[c] == -1:
            f = self.a[c // 2]

        if l == s and r == t:
            return self.__set(c, x)

        mid = (l + r) // 2
        if t <= mid:
            rv, f = self.__get_child(c, c * 2 + 1, f)
            u = min(self.__update(c * 2, l, mid, s, t, x, f), rv)
        elif s > mid:
            lv, f = self.__get_child(c, c * 2, f)
            u = min(lv, self.__update(c * 2 + 1, mid + 1, r, s, t, x, f))
        else:
            u = min(
                self.__update(c * 2, l, mid, s, mid, x, f),
                self.__update(c * 2 + 1, mid + 1, r, mid + 1, t, x, f))
            if f is not None:
                u = min(f, u)
        self.a[c] = u

        return u

    def __set(self, c, x):
        self.a[c] = x
        if c < self.tn:
            self.a[c * 2] = self.a[c * 2 + 1] = -1
        return x

    def __get_child(self, c, child, f):
        if f is not None:
            return self.__set(child, f), f
        v = self.a[child]
        if v == -1:
            f = self.a[c]
            v = self.__set(child, f)
        return v, f

def solve():
    n,q = LI()
    ans = (n-2)*(n-2)
    right = SegmentTree(n+1,n)
    down = SegmentTree(n+1,n)
    for _ in range(q):
        t,x = LI()
        if t == 1:
            d = down.find(x,x)
            ans -= d-2
            k = right.find(0,0)
            if k > x:
                right.update(0,d,x)
        else:
            r = right.find(x,x)
            ans -= r-2
            k = down.find(0,0)
            if k > x:
                down.update(0,r,x)
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
