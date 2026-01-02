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
    def f(m):
        if d[m] != None:
            return d[m]
        n = m
        for i in a:
            n = n-n%i
        d[m] = n
        return n
    k = I()
    a = LI()
    d = defaultdict(lambda : None)
    l,r = 0,1e19
    while r-l > 1:
        m = (r+l)//2
        if f(m) < 2:
            l = m
        else:
            r = m
    mi = r
    l,r = 0,1e19
    while r-l > 1:
        m = (r+l)//2
        if f(m) <= 2:
            l = m
        else:
            r = m
    ma = l
    if mi <= ma:
        if f(mi) != 2:
            print(-1)
        else:
            print(int(mi),int(ma))
    else:
        print(-1)
    return

#C
def C():
    n = I()

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


#Solve
if __name__ == "__main__":
    B()
