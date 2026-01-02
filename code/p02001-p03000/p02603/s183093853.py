#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIR_(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI_()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')

#solve
def solve():
    n = II()
    a = LI()
    ans = 1000
    have = 0
    state = 0
    for i in range(n - 1):
        if state == 0:
            if a[i] < a[i + 1]:
                have += ans // a[i]
                ans %= a[i]
                state = 1
        else:
            if a[i] > a[i + 1]:
                ans += a[i] * have
                have = 0
                state = 0
    ans += a[-1] * have
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
