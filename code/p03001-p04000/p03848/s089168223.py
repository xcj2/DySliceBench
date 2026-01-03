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
    n = I()
    a = LI()
    a.sort()
    if n&1:
        n >>= 1
        if a != sorted([2*i for i in range(n+1)]+[2*i for i in range(1,n+1)]):
            print(0)
        else:
            print(pow(2,n,mod))
    else:
        n >>= 1
        if a != sorted([2*i+1 for i in range(n)]+[2*i+1 for i in range(n)]):
            print(0)
        else:
            print(pow(2,n,mod))
    return

#Solve
if __name__ == "__main__":
    solve()
