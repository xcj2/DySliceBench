import sys
sys.setrecursionlimit(10**5)
# from collections import defaultdict

geta = lambda fn: list(map(fn, input().split()))


def egcd(a: int, b: int):
    """
    A solution of ax+by=gcd(a,b). Returns
    (gcd(a,b), (x, y)).
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def modinv(a: int, m: int):
    """
    Returns a^{-1} modulo m.
    """
    g, x, y = egcd(a, m)
    if g > 1:
        raise Exception('{}^(-1) mod {} does not exist.'.format(a, m))
    else:
        return x % m


def modpow(a: int, n: int, m: int):
    """
    Returns a^n mod m. (-inf < n < inf)
    """
    if a in [-1, 0, 1]:
        if a == -1:
            return 1 if n & 1 == 0 else m - 1
        else:
            return a

    x, k = (a % m, n) if n >= 0 else (modinv(a, m), -n)

    ret = 1
    while k > 0:
        if k & 1 == 1:
            ret = ret * x % m
        x *= x
        k = k >> 1

    return ret


mod = 998244353

N, M, K = geta(int)

if M == 1:
    print(0 if K < N - 1 else 1)
    exit()

a = M * modpow(M - 1, N - 1, mod) % mod
ans, k = a, 1
mi = modinv(M - 1, mod)

for k in range(1, K + 1):
    a = a * (N - k) * mi * modinv(k, mod) % mod
    ans = (ans + a) % mod

print(ans)
