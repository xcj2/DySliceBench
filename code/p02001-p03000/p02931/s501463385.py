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

#A
def A():
    m,d = LI()
    ans = 0
    for i in range(1,m+1):
        for j in range(1,d+1):
            d1 = j%10
            d2 = j//10
            if d1 >= 2 and d2 >= 2 and d1*d2 == i:
                ans += 1
    print(ans)
    return

#B
def B():
    def add(i):
        while i <= m:
            bit[i] += 1
            i += i&-i

    def sum(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i&-i
        return res

    n,k = LI()
    m = 2000
    a = LI()
    bit = [0]*(m+1)
    ans = 0
    for i in range(n):
        ans += (i-sum(a[i]))*k
        add(a[i])
    inv = pow(2,mod-2,mod)
    for i in range(n):
        ans += sum(a[i]-1)*k*(k-1)*inv%mod
    print(ans%mod)
    return

#C
def C():
    n = I()
    s = S()
    if "W" in (s[0],s[-1]):
        print(0)
        return
    d = [0]
    for i in range(1,2*n):
        if s[i] == s[i-1]:
            d.append(1-d[-1])
        else:
            d.append(d[-1])
    if sum(d) != n:
        print(0)
        return
    ans = 1
    s = 0
    for i in d:
        if not i:
            s += 1
        else:
            ans *= s
            s -= 1
            ans %= mod
    for i in range(1,n+1):
        ans *= i
        ans %= mod
    print(ans)
    return

#D
def D():
    n = I()
    m = n.bit_length()
    v = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            k = i^j
            for l in range(m):
                if k&(1<<l):
                    v[i][j] = l+1
                    break
    for i in range(n-1):
        print(*v[i][i+1:])
    return

#E
def E():
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(x,y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
            s[y] += s[x]
            e[y] += e[x]+1
        else:
            par[y] = x
            s[x] += s[y]
            e[x] += e[y]+1
            if rank[x] == rank[y]:
                rank[x] += 1

    n,h,w = LI()
    v = []
    m = h+w
    for i in range(n):
        r,c,a = LI()
        r -= 1
        c += h-1
        v.append((a,r,c))
    v.sort(key = lambda x:-x[0])
    par = [i for i in range(m)]
    rank = [0]*m
    s = [1]*m
    e = [0]*m
    ans = 0
    for a,x,y in v:
        rx,ry = root(x), root(y)
        if rx == ry:
            if e[rx]+1 <= s[rx]:
                ans += a
                e[rx] += 1
        else:
            if e[rx]+e[ry]+1 <= s[rx]+s[ry]:
                ans += a
                unite(x,y)
    print(ans)
    return

#F
def F():

    return

#Solve
if __name__ == "__main__":
    E()
