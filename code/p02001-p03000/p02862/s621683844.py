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
    x,y = LI()
    n = x+y
    if n%3 != 0:
        print(0)
        return
    n //= 3
    ans = 1
    for i in range(max(x,y)-n):
        ans *= n-i
        ans %= mod
        ans *= pow(i+1,mod-2,mod)
        ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
