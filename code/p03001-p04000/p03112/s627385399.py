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
    a,b,q = LI()
    s = IR(a)
    t = IR(b)
    X = IR(q)
    for x in X:
        i = bisect.bisect_right(s,x)-1
        j = bisect.bisect_right(t,x)-1
        res = float("inf")
        if i >= 0:
            si = s[i]
            if j >= 0:
                tj = t[j]
                res = x-min(si,tj)
            if j+1 < b:
                tj = t[j+1]
                m = min(abs(si-x),abs(tj-x))+abs(tj-si)
                if m < res:
                    res = m
        if i+1 < a:
            si = s[i+1]
            if j >= 0:
                tj = t[j]
                m = min(abs(si-x),abs(tj-x))+abs(si-tj)
                if m < res:
                    res = m
            if j+1 < b:
                tj = t[j+1]
                res = min(res,max(si,tj)-x)
        print(res)
    return

#Solve
if __name__ == "__main__":
    solve()
