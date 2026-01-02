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
mod = 2019

def solve():
    a = list(map(int, input()))
    n = len(a)
    for i in range(n):
        a[i] *= pow(10,n-i-1,mod)
        a[i] %= mod
    s = [0]+list(accumulate(a))
    d = [0]*mod
    ans = 0
    for i in s:
        j = i%mod
        ans += d[j]
        d[j] += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
