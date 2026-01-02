#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
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
    h,w = LI()
    a = LIR(h)
    b = LIR(h)
    for i in range(h):
        for j in range(w):
            a[i][j] -= b[i][j]
            if a[i][j] < 0:
                a[i][j] *= -1
    d = [(0,1),(1,0)]
    f = [0 for x in range(w)]
    M = (1<<25600)-1
    b = 12800
    f[0] = (1<<(b+a[0][0]))|(1<<(b-a[0][0]))
    for y in range(h):
        ny = y+1
        nf = [0 for x in range(w)]
        for x in range(w):
            nx = x+1
            if nx < w:
                f[nx] |= ((f[x]<<a[y][nx])|(f[x]>>a[y][nx]))
            if ny < h:
                nf[x] |= ((f[x]<<a[ny][x])|(f[x]>>a[ny][x]))
        if ny < h:
            f = [i for i in nf]
    ans = bin(f[w-1])[2:]
    ans = [abs(i-b) for i in range(len(ans)) if ans[len(ans)-i-1] == "1"]
    print(min(ans))
    return

#Solve
if __name__ == "__main__":
    solve()
