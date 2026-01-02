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
    n, i = LI()
    print(n-i+1)
    return

#B
def B():
    h, w = LI()
    a = SR(h)
    dy = defaultdict(int)
    dx = defaultdict(int)
    for y in range(h):
        for x in range(w):
            if a[y][x] == "#":
                dx[x] = 1
                dy[y] = 1
    dy = list(sorted(dy.items(), key=lambda x: x[0]))
    dx = list(sorted(dx.items(), key=lambda x: x[0]))
    for y,_ in dy:
        for x,_ in dx:
            print(a[y][x], end="")
        print()


    return

#C
def C():
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    B()
