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
    d = LI()
    ans = 0
    q = [1]
    for i in range(n):
        q_ = []
        while q:
            p = q.pop()
            if not (1 << d[i]) & p:
                q_.append((1 << d[i]) | p)
            if not (1 << (24 - d[i])) & p:
                q_.append((1 << (24 - d[i])) | p)
        q = q_
    for qi in q:
        tmp = 25
        for i in range(25):
            for j in range(i + 1, 25):
                x = (1 << i) | (1 << j)
                if (qi & x) == x:
                    tmp = min(tmp, min(j - i, 24 - (j - i)))
        ans = max(ans, tmp)
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
