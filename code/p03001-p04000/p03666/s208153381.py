#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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
    n,a,b,c,d = LI()
    b -= a
    n -= 1
    if b < -n*d or b > n*d:
        print("NO")
        return
    m = n*d
    x = -m
    y = n*(d-c)
    z = max(0,(n-1)*(c-d)+2*c)
    b -= x
    b %= (y+z)
    if b <= y:
        print("YES")
    else:
        print("NO")
    return

#Solve
if __name__ == "__main__":
    solve()
