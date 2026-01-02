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
    for i in range(n):
        ans += d3[a[i]] * l * (l-1) // 2 + d1[i] * l
        ans %= mod
    print(ans % mod)
    return

#C
def C():
    n = II()
    s = S()
    if s[0] == "W":
        print(0)
        return
    lis = [0] * (2 * n)
    l = [0] * (2 * n)
    l[0] = 1
    for i in range(1, 2 * n):
        lis[i] = (lis[i-1] ^ (s[i] == s[i-1]))
        l[i] += l[i - 1] + (lis[i] == 0)
    ans = 1
    if l[-1] != n or s[0] == "W":
        print(0)
        return
    k = 1
    for i in range(2 * n):
        if lis[i]:
            ans *= l[i] - (k - 1)
            ans %= mod
            k += 1
    print(ans * math.factorial(n) % mod)
    return

#D
def D():
    n = II()
    l = len(bin(n)) - 2
    for i in range(n - 1):
        ans = []
        for j in range(i + 2, n + 1):
            for k in range(l):
                if (j >> k) & 1 != ((i + 1) >> k) & 1:
                    ans.append(str(k + 1))
                    break
        print(" ".join(ans))
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
    D()
