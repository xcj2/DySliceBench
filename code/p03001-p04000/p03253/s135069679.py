from collections import Counter


def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)


def combination(n, r, mod=10**9+7):
    """
    nCr mod m
    """
    if n < r:
        return 0
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n, m = map(int, input().split())
mod = 10**9+7

c = Counter(prime_factorize(m))

ans = 1
for v in c.values():
    ans *= combination(v+n-1, n-1)
    ans %= mod

print(ans)