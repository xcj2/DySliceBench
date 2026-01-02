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
    n = II()
    ans = 0
    N = int(sqrt(n))+2
    d = defaultdict(int)
    d[1] = 1 
    for i in range(2, int(sqrt(n - 1)) + 2):
        if d[i] == 0:
            x = i
            while 1:
                if n % x == 0 and d[x] != 1:
                    ans += 1
                    n //= x
                    d[x] = 1
                else:
                    break
                x *= i
            l = i
            j = 1
            while l < N:
                d[l] = 1
                j += 1
                l = i * j
    if d[n]:
        print(ans)
    else:
        print(ans + 1)
    return


#main
if __name__ == '__main__':
    solve()
