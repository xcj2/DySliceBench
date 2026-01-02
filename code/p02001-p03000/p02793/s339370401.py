#!/usr/bin/env python3

def prime_factor(n):
    ret, p = [], 2
    while p*p <= n:
        if n % p != 0:
            p += 1
            continue
        exp_v = 0
        while n%p == 0:
            exp_v += 1
            n //= p
        ret.append( [p, exp_v] )
        p += 1
    if n != 1: ret.append( [n, 1] )
    return ret


def extgcd(a, b):
    if b == 0:
        return [1, 0, a]
    x, y, g = extgcd(b, a%b)
    return [y, x - a//b * y, g]


def mod_inverse(a, m):
    x, y, _ = extgcd(a, m)
    return (m+x%m) % m


n = int(input())
a = [ int(x) for x in input().split() ]

MOD = 10**9 + 7

primes = {}
for aa in a:
    t = prime_factor(aa)
    for tt in t:
        v, e = tt
        primes[v] = max(e, primes.get(v, 0))

prod = 1
for k, v in primes.items():
    prod *= pow(k, v, MOD)
    prod %= MOD

ans = 0
for aa in a:
    ans += prod*mod_inverse(aa, MOD)
    ans %= MOD

print(ans%MOD)
