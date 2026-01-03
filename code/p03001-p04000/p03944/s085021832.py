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
    a, b, c = LI()
    if a == b + c:
        print("Yes")
    elif b == a + c:
        print("Yes")
    elif c == a + b:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    W, H, n = LI()
    wh = [[0, W], [0, H]]
    for _ in range(n):
        x, y, a = LI()
        wha = wh[a > 2]
        x = y if a > 2 else x
        wha[0] = max(x, wha[0]) * (a % 2) or wha[0]
        wha[1] = wha[1] * (a % 2) or min(x, wha[1])
        if wha[0] >= wha[1]:
            print(0)
            return
    print(max(0, (wh[0][1] - wh[0][0]) * (wh[1][1] - wh[1][0])))
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
