def ext_euc(a, b):
    if b == 0:
        return 1, 0, a
    y, x, v = ext_euc(b, a % b)
    y -= (a // b) * x
    return x, y, v


def mod_inv(a, mod):
    ret, _, _ = ext_euc(a, mod)
    return ret % mod


def main():
    MOD = 10 ** 9 + 7
    N, M = list(map(int, input().split(' ')))
    comb = [1 for _ in range(N + 1)]  # N_C_k
    perm_1 = [1 for _ in range(N + 1)]  # M_P_k
    perm_2 = [1 for _ in range(N + 1)]  # (M-k)_P_(N-k)
    for k in range(1, N + 1):
        c = comb[k - 1] * (N - k + 1) * mod_inv(k, MOD)
        c %= MOD
        comb[k] = c
        p = perm_1[k - 1] * (M - k + 1)
        p %= MOD
        perm_1[k] = p
        p = perm_2[k - 1] * (M - N + k)
        p %= MOD
        perm_2[k] = p
    perm_2.reverse()
    ans = 0
    for k in range(N + 1):
        v = (-1) ** (k % 2)
        v *= comb[k]
        v %= MOD
        v *= perm_1[k]
        v %= MOD
        v *= perm_2[k]
        v %= MOD
        v *= perm_2[k]
        v %= MOD
        ans += v
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()