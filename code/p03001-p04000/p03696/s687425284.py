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
    n,m = LI()
    a = LIR(n)
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                a.sort(key = lambda x:(-1)**i*x[0]+(-1)**j*x[1]+(-1)**k*x[2])
                p = [0,0,0]
                for l in range(m):
                    p[0] += a[l][0]
                    p[1] += a[l][1]
                    p[2] += a[l][2]
                p = abs(p[0])+abs(p[1])+abs(p[2])
                if p > ans:
                    ans = p
    print(ans)
    return

#B
def B():
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(x,y,su):
        x = root(x)
        y = root(y)
        su += comb_2(s[x])+comb_2(s[y])
        if rank[x] < rank[y]:
            s[y] += s[x]
            su -= comb_2(s[y])
            par[x] = y
        else:
            s[x] += s[y]
            su -= comb_2(s[x])
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        return su

    def comb_2(a):
        return a*(a-1)//2

    n,m = LI()
    v = LIR(m)
    par = [i for i in range(n)]
    rank = [0]*n
    s = [1]*n
    su = comb_2(n)
    ans = [su]
    for a,b in v[:0:-1]:
        a -= 1
        b -= 1
        if root(a) != root(b):
            su = unite(a,b,su)
        ans.append(su)
    for i in ans[::-1]:
        print(i)
    return

#C
def C():
    def root(x):
        if par[x] == x:
            return par[x]
        r = root(par[x])
        d[x] += d[par[x]]
        par[x] = r
        return par[x]

    def weight(x):
        root(x)
        return d[x]

    def unite(x,y,w):
        w += weight(x)
        w -= weight(y)
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
            d[x] = -w
        else:
            par[y] = x
            d[y] = w
            if rank[x] == rank[y]:
                rank[x] += 1
    n,m = LI()
    par = [i for i in range(n)]
    rank = [0]*n
    d = [0]*n
    for i in range(m):
        l,r,w = LI()
        l -= 1
        r -= 1
        if root(l) != root(r):
            unite(l,r,w)
        else:
            if weight(r)-weight(l) != w:
                print("No")
                return
    print("Yes")
    return

#D
def D():
    h,w = LI()
    n = I()
    a = LI()
    ans = [0]*h*w
    p = 0
    for i in range(n):
        for j in range(a[i]):
            ans[p+j] = i+1
        p += a[i]
    for i in range(h):
        s = ans[i*w:(i+1)*w]
        if i%2:
            print(*s[::-1])
        else:
            print(*s)
    return

#E
def E():
    n,k = LI()
    s = [int(x) for x in input()]
    f = [0]*n
    j = 0
    su = 1
    p = s[0]
    for i in range(1,n):
        if s[i] != p:
            f[j] = su
            j += 1
            su = 1
            p = s[i]
        else:
            su += 1
    f[j] = su
    f.append(0)
    if s[0]:
        m = sum(f[:2*k+1])
        ans = m
        for i in range(2*k+1,n):
            m -= f[i-2*k-1]
            if not i%2:
                m += f[i-1]
                m += f[i]
            ans = max(m,ans)
    else:
        m = sum(f[:2*k])
        ans = m
        for i in range(2*k,n):
            m -= f[i-2*k]
            if not i%2:
                m += f[i]
                m += f[i+1]
            ans = max(m,ans)
    print(ans)
    return

#F
def F():
    n = I()
    a = LI()
    s = [0,0,0]
    for i in a:
        if i%4 == 0:
            s[0] += 1
        elif i%2 == 0:
            s[1] += 1
        else:
            s[2] += 1
    a = [0]
    while 1:
        if s[2]:
            if a[-1] == 2:
                print("No")
                return
            s[2] -= 1
            a.append(2)
            if s[0]:
                s[0] -= 1
                a.append(0)
        elif s[1]:
            if a[-1] == 2:
                print("No")
            else:
                print("Yes")
            return
        else:
            print("Yes")
            return
    return

#G
def G():
    n,m,l = LI()
    r = LI()
    for i in range(l):
        r[i] -= 1
    d = [[float("inf")]*n for i in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(m):
        a,b,c = LI()
        a -= 1
        b -= 1
        d[a][b] = c
        d[b][a] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    m = 1<<l
    dp = [[float("inf")]*l for i in range(m)]
    for i in range(l):
        dp[1<<i][i] = 0
    for b in range(m):
        for i in range(l):
            x = r[i]
            if not b&(1<<i):
                continue
            for j in range(l):
                if b&(1<<j):
                    continue
                nb = b|(1<<j)
                y = r[j]
                res = dp[b][i]+d[x][y]
                if res < dp[nb][j]:
                    dp[nb][j] = res
    print(min(dp[m-1]))
    return

#H
def H():
    n,m,q = LI()
    f = [[0]*(n+1) for i in range(n+1)]
    for i in range(m):
        l,r = LI()
        f[l][r] += 1
    for i in range(n+1):
        for j in range(n):
            f[i][j+1] += f[i][j]

    for j in range(n+1):
        for i in range(n):
            f[i+1][j] += f[i][j]
    for i in range(q):
        l,r = LI()
        print(f[r][r]-f[r][l-1]-f[l-1][r]+f[l-1][l-1])
    return

#I
def I_():
    n = I()
    s = input()
    a = ""
    q = 0
    for i in s:
        if i == "(":
            q += 1
        else:
            if q:
                q -= 1
            else:
                a += "("
    print(a+s+")"*q)
    return

#Solve
if __name__ == "__main__":
    I_()
