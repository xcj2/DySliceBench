#!/usr/bin/env python3
from functools import lru_cache
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
    n = II()
    c = LI()
    c1, c2, c3 = [c.count(i) for i in range(1, 4)]
    d = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(c3 + 1):
        di = d[i]
        dim1 = d[i - 1]
        for j in range(c3 + c2 + 1 - i):
            dim1jp1 = dim1[j + 1]
            dijm1 = di[j - 1]
            dij = di[j]
            for k in range(c3 + c2 + c1 - i - j + 1):
                l = i + j + k
                if l == 0: continue
                res = n
                if i: res += i * dim1jp1[k]
                if j: res += j * dijm1[k + 1]
                if k: res += k * dij[k-1]
                dij[k] = res / l
    print(d[c3][c2][c1])
    return


#main
if __name__ == '__main__':
    solve()
