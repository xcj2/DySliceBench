#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
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
    if n == 2:
        print(1)
        return
    if n == 3:
        print(2)
        return
    ans = 0
    for i in range(2, int(sqrt(n)) + 1):
        m = n
        if m % i == 0:
            while m % i == 0:
                m //= i
            if m % i == 1:
                ans += 1
    m = n - 1
    l = []
    for i in range(2, int(sqrt(m)) + 1):
        t = 0
        while m % i == 0:
            m //= i
            t += 1
        if t:
            l.append(t)
    if m != 1:
        l.append(1)
    tmp = 1
    for li in l:
        tmp *= (li + 1)
    print(ans+tmp)

    return


#main
if __name__ == '__main__':
    solve()
