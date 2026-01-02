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
    def f(g,b):
        left = bisect.bisect_left(g,j)
        right = bisect.bisect_left(b,j)
        res = left*(len(b)-right)
        for i in range(left):
            k = bisect.bisect_left(b,j2-g[i])
            if k < len(b) and b[k]+g[i] == j2:
                res -= 1
        return res
    n = I()
    s = input()
    r = []
    g = []
    b = []
    for i in range(n):
        if s[i] == "R":
            r.append(i)
        elif s[i] == "G":
            g.append(i)
        else:
            b.append(i)
    ans = 0
    for j in range(1,n-1):
        sj = s[j]
        j2 = 2*j
        if sj == "R":
            ans += f(g,b)+f(b,g)
        elif sj == "G":
            ans += f(r,b)+f(b,r)
        else:
            ans += f(r,g)+f(g,r)
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
