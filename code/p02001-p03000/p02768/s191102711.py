def modPow(a, n, mod):
    if n == 1:
        return a
    if n % 2 == 1:
        return (a * (modPow(a, n//2, mod) ** 2)) % mod
    else:
        return (modPow(a, n//2, mod) ** 2) % mod


def modInverse(a, p):
    # calculates the modular multiplicative of a mod m.
    # (assuming p is prime).
    return modPow(a, p-2, p)


def modBinomial(n, k, p):
    # calculates C(n,k) mod p (assuming p is prime).

    numerator = 1  # n * (n-1) * ... * (n-k+1)
    for i in range(k):
        numerator = (numerator * (n-i)) % p

    denominator = 1  # k!
    for i in range(1, k+1):
        denominator = (denominator * i) % p

    # numerator / denominator mod p.
    return (numerator * modInverse(denominator, p)) % p


mod = 10 ** 9 + 7
n, a, b = map(int, input().split())

nn = modPow(2, n, mod)
nn = (nn+mod-1) % mod


ab = (modBinomial(n, a, mod) + modBinomial(n, b, mod)) % mod

ans = (nn-ab+mod) % mod

print(ans)
