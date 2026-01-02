#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N, K = list(map(int, input().split()))
max_i = min(K, N - K + 1)

MAX = N * 2
PRIME = 10 ** 9 + 7

fac = [0] * MAX
finv = [0] * MAX


def invMod(a, m):
    a %= m
    b, x, y = m, 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        x -= t * y
        x, y = y, x
    return x % m


def binomInit():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    for i in range(2, MAX):
        fac[i] = (fac[i - 1] * i) % PRIME
        finv[i] = (finv[i - 1] * invMod(i, PRIME)) % PRIME
        

def binom(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return (fac[n] * finv[k] * finv[n - k]) % PRIME


binomInit()
    

for i in range(1, K + 1):
    blue_part = binom(K - 1, i - 1)
    red_part = binom(N - K + 1, i)
    print((blue_part * red_part) % PRIME)
