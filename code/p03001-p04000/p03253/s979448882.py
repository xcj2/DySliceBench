# -*- coding: utf-8 -*-
from sys import stdin
import math

s_in = lambda: stdin.readline()[:-1] # s = s_in()
d_in = lambda: int(stdin.readline()) # N = d_in()
ds_in = lambda: list(map(int, stdin.readline().split())) # List = ds_in()

N, M = ds_in()
MOD = 10**9 + 7

def factorize(n):
    if n == 1:
        return []
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

fct = factorize(M)

def recursive_square(n, m, p):
    """ n**p (mod m) """
    if p == 0:
        return 1 % m
    if p % 2 == 0:
        root = recursive_square(n, m, p//2) % m 
        return (root ** 2) % m
    else:
        return ((n % m) * recursive_square(n, m, p-1)) % m

Inv = dict([[1,1]]) # 逆元

# 組み合わせ
def combination(n, r):
    val = 1
    for i in range(1, r+1):
        if i not in Inv.keys():
            Inv[i] = recursive_square(i, MOD, MOD-2)
        val = (((val * (n-i+1)) % MOD) * Inv[i]) % MOD
    return val

ans = 1
for f in fct:
    ans = (ans * combination(N-1+f[1], f[1])) % MOD
print(ans)


