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
    def gcd(a,b):
        if a == 0:
            return b
        return gcd(b%a, a)
    n,k = LI()
    a = LI()
    if max(a) < k:
        print("IMPOSSIBLE")
        return
    g = a[0]
    for i in a[1:]:
        g = gcd(g, i)
    if g == 1:
        print("POSSIBLE")
    else:
        if k%g == 0:
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")
    return

#B
def B():
    n = I()

    return

#C
def C():
    x,y,z = LI()
    n = x+y+z
    c = LIR(n)
    for i in range(n):
        c[i].append(c[i][0])
    c.sort(key = lambda x:-(x[1]-x[3]))
    for i in range(y):
        c[i][3] = c[i][1]
    c.sort(key = lambda x:-(x[2]-x[3]))
    for i in range(y):
        c[i][3] = c[i][1]

    for i in c:
        print(i)
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
    A()
