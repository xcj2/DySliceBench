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
    n,m = LI()
    a = LI()
    ans = sum([(a[i+1]-a[i])%m for i in range(n-1)])
    s = [0]*(2*m)
    f = [0]*(2*m)
    x = a[0]-1
    for i in range(1,n):
        y = a[i]-1
        if y < x:
            y += m
        if x+1 >= y:
            x = a[i]-1
            continue
        s[x+2] += 1
        s[y+1] -= 1
        f[y+1] -= y-x-1
        x = a[i]-1
    for i in range(2*m-1):
        s[i+1] += s[i]
        f[i+1] += f[i]+s[i+1]
    f = [f[i]+f[i+m] for i in range(m)]
    print(ans-max(f))
    return

#Solve
if __name__ == "__main__":
    solve()
