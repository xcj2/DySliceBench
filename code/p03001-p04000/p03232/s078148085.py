# -*- coding: utf-8 -*-
from sys import stdin
from itertools import accumulate

s_in = lambda: stdin.readline()[:-1] # s = s_in()
d_in = lambda: int(stdin.readline()) # N = d_in()
ds_in = lambda: list(map(int, stdin.readline().split())) # List = ds_in()

MOD = 10**9 + 7

N = d_in()
A_list = ds_in()

def factorial(N):
    val = 1
    for i in range(1, N+1):
        val = (val * i) % MOD
    return val

def recursive_square(n, m, p):
    """ n**p (mod m) """
    if p == 0:
        return 1 % m
    if p % 2 == 0:
        root = recursive_square(n, m, p//2) % m 
        return (root ** 2) % m
    else:
        return ((n % m) * recursive_square(n, m, p-1)) % m
        
def factorize(n):
    if n == 1:
        return [(1, 1)]
    fct = []
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n //= b
            e += 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

N_factorial = factorial(N)

Coefs = []
lastval = 0
Inv = dict()
for i in range(1, N+1):
    fac = factorize(i)
    temp = N_factorial
    for f in fac:
        if f[0] not in Inv.keys():
            Inv[f[0]] = recursive_square(f[0], MOD, MOD-2)
        for _ in range(f[1]):
            temp = (temp * Inv[f[0]]) % MOD
    lastval = (lastval + temp) % MOD
    Coefs.append(lastval)

if N == 1:
    print(A_list[0])
else: 
    ans = 0
    for i in range(N):
        ans = (ans + A_list[i] * (Coefs[i] + Coefs[N-i-1] - Coefs[0])) % MOD 
    print(ans)

