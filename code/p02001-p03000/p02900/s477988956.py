#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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

def solve():
    def f(n):
        res = set([1])
        i = 2
        m = n
        while i**2 <= n:
            while m%i == 0:
                res.add(i)
                m //= i
            i += 1
        res.add(m)
        return res

    a,b = LI()
    fa = f(a)
    fb = f(b)
    l = fa&fb
    print(len(l))
    return

#Solve
if __name__ == "__main__":
    solve()
