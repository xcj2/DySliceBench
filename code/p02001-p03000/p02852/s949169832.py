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
    s = list(map(int, input()))
    d = [float("inf")]*(n+1)
    d[n] = 0
    i = n
    p = n
    while i:
        nd = d[i]+1
        for j in range(1,min(i,m)+1):
            k = p-j
            if not s[k]:
                d[k] = nd
                i = k
        if i == p:
            print(-1)
            return
        p = i
    ans = []
    l = 0
    while l < n:
        for i in range(1,min(m,n-l)+1):
            if d[l+i] < d[l]:
                l += i
                ans.append(i)
                break
    print(*ans)
    return

#Solve
if __name__ == "__main__":
    solve()
