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
inf = float('INF')

#solve
def solve():
    h, w = LI()
    a = LIR(h)
    b = LIR(h)
    mab = [[abs(a[y][x]-b[y][x]) for x in range(w)] for y in range(h)]
    ab = abs(a[0][0] - b[0][0])
    hw = h + w
    dp = [[0] * w for i in range(h)]
    dp[0][0] |= (1 << (6400 + ab) | 1 << (6400 - ab))
    for i in range(1, h + w - 1):
        for x in range(w):
            y = i - x - 1
            if 0 <= x < w and 0 <= y < h:
                value = dp[y][x]
            else:
                continue
            for mx, my in [[0, 1], [1, 0]]:
                mx += x
                my += y
                if 0 <= mx < w and 0 <= my < h:
                    mxy = mab[my][mx]
                    dp[my][mx] |= ((value << mxy) | (value >> mxy))
    ans = dp[-1][-1]
    for i in range(ans.bit_length()):
        if ans & (1 << (6400-i)):
            print(i)
            return
    return


#main
if __name__ == '__main__':
    solve()
