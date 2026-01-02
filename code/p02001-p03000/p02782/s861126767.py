r1, c1, r2, c2 = list(map(int, input().split()))

MOD = 10 ** 9 + 7


def modInverse(x, p):
    # Fermat's little theorem
    return pow(x, p - 2, p)


def nCr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return num * modInverse(den, p) % p


def hockey(n, m):
    # sum i=0 to m of nCr(n + i, i) == nCr(n + m + 1, m)
    return nCr(n + m + 1, m, MOD)


tot1 = hockey(c2, r2 + 1) - hockey(c2, r1)
tot2 = hockey(c1 - 1, r2 + 1) - hockey(c1 - 1, r1)
print((tot1 - tot2) % MOD)
