#!/usr/bin/env python3
X, Y = map(int, input().split())
if (X + Y) % 3:
    exit(print(0))
m = (2*X - Y) // 3
n = X - 2*m
if n < 0 or m < 0:
    exit(print(0))

## class
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def power(a, b, c):
    try:
        return pow(a, b, c)
    except (ValueError, TypeError) as e:
        if b < 0:
            return pow(modinv(a, c), -b, c)
        else:
            print(e)

class Factorial:
    def __init__(self, n, mod):
        self.f = f =[0] * (n + 1)
        f[0] = b = 1
        for i in range(1, n + 1):f[i] = b = b * i % mod
        self.inv = inv = [0] * (n + 1)
        inv[n] = b = power(self.f[n], -1, mod)
        for i in range(n,0,-1):inv[i-1] = b = b * i % mod
        self.mod = mod
    def factorial(self, i):
        return self.f[i]
    def ifactorial(self, i):
        return self.inv[i]
    def comb(self, n, k):
        if n >= k:return self.f[n] * self.inv[n - k] * self.inv[k] % self.mod
        else:return 0

def nCr(n, r, mod = None, limit = None):
    if mod and limit:
        return Factorial(limit, mod).comb(n, r)
    elif mod:
        r = min(r, n - r)
        a = 1
        for i in range(r):
            a = a * (n - i) * power(i + 1, mod - 2, mod) % mod
        return a
    else:
        from math import factorial as f
        return f(n) // (f(n - r) * f(r))

MOD = 10**9+7
print(nCr(m + n, n, MOD, 2*10**6))