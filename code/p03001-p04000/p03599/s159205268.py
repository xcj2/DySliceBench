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
    n, a = II(), II()
    print(n * n - a)
    return

#B
def B():
    _ = II()
    k = II()
    x = LI()
    ans = 0
    for xi in x:
        ans += min(xi, k - xi)
    print(ans * 2)
    return

#C
def C():
    a, b, c, d, e, F = LI()
    ans = [min(a,b)*100, 0]
    for ai in range(F // (100 * a) + 1):
        for bi in range((F - 100 * ai * a) // (100 * b) + 1):
            if ai == bi == 0:
                continue
            ab = ai * 100 * a + bi * 100 * b
            for ci in range((F - ab) // c + 1):
                for di in range((F - ab - ci * c) // d + 1):
                    if (ai * a + bi * b) * e < ci * c + di * d:
                        continue
                    if ans[1] / ans[0] < (ci * c + di * d) / (ab + ci * c + di * d):
                        ans = [ab + ci * c + di * d, ci * c + di * d]
    print(*ans)
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
