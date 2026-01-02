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
    if a <= 8 and b <= 8:
        print("Yay!")
    else:
        print(":(")
    return

#B
def B():
    d, n = LI()
    print(str(n * (n != 100) or n + 1) + "00" * d)
    return

#C
def C():
    II()
    ans = 0
    a = LI()
    for ai in a:
        while not ai % 2:
            ans += 1
            ai = ai // 2
    print(ans)
    return

#D
def D():
    n, m = LI()
    l = LIR(n)
    dp = [[-inf] * 8 for i in range(m+1)]
    for i in range(8):
        dp[0][i] = 0
    for i in range(n):
        for k in range(m, 0, -1):
            for x in range(8):
                t = 0
                for j in range(3):
                    t += l[i][j] if (x >> j) & 1 else -1 * l[i][j]
                dp[k][x] = max(dp[k][x], dp[k - 1][x] + t)
    print(max(dp[-1]))
    return

#Solve
if __name__ == '__main__':
    D()
