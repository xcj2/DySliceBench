def ext_euc(a, b):
    if b == 0:
        return 1, 0, a
    y, x, v = ext_euc(b, a % b)
    y -= (a // b) * x
    return x, y, v


def mod_inv(a, mod):
    x, _, _ = ext_euc(a, mod)
    return x % mod


def main():
    MOD = 10 ** 9 + 7
    N, K = list(map(int, input().split()))
    c = [1, 1]  # comb(N, n), comb(N - 1, n)
    ans = 0
    for n in range(min(N - 1, K) + 1):
        ans += c[0] * c[1]
        ans %= MOD
        n_inv = mod_inv(n + 1, MOD)
        c[0] *= N - n
        c[0] *= n_inv
        c[0] %= MOD
        c[1] *= N - 1 - n
        c[1] *= n_inv
        c[1] %= MOD
    print(ans)


if __name__ == '__main__':
    main()