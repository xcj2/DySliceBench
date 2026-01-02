#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
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
    def root(x):
        if x == p[x]:
            return x
        p[x] = root(p[x])
        return p[x]
    def unite(x,y):
        x = root(x)
        y = root(y)
        if r[x] < r[y]:
            p[x] = y
        else:
            p[y] = x
            if r[x] == r[y]:
                r[x] += 1

    n,m,k = LI()
    p = [i for i in range(n)]
    r = [0]*n
    f = [0]*n
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        if root(a) != root(b):
            unite(a,b)
        f[a] += 1
        f[b] += 1
    for i in range(k):
        a,b = LI()
        a -= 1
        b -= 1
        if root(a) == root(b):
            f[a] += 1
            f[b] += 1
    d = defaultdict(lambda : 0)
    for i in range(n):
        d[root(i)] += 1
    ans = []
    for i in range(n):
        ans.append(d[root(i)]-f[i]-1)
    print(*ans)
    return

#Solve
if __name__ == "__main__":
    solve()
