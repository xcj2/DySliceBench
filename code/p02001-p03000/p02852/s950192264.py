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
    n,m = LI()
    s = input()
    d = [float("inf")]*(n+1)
    d[n] = 0
    i = n
    k = 1
    mi = n
    while i >= 0:
        pre = i
        i = mi
        i -= m
        for j in range(m):
            x = i+j
            if x >= 0:
                if s[x] == "0":
                    d[x] = k
                    if x < mi:
                        mi = x
        if pre == i:
            print(-1)
            return
        k += 1
    q = []
    for i in range(n+1):
        heappush(q,(-d[i],i))
    ans = [0]
    x = 0
    dx = d[0]
    while q:
        di,i = heappop(q)
        if i <= x:
            continue
        di *= -1
        if dx-1 == di:
            dx = di
            x = i
            ans.append(i)
    a = [ans[i+1]-ans[i] for i in range(len(ans)-1)]
    print(*a)
    return

#Solve
if __name__ == "__main__":
    solve()
