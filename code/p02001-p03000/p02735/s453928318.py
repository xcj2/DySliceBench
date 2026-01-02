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
inf = float("INF")

#solve
def solve():
    h,w = LI()
    s = SR(h)
    b = [[inf] * w for i in range(h)]
    q = [(s[0][0] == "#", (0, 0))]
    b[0][0] = s[0][0] == "#"
    while q:
        p, xy = heappop(q)
        y, x = xy
        z = s[y][x]
        for mx, my in [(0, 1), (1, 0)]:
            mx += x
            my += y
            if 0 <= mx < w and 0 <= my < h:
                if b[my][mx] > p + (z != s[my][mx] and s[my][mx] != "."):
                    b[my][mx] = p + (z != s[my][mx] and s[my][mx] != ".")
                    heappush(q, (p + (z != s[my][mx] and s[my][mx] != "."), (my, mx)))

    print(b[-1][-1] if b[-1][-1] else 0)

    return


#main
if __name__ == '__main__':
    solve()
