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
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n = I()
    p = LIR(n)
    r = [(x+y,x-y) for x,y in p]
    mx = [float("inf"),float("inf")]
    my = [float("inf"),float("inf")]
    Mx = [-float("inf"),float("inf")]
    My = [float("inf"),-float("inf")]
    for X,Y in r:
        if X < mx[0]:
            mx = [X,Y]
        if Y < my[1]:
            my = [X,Y]
        if Mx[0] < X:
            Mx = [X,Y]
        if My[1] < Y:
            My = [X,Y]
    ans = 0
    for X,Y in r:
        x = (X+Y)//2
        y = (X-Y)//2
        for A,B in (mx,my,Mx,My):
            a = (A+B)//2
            b = (A-B)//2
            d = abs(x-a)+abs(y-b)
            if ans < d:
                ans = d
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
