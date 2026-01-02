def pow_mod(a, b, p):
    res = 1
    mul = a
    for i in range(len(bin(b)) - 2):
        if (1 << i) & b:
            res = (res * mul) % p
        mul = (mul ** 2) % p
    return res


def perm_mod(n, r, p):
    res = 1
    for i in range(r):
        res = (res * (n - i)) % p
    return res


def comb_mod(n, r, p):
    r = min(r, n - r)
    return (perm_mod(n, r, p) * pow_mod(perm_mod(r, r, p), p - 2, p)) % p


def main():
    p = 10 ** 9 + 7
    n, a, b = map(int, input().split())
    print((pow_mod(2, n, p) - 1 - comb_mod(n, a, p) - comb_mod(n, b, p)) % p)


main()
