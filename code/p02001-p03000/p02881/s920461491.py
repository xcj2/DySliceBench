#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
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
    def f(n):
        if n < 4:
            return [1,n]
        res = [1]
        i = 2
        while i*i <= n:
            if n%i == 0:
                res.append(i)
                m = n//i
                if m != i:
                    res.append(m)
            i += 1
        res.append(n)
        return res

    n = I()
    l = f(n)
    ans = float("inf")
    for x in l:
        m = x+n//x-2
        if m < ans:
            ans = m
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
