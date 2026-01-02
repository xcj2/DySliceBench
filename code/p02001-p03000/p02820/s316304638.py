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
    def f(c):
        if c == "r":
            return 0
        elif c == "s":
            return 1
        return 2
    def g(i,j):
        if (i+1)%3 == j:
            return 1
        return 0
    n,K = LI()
    r = LI()
    t = input()
    t = [f(i) for i in t]
    c = [1]*n
    ans = 0
    for i in range(n):
        if not c[i]:
            continue
        j = i
        l = []
        while j < n:
            l.append(j)
            c[j] = 0
            j += K
        dp = [[0]*3 for j in range(len(l))]
        for j in range(3):
            li = t[l[0]]
            dp[0][j] = r[j]*g(j,li)
        for j in range(1,len(l)):
            nj = j-1
            cj = t[l[j]]
            for k in range(3):
                q = r[k]*g(k,cj)
                for m in range(3):
                    if k == m:
                        continue
                    nd = dp[nj][m]+q
                    if dp[j][k] < nd:
                        dp[j][k] = nd

        ans += max(dp[-1])
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
