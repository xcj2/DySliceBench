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
    a, b = LI()
    print((a-1)*(b-1))
    return

#B
def B():
    def est(n):
        res = 0
        for i in range(1, int(n ** 0.5) + 1):
            if not n % i:
                res += 2
        res -= float.is_integer(n ** 0.5)
        return res == 8
    n = II()
    ans = 0
    for i in range(1, n + 1, 2):
        ans += est(i)
    print(ans)
    return

#C
def C():
    s = S()
    k = II()
    for i in range(k):
        if s[i] != "1":
            print(s[i])
            return
    print(s[k-1])
    return

# D
# 解説AC
# 始点と終点を2次元座標に落とし込むことで解ける
# 難しい
def D():
    n, m, q = LI()
    c = [[0] * n for i in range(n)]
    for _ in range(m):
        l, r = LI_()
        c[r][l] += 1
    for y in range(n):
        for x in range(1, n):
            c[y][x] += c[y][x - 1]
    for _ in range(q):
        p, q = LI_()
        ans = 0
        for qi in range(p, q + 1):
            ans += c[qi][q] - (c[qi][p - 1] if p != 0 else 0)
        print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
