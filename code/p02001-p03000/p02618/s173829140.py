#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
import random
import time
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
    def score(t):
        n = 26
        v = 0
        minus = sum_ = sum(c)
        last = [0]*n
        for i in range(d):
            ti = t[i]-1
            minus -= (i+1-last[ti])*c[ti]
            v += s[i][ti]-minus
            minus += sum_
            last[ti] = i+1
        return v
    start = time.time()
    d = I()
    c = LI()
    s = LIR(d)
    n = 26
    t = []
    for i in range(d):
        argmax = 0
        m = s[i][0]
        for j in range(1,n):
            sj = s[i][j]
            if m < sj:
                argmax = j
                m = sj
        t.append(argmax+1)
    v = score(t)
    nt = [(i%n)+1 for i in range(d)]
    nv = score(t)
    if v < nv:
        t = [i for i in nt]
        v = nv
    i = 0
    while time.time() < 1.5+start:
        nt = [i for i in t]
        r = random.random()
        if r > 0.5:
            if nt[i] < n:
                nt[i] += 1
        else:
            if nt[i] > 1:
                nt[i] -= 1
        nv = score(nt)
        if v < nv:
            t = [i for i in nt]
            v = nv
        i += 1
        i %= d
    for i in t:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
