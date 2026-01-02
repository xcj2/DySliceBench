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
inf = float("INF")

#solve
def solve():
    n = II()
    s = SR(n)
    m = []
    x = []
    for si in s:
        l = 0 # )
        r = 0 # (
        for i in si:
            if i == ")":
                if r:
                    r -= 1
                else:
                    l += 1
            elif i == "(":
                r += 1
        if r > l:
            m.append((l, r))
        else:
            x.append((r, l))
    m.sort()
    x.sort(reverse=True)
    tmp = 0
    for l, r in m:
        if tmp - l < 0:
            print("No")
            return
        else:
            tmp -= l
            tmp += r
    for r, l in x:
        if tmp - l < 0:
            print("No")
            return
        else:
            tmp -= l
            tmp += r
    if tmp == 0:
        print("Yes")
    else:
        print("No")
    return


#main
if __name__ == '__main__':
    solve()
