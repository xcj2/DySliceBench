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
    a = LI()
    b = LI()
    if sum(a) < sum(b):
        print(-1)
        return
    c = [a[i]-b[i] for i in range(n)]
    mc = [-i for i in c if i < 0]
    pc = [i for i in c if i >= 0]
    pc.sort(reverse = True)
    for i in range(1,len(pc)):
        pc[i] += pc[i-1]
    s = sum(mc)
    if s == 0:
        print(0)
        return
    for i in range(len(pc)):
        if pc[i] >= s:
            break
    print(len(mc)+i+1)
    return

#Solve
if __name__ == "__main__":
    solve()
