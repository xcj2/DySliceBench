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
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
    n, m = LI()
    a = LI()
    a.sort()
    if len(a) != len(set(a)):
        print(0)
        return
    b = LI()
    b.sort()
    if len(b) != len(set(b)):
        print(0)
        return
    ans = 1
    for i in range(n * m, 0, -1):
        x = bisect_left(a, i)
        y = bisect_left(b, i)
        if x == n or y == m:
            print(0)
            return
        ansx = 1 if a[x] == i else n - x 
        ansy = 1 if b[y] == i else m - y
        f = a[x] == i or b[y] == i
        ans *= (ansx * ansy - (n * m - i if not f else 0)) % mod
        ans %= mod
    print(ans)

    return


#main
if __name__ == '__main__':
    solve()
