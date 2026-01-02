#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
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
    a = [input() for i in range(n)]
    sp,sm = [],[]
    for i in range(n):
        p = 0
        m = 0
        for j in a[i]:
            if j == "(":
                p += 1
            else:
                p -= 1
            if p < m:
                m = p
        if p > 0:
            sp.append((m,p))
        else:
            sm.append((m,p))
    sp.sort(reverse = True)
    sm.sort(key = lambda x:x[0]-x[1])
    k = 0
    for m,p in sp:
        if k+m < 0:
            print("No")
            return
        k += p
    for m,p in sm:
        if k+m < 0:
            print("No")
            return
        k += p
    if k != 0:
        print("No")
    else:
        print("Yes")
    return

#Solve
if __name__ == "__main__":
    solve()
