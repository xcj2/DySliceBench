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
    N = 200000
    f = [1]*N
    p = 2
    prime = []
    while p < N:
        while p < N and not f[p]:
            p += 1
        if p >= N:
            break
        j = 2*p
        prime.append(p)
        while j < N:
            f[j] = 0
            j += p
        p += 1
    x = I()
    print(prime[bisect.bisect_left(prime,x)])
    return

#Solve
if __name__ == "__main__":
    solve()
