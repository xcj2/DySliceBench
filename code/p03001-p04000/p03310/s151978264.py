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
    n = II()
    if n % 2:
        print(2 * n)
    else:
        print(n)
    return

#B
def B():
    n = II()
    a = LI()
    a.sort()
    print(a[n-1]-a[0])
    return

#C
def C():
    return

# D
# 解説AC
# BCDEのC,Dの仕切り位置を右に移動させていくと
# B,CとD,Eの仕切り位置について右にしか移動しないこと
# がわかれば終わりだった。
# わかりたい
def D():
    n = II()
    a = LI()
    for i in range(n - 1):
        a[i + 1] += a[i]
    l, r = 0, 0
    ans = inf
    for center in range(1, n - 2):
        r = max(r, center + 1)
        while center - l > 1:
            if abs(a[center] - 2 * a[l]) > abs(a[center] - 2 * a[l + 1]):
                l += 1
            else:
                break
        while n - 1 - r > 1:
            if abs(a[n - 1] - a[r] - (a[r] - a[center])) > abs(a[n - 1] - a[r + 1] - (a[r + 1] - a[center])):
                r += 1
            else:
                break
        b = a[l]
        c = a[center] - a[l]
        d = a[r] - a[center]
        e = a[n - 1] - a[r]
        ans = min(ans, max(b, c, d, e) - min(b, c, d, e))
    print(ans)

        
    return

#Solve
if __name__ == '__main__':
    D()
