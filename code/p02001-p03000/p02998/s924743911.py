#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
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
    s = S()
    for i in range(3):
        if s[i] == s[i + 1]:
            print("Bad")
            return
    print("Good")
    return

#B
def B():
    n, l = LI()
    lis = [l + i for i in range(n)]
    s = sum(lis)
    a = inf
    for i in lis:
        if abs(a) > abs(i):
            a = i
    print(s-a)
    return

#C
def C():
    def gcd(a, b):
        a, b = max(a, b), min(a, b)
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b // gcd(a, b)
    a, b, c, d = LI()
    x = b // c - (a-1) // c
    y = b // d - (a-1) // d
    z = b // lcm(c , d) - (a-1) // lcm(c , d)
    print(b-a+1-(x+y-z))
    return

#D
def D():
    n = II()
    ab = LIR(n)
    ab.sort(key=lambda x: x[1])
    now = 0
    for a, b in ab:
        now += a
        if now <= b:
            continue
        print("No")
        return
    print("Yes")
    return

#E
def E():
    n, k = LI()
    if k > (n - 1) * (n - 2) / 2:
        print(-1)
        return
    d = (n - 1) * (n - 2) // 2 - k
    a = [[] for i in range(n)]
    for i in range(n):
        if i != 1:
            a[i].append(1)
            a[1].append(i)
    l = 0
    m = 2
    while d > 0:
        a[l].append(m)
        m += 1
        d -= 1
        if m == n:
            l += 1
            m = l + 1
            if l == 1:
                l = 2
                m = 3
    aa = 0
    ans = []
    for num,i in enumerate(a):
        for l in i:
            if num < l:
                aa += 1
                ans.append((num+1,l+1))
    print(aa)
    for x, y in ans:
        print(x, y)
    return

#F
def F():
    n = II()
    xy = LIR(n)
    d = defaultdict(list)
    par = defaultdict(int)
    for _, y in xy:
        par[y] = y
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]
    
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return False
        if x > y: x, y = y, x
        par[y] = x
        return True
    
    setx = set()
    for x, y in xy:
        d[x].append(y)
    for key, value in d.items():
        p = value[0]
        for v in value[1:]:
            unite(p, v)
    ans1 = defaultdict(int)
    ans2 = defaultdict(int)
    ans = 0
    for x, y in xy:
        root(y)
    # print(par)
    for _, value in d.items():
        ans1[par[value[0]]] += 1
    for _, value in par.items():
        ans2[value] += 1
    # print(ans1,ans2)
    for key, value in ans1.items():
        ans += ans2[key] * value
    print(ans - n)
    return

#Solve
if __name__ == '__main__':
    F()