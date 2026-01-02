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
    x, y = LI()
    print(x+y//2)
    return

#B
def B():
    II()
    t, a = LI()
    h = LI()
    ans = [0,inf]
    for num, i in enumerate(h):
        if ans[1] > abs(t - a - i * 0.006):
            ans = [num, abs(t - a - i * 0.006)]
    print(ans[0] + 1)
    return

#C
def C():
    n, m = LI()
    py = LIR(m)
    pya = py[::1]
    py.sort(key=lambda x: x[1])
    city = [1 for i in range(n)]
    dicity = {}
    for p, y in py:
        dicity[(p,y)] = city[p-1]
        city[p-1] += 1    
    for p, y in pya:
        a = "00000" + str(p)
        a = a[-6:]
        b = "00000" + str(dicity[(p, y)])
        b = b[-6:]
        print(a+b)

    return

#D
def D():
    h, w, k = LI()
    stick = [[0, 0] for i in range(w)]
    stick[0] = [1, 0]
    for i in range(1, w):
        stick[i][0] += stick[i - 1][0] + stick[i - 1][1]
        stick[i][1] += stick[i - 1][0]
    dp1 = [0] * (w + 2)
    dp1[1] = 1
    for i in range(h):
        dp2 = [0] * (w + 2)
        for wi in range(1, w + 1):
            tmp = dp1[wi - 1] * stick[wi - 1][1] * stick[w - wi][0]
            tmp += dp1[wi + 1] * stick[w - wi][1] * stick[wi - 1][0]
            tmp += dp1[wi] * stick[wi - 1][0] * stick[w - wi][0]
            dp2[wi] = tmp
            dp2[wi] %= mod
        dp1 = dp2
    print(dp2[k])

    return

#Solve
if __name__ == '__main__':
    D()
