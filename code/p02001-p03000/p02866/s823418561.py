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
mod = 998244353

def solve():
    n = I()
    d = LI()
    f = defaultdict(lambda : 0)
    for i in d:
        f[i] += 1
    m = max(d)
    ans = 1
    if f[0] != 1:
        print(0)
        return
    if d[0] != 0:
        print(0)
        return
    for i in range(m):
        ans *= pow(f[i],f[i+1],mod)
        ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
