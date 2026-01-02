#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
    m = sum(a)/n
    f = {}
    for i in range(n):
        if not a[i] in f:
            f[a[i]] = i
    a = list(set(a))
    a.sort()
    i = bisect.bisect_left(a,m)-1
    if abs(m-a[i]) < abs(a[i+1]-m):
        print(f[a[i]])
    elif abs(m-a[i]) == abs(a[i+1]-m):
        print(min(f[a[i]],f[a[i+1]]))
    else:
        print(f[a[i+1]])
    return

#Solve
if __name__ == "__main__":
    solve()
