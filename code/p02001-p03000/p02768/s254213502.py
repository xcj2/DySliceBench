import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MAX = 2 * 10 ** 5 + 5
MOD = 10 ** 9 + 7

fac = [0 for i in range(MAX)]
finv = [0 for i in range(MAX)]
inv = [0 for i in range(MAX)]

def comInit(mod):
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

def com(mod, n, k):
    numerator = 1
    for i in range(1, k + 1):
        numerator *= (n - i + 1)
        numerator %= mod
    return (numerator * finv[k] % mod)
comInit(MOD)

n, a, b = map(int, readline().split())
nb = n

def my_pow(base, n, mod):
    if n == 0:
        return 1
    x = base
    y = 1
    while n > 1:
        if n % 2 == 0:
            x *= x
            n //= 2
        else:
            y *= x
            n -= 1
        x %= mod
        y %= mod
    return x * y % mod
ans = (my_pow(2, n, MOD) - 1) % MOD

print((ans - com(MOD, nb, a) - com(MOD, nb, b)) % MOD)