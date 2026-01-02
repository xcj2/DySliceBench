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
    s = LI()
    b = list(set([i for i in s]))
    b.sort()
    f = {i:bisect.bisect_left(b,i) for i in s}
    s = [f[i] for i in s]
    m = max(s)
    d = [0]*(m+1)
    for i in s:
        d[i] += 1
    if d[m] > 1:
        print("No")
        return
    ans = defaultdict(lambda : 0)
    ans[m] = 1
    k = 2
    for i in range(n):
        na = defaultdict(lambda : 0)
        su = 0
        for j in range(k):
            l = m-j
            if l < 0:
                break
            na[l] = ans[l]
            p = d[l]-ans[l]
            if p > 0:
                if su < p:
                    na[l] += su
                    su = 0
                else:
                    na[l] = d[l]
                    su -= p
            su += ans[l]
            ans[l] = na[l]
        k <<= 1
    for i in s:
        if d[i] != ans[i]:
            print("No")
            return
    print("Yes")
    return

#Solve
if __name__ == "__main__":
    solve()
