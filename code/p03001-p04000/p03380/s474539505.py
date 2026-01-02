#!usr/bin/env python3
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
inf = float("INF")

#A
def A():
    a, b, x = LI()
    if a <= x <= a + b:
        print("YES")
    else:
        print("NO")
    return

#B
def B():
    _, m, x = LI()
    a = LI()
    print(min(bisect.bisect_left(a, x), m - bisect.bisect_right(a, x)))
    return

#C
def C():
    n = II()
    x = LI()
    xb = x[::1]
    xb.sort()
    a = xb[n // 2 - 1]
    b = xb[n // 2]
    for i in range(n):
        if x[i] <= a:
            print(b)
        elif x[i] >= b:
            print(a)
        
    return

#D
def D():
    n = II()
    a = LI()
    a.sort()
    maxa = max(a) / 2
    ans = inf
    for i in range(n):
        if abs(maxa - a[i]) < abs(maxa - ans):
            ans = a[i]
    print(max(a), ans)
    return


#Solve
if __name__ == '__main__':
    D()
