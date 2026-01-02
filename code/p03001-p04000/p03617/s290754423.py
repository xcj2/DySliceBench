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
    q,h,s,d = LI()
    d = min(d,2*s,4*h,8*q)
    s = min(s,2*h,4*q)
    h = min(h,2*q)
    n = I()
    n *= 4
    ans = d*(n>>3)
    n &= (1<<3)-1
    ans += s*(n>>2)
    n &= (1<<2)-1
    ans += h*(n>>1)
    n &= (1<<1)-1
    ans += q*n
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

#Solve
if __name__ == "__main__":
    A()
