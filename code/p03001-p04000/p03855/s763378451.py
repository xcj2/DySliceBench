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
    a = ["a", "i", "u", "e", "o"]
    c = S()
    if c[0] in a:
        print("vowel")
    else:
        print("consonant")
    return

#B
def B():
    _ = II()
    t = LI()
    tsum = sum(t)
    for _ in range(II()):
        p, x = LI()
        print(tsum - t[p - 1] + x)
    return

#C
def C():
    s = input()
    lens = len(s)
    check = ["dream", "dreamer", "erase", "eraser"]
    q = deque()
    q.append(0)
    while q:
        p = q.pop()
        if p == lens:
            print("YES")
            return
        for i in check:
            if s[p:p + len(i)] == i:
                q.appendleft(p + len(i))
    print("NO")
    return

#D
def D():
    class UnionFind():

        def __init__(self, n):
            self.par = [i for i in range(n)]
            self.size = [1] * n
        
        def find(self, a):
            if a == self.par[a]:
                return a
            x = self.find(self.par[a])
            self.par[a] = x
            return x

        def unite(self, a, b):
            a = self.find(a)
            b = self.find(b)
            if a == b: return
            if a > b: a, b = b, a
            self.par[b] = a
            self.size[a] += self.size[b]

    n, k, l = LI()
    rail = UnionFind(n)
    road = UnionFind(n)

    for _ in range(k):
        p, q = LI_()
        rail.unite(p, q)
    for _ in range(l):
        r,s = LI_()
        road.unite(r, s)
    d = defaultdict(int)
    for i in range(n):
        d[(rail.find(i), road.find(i))] += 1
    for i in range(n):
        print(d[(rail.find(i), road.find(i))], end=" ")
    print()
    return

#Solve
if __name__ == '__main__':
    D()
