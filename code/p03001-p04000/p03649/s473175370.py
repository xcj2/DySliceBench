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

    return

#D
def D():
    n = I()

    return
#E
def E():
    n = I()
    a = LI()
    ans = 0
    s = 1
    while s:
        b = [a[i]//n for i in range(n)]
        s = sum(b)
        a = [(a[i]%n+s-b[i]) for i in range(n)]
        ans += s
        
    print(ans)
    return

#F
def F():
    n = I()

    return

#Solve
if __name__ == "__main__":
    E()
