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
    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while 1:
        w, h = LI()
        if w == h == 0:
            break
        check = defaultdict(lambda: True)
        field = SR(h)
        for i in range(h):
            for k in range(2 * w + 1):
                if field[i][k] == "L":
                    L = [k, i]
                if field[i][k] == "R":
                    R = [k, i]
        state = deque()
        state.append([L, R])
        flg = True
        while state and flg:
            l, r = state.pop()
            lx, ly = l
            rx, ry = r
            for mx, my in move:
                xl = lx + mx
                yl = ly + my
                xr = rx - mx
                yr = ry + my
                if not 0 <= xl < w:
                    xl -= mx
                if not w + 1 <= xr < 2 * w + 1:
                    xr += mx
                if not 0 <= yl < h:
                    yl -= my
                if not 0 <= yr < h:
                    yr -= my
                if field[yl][xl] == "%" and field[yr][xr] == "%":
                    flg = False
                    break
                if field[yl][xl] == "#":
                    yl -= my
                    xl -= mx
                if field[yr][xr] == "#":
                    yr -= my
                    xr += mx
                if check[(xl, xr, yl, yr)] and field[yl][xl] != "%" and field[yr][xr] != "%":
                    check[(xl, xr, yl, yr)] = False
                    state.append([[xl, yl], [xr, yr]])
        if not flg:
            print("Yes")
        else:
            print("No")
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    E()

