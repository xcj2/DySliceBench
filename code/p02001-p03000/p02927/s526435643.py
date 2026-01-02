#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import *
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
    m, d = LI()
    ans = 0
    for i in range(1, m + 1):
        for j in range(10, d + 1):
            if int(str(j)[0]) < 2 or int(str(j)[1]) < 2:
                continue
            if i == int(str(j)[0]) * int(str(j)[1]):
                ans += 1
    print(ans)
    return

#B
def B():
    n, l = LI()
    a = LI()
    d0 = defaultdict(int)
    d1 = defaultdict(int)
    for i in a:
        d0[i] += 1
    for i in range(n):
        b = 0
        for k in range(i+1, n):
            if a[i] > a[k]:
                b += 1
        d1[i] = b
    ans = 0
    d2 = list(d0.items())
    d2.sort()
    d3 = defaultdict(int)
    d = 0
    for key, value in d2:
        d3[key] = d
        d += value
    print(d3,d1)
    for i in range(n):
        ans += d3[a[i]] * l * (l-1) // 2 + d1[i] * l
        ans %= mod
    print(ans % mod)
    return

#C
def C():
    n = II()
    s = itertools.product([1, 0], repeat=2 * n)
    a = list(itertools.combinations(range(2*n), 2))
    d = defaultdict(int)
    def dfs(a):
        if len(a) == n:
            lis.append(a)
            return True
        for i in range(n):
            if d[i] == 0:
                d[i] = 1
                for k in range(n):
                    if d[k] == 0:
                        d[k] = 1
                        a.append((i, k))
                        dfs(a)
                        a.remove((i, k))
    lis = []
    dfs([])
    for si in s:
        for di in lis:
            b = list(si[::1])
            for x, y in di:
                for i in range(x, y + 1):
                    b[i] ^= 1
            if sum(b) < 1:
                print(si, di)
                break

    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    A()
