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
inf = float('INF')


def cmb(n, k):
    # print(n,k)
    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = factorial(n)
    b = factorial(k)
    c = factorial(n - k)
    return a // b // c

def dfs(i, k, lenn, sn):
    if k == 0:
        return 1
    if i == lenn:
        return 0
    if sn[i] == "0":
        return dfs(i + 1, k, lenn, sn)
    return cmb(lenn - i - 1, k) * 9 ** k + cmb(lenn - i - 1, k - 1) * 9 ** (k - 1) * (int(sn[i]) - 1) + dfs(i + 1, k - 1, lenn, sn)

#solve
def solve():
    n, k = IR(2)
    lenn = len(str(n))
    sn = str(n)
    ans = dfs(0,k,lenn,sn)
    print(int(ans))
    return


#main
if __name__ == '__main__':
    solve()
