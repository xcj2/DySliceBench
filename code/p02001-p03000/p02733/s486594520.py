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
    h,w,k = LI()
    a = [list(map(int, input())) for i in range(h)]
    s = [[0]*(w+1)]+[[0]+list(accumulate(i)) for i in a]
    for j in range(w+1):
        for i in range(h):
            s[i+1][j] += s[i][j]
    ans = float("inf")
    for b in range(1<<(h-1)):
        l = [0]
        for i in range(h-1):
            if b&(1<<i):
                l.append(i+1)
        l.append(h)
        ll = len(l)-1
        su = [0]*ll
        m = bin(b).count("1")
        p = 0
        f = 0
        for j in range(1,w+1):
            for i in range(ll):
                u = l[i]
                d = l[i+1]
                su[i] += s[d][j]-s[d][p]-s[u][j]+s[u][p]
                if su[i] > k:
                    m += 1
                    p = j-1
                    su = [0]*ll
                    for ii in range(ll):
                        u = l[ii]
                        d = l[ii+1]
                        su[ii] = s[d][j]-s[d][p]-s[u][j]+s[u][p]
                        if su[ii] > k:
                            f = 1
                    break
            p = j
            if f:
                m = float("inf")
                break
        if m < ans:
            ans = m
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
