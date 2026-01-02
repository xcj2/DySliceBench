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
def LS(): return input().rstrip().split()
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
    def f0(x):
        for td_ in td:
            if td_[0] == s[x]:
                if td_[1] == "L":
                    x -= 1
                else:
                    x += 1
            if x < 0:
                return True
            if x >= n:
                return False
        return False
    def f1(x):
        for td_ in td:
            if td_[0] == s[x]:
                if td_[1] == "L":
                    x -= 1
                else:
                    x += 1
            if x >= n:
                return True
            if x < 0:
                return False
        return False

    n, q = LI()
    s = S()
    td = LSR(q)
    ok = -1
    ng = n
    ans = n
    while ng - ok > 1:
        mid = (ng - ok) // 2 + ok
        if f0(mid):
            ok = mid
        else:
            ng = mid
    ans -= ok  + 1
    ok = n
    ng = -1
    while ok - ng > 1:
        mid = (ok - ng) // 2 + ng
        if f1(mid):
            ok = mid
        else:
            ng = mid
    ans -= n - ok
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
