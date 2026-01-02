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
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n,x,m = LI()
    f = [0]*m
    a = x
    ans = 0
    for i in range(1,n+1):
        ans += a
        if f[a]:
            break
        f[a] = 1
        a = pow(a,2,m)
    s = []
    f = [0]*m
    for j in range(i+1,n+1):
        if f[a]:
            break
        f[a] = 1
        a = pow(a,2,m)
        s.append(a)
    r = n-i
    if s:
        ans += sum(s)*(r//len(s))+sum(s[:r%len(s)])
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
