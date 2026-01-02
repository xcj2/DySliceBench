#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
import re
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    s = SR(n)
    a = 0
    b = 0
    ab = 0
    ans = 0
    for si in s:
        if si[0] == "B" and si[-1] == "A":
            ab += 1
        elif si[0] == "B":
            b += 1
        elif si[-1] == "A":
            a += 1
        ans += si.count("AB")
    if ab:
        ans += ab - 1
        ans += (a > 0) + (b > 0)
        a -= a > 0
        b -= b > 0
    ans += min(a, b)
    print(ans)

    return


#main
if __name__ == '__main__':
    solve()
