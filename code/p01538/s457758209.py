#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    while 1:
        n = II()
        ans = 0
        if n == 0:
            break
        i = 1
        while i < n / 2:
            tmp = 0
            l = i
            while tmp < n:
                tmp += l
                l += 1
            if tmp == n:
                ans += 1
            i += 1
        print(ans)  

    return

#B
def B():

    def f(x):
        tmp = 0
        for i in range(len(x)-1):
            x1 = int(x[:i+1])
            x2 = int(x[i+1:])
            tmp = max(tmp, x1 * x2)
        return tmp

    q = II()
    for i in range(q):
        ans = 0
        n = II()
        while n > 9:
            ans += 1
            n = f(str(n))

        print(ans)
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    R, C, K = LI()
    n = II()
    rc = LIR_(n)
    fldr = [0 for _ in range(R)]
    fldc = [0 for _ in range(C)]
    for r, c in rc:
        fldr[r] += 1
        fldc[c] += 1
    fldcs = fldc[::1]
    fldcs.sort()
    fldrs = fldr[::1]
    fldrs.sort()
    ans = 0
    dr = defaultdict(int)
    dc = defaultdict(int)
    for k in range(R):
        dr[fldr[k]] += 1
    for k in range(C):
        dc[fldc[k]] += 1
    for k in range(K+1):
        ans += dr[K - k] * dc[k]
    for r, c in rc:
        a = fldr[r] + fldc[c]
        if a == K:
            ans -= 1
        elif a == K + 1:
            ans += 1
    print(ans)
    return

#F
def F():
    n, m = LI()
    uvl = LIR_(m)
    dist = [[inf] * n for _ in range(n)]
    dist0 = defaultdict(int)
    full = []
    d = 0
    for u, v, l in uvl:
        if u == 0:
            dist0[v] = l + 1
            full.append(v)
            d += 1
        elif v == 0:
            dist0[u] = l + 1
            d += 1
            full.append(u)
        else:
            l += 1
            dist[u][v] = l
            dist[v][u] = l
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    fulls = itertools.combinations(range(d), 2)
    ans = inf
    for a, b in fulls:
        a, b = full[a], full[b]
        tmp = dist0[a] + dist0[b] + dist[a][b]
        ans = min(ans, tmp)
    print(-1 if ans == inf else ans)
    return

#G
def G():
    s = S()
    s = s[::-1]
    M_count = s.count("M")
    M_lis = [0] * M_count
    M_count //= 2
    tmp = 0
    k = 0
    for i in range(len(s)):
        if s[i] == "+":
            tmp += 1
        elif s[i] == "-":
            tmp -= 1
        else:
            M_lis[k] = tmp
            k += 1
    M_lis.sort()
    print(-sum(M_lis[:M_count]) + sum(M_lis[M_count:]))


    return

#H
def H():
    def f(t):
        return a * t + b * math.sin(c * t * math.pi)
    a, b, c = LI()
    ok = 99 // a + 1
    ng = 0
    while 1:
        t = (ok + ng) / 2
        ft = f(t)
        if abs(ft - 100) <= 10 ** (-6):
            print(t)
            return
        if ft > 100:
            ok = t
        if ft < 100:
            ng = t
    return

#Solve
if __name__ == '__main__':
    B()
