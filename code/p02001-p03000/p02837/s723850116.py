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
    v = [[] for i in range(n)]
    for i in range(n):
        a = I()
        for j in range(a):
            x,y = LI()
            x -= 1
            v[i].append((x,y))
    m = 1<<n
    ans = 0
    for b in range(m):
        f = [1 if b&(1<<i) else 0 for i in range(n)]
        for i in range(n):
            for x,y in v[i]:
                if f[i]:
                    if f[x] != y:
                        break
            else:
                continue
            break
        else:
            na = sum(f)
            if ans < na:
                ans = na
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
