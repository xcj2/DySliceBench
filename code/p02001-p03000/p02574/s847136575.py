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
        return gcd(b%a, a)
    N = 1000001
    f = [1]*N
    lis = []
    p = 2
    while p < N:
        while p < N and not f[p]:
            p += 1
        j = p
        lis.append(p)
        while j < N:
            f[j] = 0
            j += p
    def func(n):
        i = 0
        p = lis[i]
        if n < 2:
            return 0
        while p*p <= n:
            if n%p == 0:
                if c[p]:
                    return 1
                c[p] = 1
                while n%p == 0:
                    n //= p
            i += 1
            p = lis[i]
        if c[n]:
            return 1
        if n > 1:
            c[n] = 1
        return 0
    n = I()
    a = LI()
    g = a[0]
    for i in a[1:]:
        g = gcd(g,i)
    if g != 1:
        print("not coprime")
        return
    c = [0]*N
    for i in a:
        if func(i):
            print("setwise coprime")
            return
    print("pairwise coprime")
    return

#Solve
if __name__ == "__main__":
    solve()
