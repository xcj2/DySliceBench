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
    a,b,c = LI()
    if min(a,b) < c < max(a,b):
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    n = I()
    s = S()
    k = I()
    f = s[k-1]
    for i in range(n):
        if s[i] != f:
            print("*",end = "")
        else:
            print(s[i],end = "")
    print()
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

#Solve
if __name__ == "__main__":
    B()
