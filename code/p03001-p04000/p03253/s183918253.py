
from collections import defaultdict


def prime_factor(n):
    # O(sqrt(N))
    d = defaultdict(int)
    for i in range(2, n + 1):
        if i * i > n:
            break

        while n % i == 0:
            d[i] += 1
            n //= i

    if n != 1:
        d[n] += 1

    return d


MAX = 2 * 10 ** 5 + 10
MOD = 10 ** 9 + 7

# Factorial
fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1

# Inverse
inv = [0] * (MAX + 1)
inv[1] = 1

# Inverse factorial
finv = [0] * (MAX + 1)
finv[0] = 1
finv[1] = 1

for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, k):
    if n < k or k < 0:
        return 0
    return (fac[n] * finv[k] * finv[n - k]) % MOD


def comb_rep(n, k):
    return comb(n + k - 1, n - 1)


N, M = map(int, input().split())
primes = prime_factor(M)
res = 1
for k in primes.values():
    res *= comb_rep(N, k)
    res %= MOD

print(res)
