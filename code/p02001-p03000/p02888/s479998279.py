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
    N = 10**6+1
    bit = [0]*(N+1)
    def add(i):
        while i <= N:
            bit[i] += 1
            i += i&-i
    def sum(i):
        res = 0
        while i:
            res += bit[i]
            i -= i&-i
        return res

    n = I()
    l = LI()
    l.sort()
    ans = 0
    s = []
    k = 0
    for i in range(n):
        li = l[i]
        ans += k-sum(li)
        for j in range(i):
            add(li+l[j])
            k += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
