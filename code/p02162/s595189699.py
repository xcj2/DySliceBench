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
    T1, T2, R1, R2 = LI()
    if (R1 == -1 or R2 == -1) :
        if (T1 < T2):
            print("Alice")
        elif (T2 < T1) :
            print("Bob")
        else :
            print("Draw")
    else :
        if (R1 > R2):
             print("Alice")
        elif (R2 > R1) :
             print("Bob")
        else :
             print("Draw")
    return


if __name__ == "__main__":
    solve()

