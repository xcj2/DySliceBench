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

#A
def A():
    n,m = LI()
    a = LIR(n)
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                a.sort(key = lambda x:(-1)**i*x[0]+(-1)**j*x[1]+(-1)**k*x[2])
                p = [0,0,0]
                for l in range(m):
                    p[0] += a[l][0]
                    p[1] += a[l][1]
                    p[2] += a[l][2]
                p = abs(p[0])+abs(p[1])+abs(p[2])
                if p > ans:
                    ans = p
    print(ans)
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

#I
def I_():

    return

#Solve
if __name__ == "__main__":
    A()
