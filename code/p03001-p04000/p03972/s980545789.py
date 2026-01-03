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
    w,h = LI()
    p = IR(w)
    q = IR(h)
    l = []
    for i in p:
        l.append([i,0])
    for i in q:
        l.append([i,1])
    x = 0
    y = 0
    l.sort()
    ans = 0
    for i,j in l:
        if j:
            ans += i*(w+1-x)
            y += 1
        else:
            ans += i*(h+1-y)
            x += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
