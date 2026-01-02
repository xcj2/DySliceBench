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
    n,p,q = LI()
    c = IR(n)
    cp = [c[i]+p*i for i in range(n)]
    cp.sort(reverse=True)
    ans = 0
    s = 0
    for i in range(n):
        s += cp[i]
        ns = s+p*(i+1)*(i+2-(q+2*n))
        if ans < ns:
            ans = ns
    print(ans+p*(n*q+(n*(n-1))//2))
    return

#Solve
if __name__ == "__main__":
    solve()

