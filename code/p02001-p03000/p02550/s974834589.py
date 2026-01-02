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
inf = float("INF")

#solve
def solve():
    n, x, m = LI()
    if n <= 10 ** 5:
        ans = x
        for _ in range(n - 1):
            x = x ** 2 % m
            ans += x
        print(ans)
        return
    else:
        d = defaultdict(int)
        xd = x
        ans = 0
        for i in range(n + 1):
            if d[x]:
                break
            ans += x
            d[x] = (i + 1, ans)
            x = x ** 2 % m
        i += 1
        cycle = i - d[x][0]
        cycle_score = ans - d[x][1] + x
        n = n - d[x][0] + 1
        ans = d[x][1] - x
        diff = n % cycle
        tern = n // cycle
        ans += tern * cycle_score
        for j in range(diff):
            ans += x
            x = x ** 2 % m
        print(ans)
    return


#main
if __name__ == '__main__':
    solve()
