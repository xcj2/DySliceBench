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

def solve():
    def comb(a,b):
        res = 1
        for i in range(b):
            res *= n-i
            res %= mod
            res *= pow(i+1,mod-2,mod)
            res %= mod
        return res
    n,a,b = LI()
    ans = pow(2,n,mod)-1
    ans -= comb(n,a)+comb(n,b)
    ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
