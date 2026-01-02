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
    s = []
    for i in range(m):
        a = LI()[1:]
        for j in range(len(a)):
            a[j] -= 1
        s.append(a)
    p = LI()
    ans = 0
    for b in range(1<<n):
        su = [0]*m
        for i in range(m):
            for j in s[i]:
                if b&(1<<j):
                    su[i] ^= 1
        if su == p:
            ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
