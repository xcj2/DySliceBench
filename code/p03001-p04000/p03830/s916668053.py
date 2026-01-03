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
def S(): return list(sys.stdin.readline())[:-1]
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

#A
def A():
    n = I()
    return

#B
def B():
    n = I()

    return

#C
def C():
    def factor(n):
        if n < 4:
            return {1:1,n:1}
        else:
            d = defaultdict(lambda : 0)
            i = 2
            m = n
            while i**2 <= n:
                if m%i == 0:
                    while m%i == 0:
                        d[i] += 1
                        m //= i
                i += 1
            d[m] += 1
            return d
    n = I()
    if n == 1:
        print(1)
        quit()
    f = defaultdict(lambda : 0)
    for i in range(2,n+1):
        fact = factor(i)
        for j,k in fact.items():
            if j > 1:
                f[j] += k
                f[j] %= mod
    ans = 1
    for i in f.values():
        ans *= (i+1)
        ans %= mod
    print(ans)
    return

#D
def D():
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(x,y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    n,a,b = LI()
    par = [i for i in range(n)]
    rank = [0]*n
    x = LI()
    for i in range(n-1):
        if a*(x[i+1]-x[i]) < b:
            unite(i,i+1)
    ans = 0
    f = [1]*n
    f[0] = 0
    for i in range(1,n):
        if f[root(i)]:
            ans += b
            f[root(i)] = 0
        else:
            ans += a*(x[i]-x[i-1])
    print(ans)
    return

#E
def E():
    n = I()

    return

#F
def F():
    n = I()

    return

#Solve
if __name__ == "__main__":
    C()
