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
def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass

#solve
def solve():
    n = II()
    a = LI()
    x = 1
    if 1 in a:
        x = 0
    a = [i for i in a if i != 1]
    M = 10 ** 6 + 1
    p = [True] * M
    p[0] = False
    p[1] = False
    d = [-1] * M
    for xi in range(2, M):
        if p[xi]:
            d[xi] = xi
            for i in range(xi * 2, M, xi):
                p[i] = False
                if d[i] == -1:
                    d[i] = xi
    res = defaultdict(int)
    flg = 0
    for ai in a:
        tmp = []
        if d[ai] == -1:
            res[ai] = 1
            tmp = [ai]
        else:
            while d[ai] != -1:
                tmp.append(d[ai])
                ai = ai // d[ai]
        for t in set(tmp):
            if res[t]:
                flg = 1
            res[t] = 1
        if flg:
            break
    else:
        print("pairwise coprime")
        return
    g = a[0]
    for i in a:
        g = math.gcd(g, i)
    if g == 1 or x == 0:
        print("setwise coprime")
        return
    print("not coprime")
    
    return


#main
if __name__ == '__main__':
    solve()
