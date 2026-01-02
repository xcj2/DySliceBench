from math import gcd

from collections import Counter
from itertools import product


min2 = lambda x,y: x if x < y else y


# 拡張ユークリッド互除法
# ax + by = gcd(a,b)の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def chinese_remainder_theorem(R, M, prod):
    """
    returns x s.t.
    all(x%m == r for r,m in zip(R,M))
    """
    s = 0
    for m,r in zip(M,R):
        p = prod//m
        s += r * p * modinv(p,m)
        s %= prod
    return s


# 素因数分解
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n



N = int(input())

factors = Counter(prime_factors(N))
if factors[2] > 0:
    factors[2] += 1
    N *= 2
mods = [f**p for f,p in factors.items()]

res = N
for R in product(*((0,m-1) for m in mods)):
    t = chinese_remainder_theorem(R, mods, N)
    if t > 0:
        res = min2(res, t)

print(res)