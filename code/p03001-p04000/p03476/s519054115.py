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
    n = 10**5+1
    p = 2
    f = [1]*(n+1)
    f[0] = 0
    f[1] = 0
    while p <= n:
        while p <= n and not f[p]:
            p += 1
        j = 2*p
        while j <= n:
            f[j] = 0
            j += p
        p += 1
    s = [1 if f[i] and f[(i+1)>>1] and i&1 else 0 for i in range(n+1)]
    for i in range(n):
        s[i+1] += s[i]
    q = I()
    for _ in range(q):
        l,r = LI()
        print(s[r]-s[l-1])
    return

#Solve
if __name__ == "__main__":
    solve()
