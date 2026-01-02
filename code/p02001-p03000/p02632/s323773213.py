def pows(a, n, mod):
    # [a**0, a**1, ..., a**n] % mod
    ret = [1] * (n + 1)
    for i in range(1, n + 1):
        ret[i] = ret[i - 1] * a % mod
    return ret


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
    MOD = 10**9 + 7
    K = int(input())
    S = input()
    N = len(S)
    ans = 0
    pw25 = pows(25, K, MOD)
    pw26 = pows(26, K, MOD)
    comb = 1  # (k+N-1)_C_k
    for k in range(K + 1):
        ans += pw25[k] * comb * pw26[K - k]
        ans %= MOD
        comb *= k + N
        comb *= mod_inv(k + 1, MOD)
        comb %= MOD
    print(ans)


if __name__ == '__main__':
    main()