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
    S = int(input())
    length = 1
    ans = 0
    comb = 1 # (S-2*l-1)_C_(l-1)
    while 3 * length <= S:
        ans += comb
        comb *= (S-3*length)*(S-3*length-1)*(S-3*length-2)
        comb %= MOD
        comb *= mod_inv(length, MOD) * mod_inv(S-2*length-1, MOD) * mod_inv(S-2*length-2, MOD)
        comb %= MOD
        length += 1
    print(ans % MOD)


if __name__ == '__main__':
    main()