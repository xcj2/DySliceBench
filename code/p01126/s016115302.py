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

def solve(n,m,a):
    if m == 0:
        print(a)
        return
    l = LIR(m)
    l.sort(key = lambda x:-x[0])
    x = l[0][0]
    for h,p,q in l:
        if x < h:
            continue
        if p == a:
            x = h-1
            a = q
        elif q == a:
            x = h-1
            a = p
    print(a)
    return

#Solve
if __name__ == "__main__":
    while 1:
        n,m,a = LI()
        if n == m == a == 0:
            break
        solve(n,m,a)
