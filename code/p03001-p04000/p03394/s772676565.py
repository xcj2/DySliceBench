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
    if n == 3:
        l = [2,5,63]
    elif n == 4:
        l = [2,5,20,63]
    elif n == 5:
        l = [2,3,4,6,9]
    else:
        l = []
        while len(l) < n:
            for k in range(30000):
                for i in [2,3,4,6]:
                    l.append(6*k+i)
                    if len(l) == n:
                        break
                else:
                    continue
                break
        s = sum(l)%6
        if s == 2:
            l[4] = 30000
        elif s == 3:
            l[5] = 30000
        elif s == 4:
            l[6] = 30000
        elif s == 5:
            l[5] = 29998
    s = sum(l)%6
    print(*l)
    return

#Solve
if __name__ == "__main__":
    solve()
