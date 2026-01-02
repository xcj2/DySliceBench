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
def LS(): return list(map(str, stdin.readline().split()))
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
    n, a = IR(2)
    n %= 500
    if a >= n:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    _ = II()
    a = LI()
    a.sort(reverse=True)
    op = 0
    ans = 0
    for ai in a:
        ans += -ai * op or ai
        op ^= 1
    print(ans)
    return

#C
def C():
    c = LIR(3)
    for x in range(c[0][0] + 1):
        b = (c[0][0] - x, c[0][1] - x, c[0][2] - x)
        if (c[1][0] - b[0]) == (c[1][1] - b[1]) == (c[1][2] - b[2]):
            if (c[2][0] - b[0]) == (c[2][1] - b[1]) == (c[2][2] - b[2]):
                print("Yes")
                return
    print("No")
    return
#D
def D():
    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    h, w = LI()
    s = SR(h)
    q = deque([(0, 0, 1)])
    ans = h * w
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                ans -= 1
    check = [[True] * w for _ in range(h)]
    while q:
        x, y, tern = q.pop()
        for mx, my in move:
            mx += x
            my += y
            if 0 <= mx < w and 0 <= my < h:
                if s[my][mx] == "." and check[my][mx]:
                    check[my][mx] = False
                    if my == h - 1 and mx == w - 1:
                        print(ans - tern - 1)
                        return
                    q.appendleft((mx, my, tern + 1))
    print(-1)


    return

#Solve
if __name__ == '__main__':
    D()
