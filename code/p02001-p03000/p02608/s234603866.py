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
    n = I()
    N = 10000
    f = [0]*(N+1)
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                s = x**2+y**2+z**2+x*y+y*z+z*x
                if s <= N:
                    f[s] += 1
    for i in range(1,n+1):
        print(f[i])
    return

#Solve
if __name__ == "__main__":
    solve()
