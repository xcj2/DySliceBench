#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    h,w,m = LI()
    fx = [0]*w
    fy = [0]*h
    f = defaultdict(lambda : 0)
    for _ in range(m):
        y,x = LI()
        y -= 1
        x -= 1
        f[(y,x)] = 1
        fx[x] += 1
        fy[y] += 1
    m = 0
    lisx = []
    for x in range(w):
        srx = fx[x]
        if m < srx:
            m = srx
    for x in range(w):
        srx = fx[x]
        if m == srx:
            lisx.append(x)
    M = 0
    lisy = []
    for y in range(h):
        srx = fy[y]
        if M < srx:
            M = srx
    for y in range(h):
        srx = fy[y]
        if M == srx:
            lisy.append(y)
    ans = m+M
    for y in lisy:
        for x in lisx:
            if not f[(y,x)]:
                print(ans)
                return
    print(ans-1)
    return

#Solve
if __name__ == "__main__":
    solve()
