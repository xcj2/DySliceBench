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
    s = SR(3)
    for i in range(3):
        print(s[i][i], end="")
    print()
    return

#B
def B():
    a, b = LI()
    ans = 0
    for i in range(a, b + 1):
        x = str(i)
        for k in range(len(x)//2):
            if x[k] != x[-k - 1]:
                break
        else:
            ans += 1
    print(ans)
    return

#C
def C():
    n, m = LI()
    if n == m == 1:
        print(1)
        return
    if n == 1 or m == 1:
        print(max(n - 2, m - 2))
        return
    if n == 2 or m == 2:
        print(0)
        return
    print(n * m - n * 2 - (m - 2) * 2)
    return

#D
def D():
    n, k = LI()
    ans = 0
    if k == 0:
        print(n * n)
        return
    for b in range(k + 1, n + 1):
        tmp1, tmp2 = n // b, n % b
        ans += tmp1 * (b - k) + max(tmp2 - k + 1, 0)
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
