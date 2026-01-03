#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a = input()
    print(" ".join(a.split(",")))
    return

#B
def B():
    k, s = LI()
    ans = 0
    for i in range(k + 1):
        for j in range(k + 1):
            if 0 <= s - (i + j) <= k:
                ans += 1
    print(ans)
    return

#C
def C():
    sx, sy, tx, ty = LI()
    UD = ("U", "D")
    LR = ("R", "L")
    ans = UD[sy > ty] * (abs(sy - ty)) + LR[sx > tx] * (abs(sx - tx))
    ans += UD[ty > sy] * (abs(sy - ty)) + LR[tx > sx] * (abs(sx - tx))
    ans += LR[tx > sx] + UD[sy > ty] * (abs(sy - ty) + 1) + LR[sx > tx] * (abs(sx - tx) + 1) + UD[ty > sy]
    ans += LR[sx > tx] + UD[ty > sy] * (abs(sy - ty) + 1) + LR[tx > sx] * (abs(sx - tx) + 1) + UD[sy > ty]
    print(ans)
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
