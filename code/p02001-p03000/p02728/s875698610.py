#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
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
    def dfs(x):
        fx = ans[x]
        nf = fx*inv[s[x]-1]%mod
        sx = s[x]
        for y in v[x]:
            sy = s[y]
            nsx = sx-sy
            nsy = s[x]
            if ans[y] == None:
                fy = nf*s[y]*f[nsy-1]*p[nsx]%mod
                ans[y] = fy
                s[x] = nsx
                s[y] = nsy
                dfs(y)
                s[x] = sx
                s[y] = sy

    n = I()
    f = [1]
    for i in range(1,n+1):
        f.append(f[-1]*i%mod)
    inv = [None]*(n+1)
    inv[n] = pow(f[n],mod-2,mod)
    for i in range(n)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod

    v = [[] for i in range(n)]
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    d = [0]*n
    d[0] = 1
    q = deque([0])
    p = [None]*n
    while q:
        x = q.popleft()
        nd = d[x]+1
        for y in v[x]:
            if not d[y]:
                d[y] = nd
                p[y] = x
                q.append(y)
    V = list(range(n))
    V.sort(key = lambda x:-d[x])
    m = d[V[0]]
    s = [0]*n
    res = 1
    for i in V:
        j = p[i]
        s[i] += 1
        if j != None:
            s[j] += s[i]
            res *= inv[s[i]]
        if d[i] == m:
            continue
        res *= f[s[i]-1]
        res %= mod
    ans = [None]*n
    ans[0] = res
    p = [pow(i,mod-2,mod) for i in range(n+1)]
    dfs(0)
    for i in ans:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
