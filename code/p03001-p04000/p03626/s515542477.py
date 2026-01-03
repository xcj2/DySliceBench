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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
    s1 = S()
    s2 = S()
    i = 0
    f = 0
    if s1[i] == s2[i]:
        ans = 3
        i += 1
        f = 1
    else:
        ans = 6
        i += 2
    while i < n:
        if s1[i] == s2[i]:
            ans *= 2 if f else 1
            ans %= mod
            i += 1
            f = 1
            continue
        i += 2
        ans *= 2 if f else 3
        f = 0
        ans %= mod
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
