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
    def f(a):
        b = [0]*(n+1)
        for i in range(n):
            l = max(0,i-a[i])
            r = min(n,i+a[i]+1)
            b[l] += 1
            b[r] -= 1
        for i in range(n):
            b[i+1] += b[i]
        return b[:n]
    n,k = LI()
    a = LI()
    while k:
        if sum(a) == n**2:
            break
        a = f(a)
        k -= 1
    print(*a)
    return

#Solve
if __name__ == "__main__":
    solve()
