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
    n,A,B = LI()
    G = LIR(n)
    n1 = n>>1
    n2 = n-n1
    s1 = defaultdict(lambda : float("inf"))
    s2 = defaultdict(lambda : float("inf"))
    for j in range(1<<n1):
        sa = 0
        sb = 0
        sc = 0
        for i in range(n1):
            if j&(1<<i):
                a,b,c = G[i]
                sa += a
                sb += b
                sc += c
        if s1[(sa,sb)] > sc:
            s1[(sa,sb)] = sc
    m = 1
    for j in range(1<<n2):
        sa = 0
        sb = 0
        sc = 0
        for i in range(n2):
            if j&(1<<i):
                a,b,c = G[i+n1]
                sa += a
                sb += b
                sc += c
        if sa > m:
            m = sa
        if s2[(sa,sb)] > sc:
            s2[(sa,sb)] = sc
    ans = float("inf")
    for (a,b),c in s1.items():
        for i in range(m+1):
            s = B*(i+a)
            if s%A:
                continue
            j = (s//A)-b
            nc = s2[(i,j)]
            cost = c+nc
            if a == b == i == j:
                continue
            if cost < ans:
                ans = cost
    if ans == float("inf"):
        print(-1)
        return
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
