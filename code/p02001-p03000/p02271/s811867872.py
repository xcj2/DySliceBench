#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
    a = LI()
    q = I()
    m = LI()
    M = max(m)
    l = [i for i in a[:n>>1]]
    r = [i for i in a[n>>1:]]
    nl = len(l)
    nr = len(r)
    fl = [0]*(M+1)
    fr = [0]*(M+1)
    for b in range(1<<nl):
        s = 0
        for i in range(nl):
            if b&(1<<i):
                s += l[i]
        if s <= M:
            fl[s] = 1
    for b in range(1<<nr):
        s = 0
        for i in range(nr):
            if b&(1<<i):
                s += r[i]
        if s <= M:
            fr[s] = 1
    f = [0]*(M+1)
    for i in range(M+1):
        if not fl[i]:
            continue
        for j in range(M+1-i):
            if fr[j]:
                f[i+j] = 1
    for i in m:
        print(["no","yes"][f[i]])
    return

#Solve
if __name__ == "__main__":
    solve()

