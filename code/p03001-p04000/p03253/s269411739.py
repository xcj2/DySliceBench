# -*- coding: utf-8 -*-
import heapq
import itertools
import math
from collections import defaultdict

def factorization(m, flag=0):
    m0 = m
    hq = []
    F = defaultdict(int)
    for n in itertools.count(2) if flag else range(2,math.ceil(math.sqrt(m))+5):

        while hq and hq[0][0] == n:
            heapq.heapreplace(hq,(sum(hq[0]),hq[0][1]))
            if hq[0][0] > n:break
        else:
            while m > 1:
                if m%n:
                    break
                else:
                    m //= n
                    F[n] += 1
            hq.append((n*n,n))
            if m == 1:
                return F
    if not F or m > 1:
        F[m] += 1
    return F


def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n;

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p;
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def solve():
    N, M = map(int, input().split())
    F = factorization(M)
    res = 1
    for n in F.values():
        res *= cmb(N+n-1, n)
    res %= (10**9+7)
    return str(res)

if __name__ == '__main__':
    print(solve())

