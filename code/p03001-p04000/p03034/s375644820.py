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
    s = LI()
    ans = 0
    for c in range(1,n+1):
        K = (n-1)//c
        dp = 0
        S = set([0,n-1])
        for k in range(1,K+1):
            a = i = n-1-k*c
            if i in S:
                break
            b = a-c
            if b >= a or b <= 0:
                break
            S.add(i)
            j = k*c
            if j in S:
                break
            S.add(j)
            cost = s[i]+s[j]
            dp += cost
            if ans < dp:
                ans = dp
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
