#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
import random
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

def solve():
    def gcd(a,b):
        if a == 0:
            return b
        return gcd(b%a,a)
    n,m = LI()
    a = LI()
    b = [i >> 1 for i in a]
    c = [i&1 for i in b]
    c.sort()
    while 1:
        if c[0] == 1:
            break
        if c[0] == 0 and c[-1] == 1:
            print(0)
            return
        b = [i >> 1 for i in b]
        c = [i&1 for i in b]
        c.sort()
        m >>= 1
    l = b[0]
    for i in b[1:]:
        if l&1 != i&1:
            print(0)
            return
        g = gcd(l,i)
        l = l*i//g
        if l > m:
            print(0)
            return
    L = l
    l = 0
    r = m+1
    while r-l > 1:
        x = (l+r) >> 1
        if (2*x-1)*L <= m:
            l = x
        else:
            r = x
    print(l)
    return

#Solve
if __name__ == "__main__":
    solve()
