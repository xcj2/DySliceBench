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
    a, b, h = IR(3)
    print((a+b)*h//2)
    return

#B
def B():
    d = defaultdict(int)
    d["a"] = deque(S())
    d["b"] = deque(S())
    d["c"] = deque(S())
    tern = "a"
    while d[tern]:
        tern =  d[tern].popleft()
    print(str.capitalize(tern))
    return

#C
def C():
    n, x = LI()
    a = LI()
    ans = 0
    for i in range(n-1):
        if a[i] + a[i + 1] > x:
            if x > a[i]:
                ans += a[i] + a[i + 1] - x
                a[i + 1] = x - a[i]
            else:
                ans += a[i] + a[i + 1] - x
                a[i + 1] = 0
    print(ans)
    return

#D
def D():
    h, w, n = LI()
    ans = [(h - 2) * (w - 2)] + [0] * 9
    d = defaultdict(int)
    for _ in range(n):
        a, b = LI()
        for mb in range(-1, 2):
            mb += b
            for ma in range(-1, 2):
                if mb == ma == 0:
                    continue
                ma += a
                if 2 <= ma < h and 2 <= mb < w:
                    d[(ma, mb)] += 1
    for _, value in d.items():
        ans[value] += 1
        ans[0] -= 1
    print("\n".join(map(str, ans)))
    return

#Solve
if __name__ == '__main__':
    D()
