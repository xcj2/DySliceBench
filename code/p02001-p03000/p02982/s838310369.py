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
    n,a,b = LI()
    print(min(a*n,b))
    return

#B
def B():
    n,d = LI()
    x = LIR(n)
    f = defaultdict(lambda : 0)
    for i in range(1000000):
        f[i*i] = 1
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            s = 0
            for k in range(d):
                s += (x[i][k]-x[j][k])**2
            if f[s]:
                ans += 1
    print(ans)
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
