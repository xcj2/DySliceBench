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
    ab = LIR(n)
    d = defaultdict(int)
    d2 = defaultdict(int)
    d3 = defaultdict(int)
    aa = 0
    for a, b in ab:
        if a == b == 0:
            aa += 1
            continue
        if a == 0:
            d[0] += 1
            d3[0] = 1
        elif b == 0:
            d2[0] += 1
            d3[0] = 1
        else:
            if a * b > 0:
                x = math.gcd(a, b)
                a //= x
                b //= x
                d[(abs(a) , abs(b))] += 1
                d3[(abs(a) , abs(b))] = 1
            else:
                x = math.gcd(a, b)
                a //= x
                b //= x
                d2[(abs(b), abs(a))] += 1
                d3[(abs(b), abs(a))] = 1
    ans = 1
    for k in d3.keys():
        ans *= (2 ** d[k] + 2 ** d2[k] - 1)
        ans %= mod
    ans -= 1
    ans += aa
    print(ans % mod)
    return


#main
if __name__ == '__main__':
    solve()
