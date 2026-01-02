def ext_euler(a, b):
    # return (x, y, gcd(a, b)) s.t. ax + by = gcd(a, b)
    assert a > b
    if b == 0:
        return 1, 0, a
    y, x, v = ext_euler(b, a % b)
    y -= (a // b) * x
    return x, y, v


def mod_inv(a, mod):
    if a > mod:
        x, _, _ = ext_euler(a, mod)
    else:
        _, x, _ = ext_euler(mod, a)
    return x % mod


def mod_comb(n, k, mod):
    if k > n // 2:
        return mod_comb(n, n - k, mod)
    c = 1
    for i in range(k):
        c *= (n - i)
        c *= mod_inv(k - i, mod)
        c %= mod
    return c


def main():
    MOD = 10**9 + 7
    X, Y = list(map(int, input().split(' ')))
    if (2 * X - Y) % 3 != 0 or (- X + 2 * Y) % 3 != 0:
        print(0)
        exit(0)
    a = (2 * X - Y) // 3
    b = (- X + 2 * Y) // 3
    if a < 0 or b < 0:
        print(0)
        exit(0)
    print(mod_comb(a + b, b, MOD))


if __name__ == '__main__':
    main()