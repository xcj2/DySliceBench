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
    n,k = LI()
    g = LIR(n)
    l = list(set(([i for (i,j) in g])))
    g.sort(key=lambda x:-x[1])
    l.sort()
    q = []
    q2 = []
    f = [0]*len(l)
    ans = 0
    res = k
    for i in range(n):
        t,d = g[i]
        g[i][0] = t = bisect.bisect_left(l,t)
        if res:
            f[t] += 1
            ans += d
            res -= 1
            if f[t] > 1:
                heappush(q,(d,t))
        else:
            heappush(q2,(-d,t))
    x = sum([i >= 1 for i in f])
    ans += x**2
    s = ans
    while q2 and q:
        d,t = heappop(q2)
        d *= -1
        if f[t]:
            continue
        else:
            nd,nt = heappop(q)
            s -= nd
            s += 2*x+1
            s += d
            x += 1
            f[t] = 1
            f[nt] -= 1
            if ans < s:
                ans = s
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
