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
    a, b, c = LI()
    ans = 10 ** 5
    ans = min(ans, abs(a - b) + abs(b - c))
    ans = min(ans, abs(a - c) + abs(b - c))
    ans = min(ans, abs(a - c) + abs(a - b))
    print(ans)
    return

#B
def B():
    s, t = S(), S()
    f = 0
    for i in range(len(s)):
        f = f or s[i:] + s[:i] == t
    print(["No","Yes"][f])
    return

#C
def C():
    return

# D
# 解説AC
# 貪欲かよ
# 言われればその通りでbi昇順でソートしていれば
# 直前で取り除いたものに関してはその橋より左側
# の街について絶対に橋が途切れているからね
# fuck!!! 
def D():
    n, m = LI()
    d = defaultdict(int)
    for _ in range(m):
        a, b = LI_()
        d[a] = max(d[a], n-b)
    mi = 0
    ans = 0
    for i in range(n - 1):
        if mi < d[i]:
            mi = d[i]
        if i == n - mi - 1:
            mi = 0
            ans += 1
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
