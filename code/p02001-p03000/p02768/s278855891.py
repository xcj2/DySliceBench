def comb(a, b, p=10 ** 9 + 7):
    if (b > a - b):
        return comb(a, a - b, p)
    c = d = 1
    for i in range(b):
        c *= (a - i)
        d *= (b - i)
        c %= p
        d %= p
    return c * modpow(d, p - 2, p) % p


def modpow(n, p, m=10 ** 9 + 7):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (modpow(n, p // 2, m) ** 2) % m
    return (modpow(n, p - 1, m) * n) % m


def resolve():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = modpow(2, n) - 1
    ans -= comb(n, a)
    ans -= comb(n, b)
    print(ans % mod)


if __name__ == '__main__':
    resolve()
