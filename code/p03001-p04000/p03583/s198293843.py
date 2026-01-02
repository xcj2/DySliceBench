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
    n = I()
    for i in range(1,3501):
        for j in range(i,3501):
            p = i*j
            s = 4*p-n*(i+j)
            if s <= 0:
                continue
            m = n*p
            if m%s:
                continue
            k = m//s
            q = j*k
            r = k*i
            if (p+q+r)*n == 4*i*j*k:
                print(i,j,k)
                return
    return


#Solve
if __name__ == "__main__":
    solve()
