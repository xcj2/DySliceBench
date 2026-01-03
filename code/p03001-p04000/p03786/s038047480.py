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
    def f(x):
        tmp = a[x]
        for i in range(n):
            if i != x:
                if tmp * 2 >= a[i]:
                    tmp += a[i]
                else:
                    return False
        return True
    n = II()
    a = LI()
    a.sort()
    ok = n - 1
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(n - ok)
    return


#main
if __name__ == '__main__':
    solve()
