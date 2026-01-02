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
    n, a, b = LI()
    print(min(n * a, b))
    return

#B
def B():
    n, d = LI()
    x = LIR(n)
    a = list(itertools.combinations(range(n), 2))
    ans = 0
    for a1,a2 in a:
        b = 0
        for bi in range(d):
            b += (x[a1][bi] - x[a2][bi])** 2
        if float.is_integer(math.sqrt(b)):
            ans += 1
    print(ans)
    return

#C
def C():
    l, r = LI()
    ans = 2018
    if l // 2019 == r // 2019:
        for i in range(l, r + 1):
            for k in range(i+1, r + 1):
                ans = min(ans, (i * k) % 2019)
        print(ans)
    else:
        print(0)
    return

#D
def D():
    n = II()
    a = LI()
    a = a + [a[0]]
    ans = [0] * n
    x = 0
    for i in range(1, n, 2):
        x = x + a[i + 1] - a[i]
    ans[1] = a[0] - x
    ans[0] = ans[1] + 2 * x
    for i in range(2, n):
        ans[i] = (a[i - 1] - ans[i - 1] // 2) * 2
    print(" ".join(map(str, ans)))

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
    C()
