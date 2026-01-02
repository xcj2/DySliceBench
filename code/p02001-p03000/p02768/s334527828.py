def calc_pow(a, n, mod):
    rev_bin_n_str = bin(n)[2:][::-1]
    val = 1
    base_a = a
    for b in rev_bin_n_str:
        if b == '1':
            val *= base_a
            val %= mod
        base_a *= base_a
        base_a %= mod
    return val


def ext_euc(a, b):
    # return (x, y, gcd(a, b)) such that ax + by = gcd(a, b)
    # assumed a > b
    if b == 0:
        return 1, 0, a
    y, x, v = ext_euc(b, a % b)
    y -= (a // b) * x
    return x, y, v


def mod_inv(a, mod):
    if a > mod:
        x, _, _ = ext_euc(a, mod)
    else:
        _, x, _ = ext_euc(mod, a)
    return x % mod


def calc_comb(n, k, mod):
    if k > n / 2:
        return calc_comb(n, n - k, mod)
    comb = 1
    for i in range(k):
        comb *= (n - i)
        comb %= mod
        comb *= mod_inv((k - i), mod)
        comb %= mod
    return comb


def main():
    MOD = 10**9 + 7
    n, a, b = list(map(int, input().split(' ')))
    ans = calc_pow(2, n, MOD) - calc_comb(n, a, MOD) - calc_comb(n, b, MOD) - 1
    print(ans % MOD)


if __name__ == '__main__':
    main()