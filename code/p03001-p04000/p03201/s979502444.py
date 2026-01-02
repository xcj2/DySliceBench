#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    a = LI()
    a.sort()
    d = defaultdict(int)
    for ai in a:
        d[ai] += 1
    ans = 0
    for j in range(n - 1, -1, -1):
        i = 0
        aj = a[j]
        while aj:
            aj >>= 1
            i += 1
        m = 1 << i
        if d[a[j]]:
            if m - a[j] == a[j]:
                x = d[a[j]]
                d[a[j]] -= x
                ans += x // 2
            else:
                x = m - a[j]
                if bisect_right(a, x) - bisect_left(a, x) and d[x]:
                    x = d[a[j]]
                    y = d[m - a[j]]
                    d[a[j]] -= min(x, y)
                    d[m - a[j]] -= min(x, y)
                    ans += min(x, y)

    print(ans)

    return


#main
if __name__ == '__main__':
    solve()
