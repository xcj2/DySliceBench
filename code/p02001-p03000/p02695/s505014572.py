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
    def f(A):
        res = 0
        for a,b,c,d in g:
            if A[b] == A[a]+c:
                res += d
        return res

    n,m,q = LI()
    g = LIR(q)
    for i in range(q):
        g[i][0] -= 1
        g[i][1] -= 1
    l = [([i],i) for i in range(1,m+1)]
    for i in range(n-1):
        l = [(x+[j], j) for (x,y) in l for j in range(y,m+1)]
    ans = 0
    for A,_ in l:
        s = f(A)
        if ans < s:
            ans = s
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
