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
    x = II()
    if x < 1200:
        print("ABC")
    else:
        print("ARC")
    return

#B
def B():
    s = S()
    a = inf
    z = 0
    for num,si in enumerate(s):
        if si == "A":
            a = min(a, num)
        if si == "Z":
            z = max(z, num)
    print(z-a+1)
    return

#C
def C():
    x = II()
    print(x // 11 * 2 + (x % 11) // 7 + (x % 11 != 0))
    return

#D
def D():
    n = II()
    x = LI()
    print(len(set(x)) - (n - len(set(x))) % 2)
    return

#Solve
if __name__ == '__main__':
    D()
