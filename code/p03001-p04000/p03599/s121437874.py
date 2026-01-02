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
    a,b,c,d,e,f = LI()
    ans = 0
    p = [100*a,0]
    n = 31
    for x in range(n):
        A = a*x
        for y in range(n):
            B = b*y
            s = A+B
            r = min(f-100*s,s*e)
            if r > 0:
                for z in range(r+1):
                    C = c*z
                    rest = r-C
                    if rest < 0:
                        break
                    w = rest//d
                    D = d*w
                    res = (C+D)/(100*s+C+D)
                    if ans < res:
                        ans = res
                        p[0] = 100*s+C+D
                        p[1] = C+D
    print(*p)
    return

#Solve
if __name__ == "__main__":
    solve()
