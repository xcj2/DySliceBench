import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces

# 大きい数用


def modPow(a, n, p):
    if n == 1:
        return a
    if n % 2 == 1:
        return (a * (modPow(a, n // 2, p) ** 2)) % p
    else:
        return (modPow(a, n // 2, p) ** 2) % p


def modInverse(a, p):
    # calculates the modular multiplicative of a mod m.
    # (assuming p is prime).
    return modPow(a, p - 2, p)


def modBinomial(n, k, p):
    # calculates C(n,k) mod p (assuming p is prime).

    numerator = 1  # n * (n-1) * ... * (n-k+1)
    for i in range(k):
        numerator = (numerator * (n - i)) % p

    denominator = 1  # k!
    for i in range(1, k + 1):
        denominator = (denominator * i) % p

    # numerator / denominator mod p.
    return (numerator * modInverse(denominator, p)) % p


r1, c1, r2, c2 = na()
mod = 10 ** 9 + 7
print((modBinomial(r2 + c2 + 2, r2 + 1, mod) + modBinomial(r1 + c1, r1, mod) -
       modBinomial(r1 + c2 + 1, r1, mod) - modBinomial(r2 + c1 + 1, c1, mod)) % mod)
