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
    n,Q = LI()
    q = LIR(n)
    q.sort(key = lambda x:x[2])
    d = IR(Q)
    ans = [-1]*(Q+1)
    f = [0]*Q
    for s,t,x in q:
        l = bisect.bisect_left(d,s-x)
        r = bisect.bisect_left(d,t-x)
        while l < r:
            while ans[l] != -1:
                l = f[l]
            if r <= l:
                break
            ans[l] = x
            f[l] = r
            l += 1
    for i in ans[:-1]:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
