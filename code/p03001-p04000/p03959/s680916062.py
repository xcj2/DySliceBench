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
def S(): return list(sys.stdin.readline())[:-1]
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

#A
def A():
    n = I()

    return

#B
def B():
    n = I()

    return

#C
def C():
    n = I()
    t = LI()
    a = LI()
    f = [1]*n
    h = [float("inf")]*n
    ma = 0
    for i in range(n):
        if t[i] > ma:
            ma = t[i]
            f[i] = 0
        h[i] = ma
    ma = 0
    for i in range(n)[::-1]:
        if a[i] > ma:
            ma = a[i]
            if not f[i] and h[i] != ma:
                print(0)
                return
            f[i] = 0
            if h[i] < ma:
                print(0)
                return
        if ma < h[i]:
            h[i] = ma
    ans = 1
    for i in range(n):
        if f[i]:
            ans *= h[i]
            ans %= mod
    print(ans)
    return

#D
def D():
    n = I()

    return

#E
def E():
    n = I()

    return

#F
def F():
    n = I()

    return

#G
def G():
    n = I()

    return

#H
def H():
    n = I()

    return

#I
def I_():
    n = I()

    return

#J
def J():
    n = I()

    return

#Solve
if __name__ == "__main__":
    C()
