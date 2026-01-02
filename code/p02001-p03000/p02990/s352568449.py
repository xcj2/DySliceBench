import sys
input = sys.stdin.readline

P = 10**9 + 7


def make_fac_tables_mod_p(n, p):
    fac = [0] * (n + 1)
    fac_inv = [0] * (n + 1)
    mod_inv = [0] * (n + 1)
    fac[0] = fac[1] = 1
    fac_inv[0] = fac_inv[1] = 1
    mod_inv[1] = 1
    for i in range(2, n + 1):
        fac[i] = (fac[i - 1] * i) % p
        mod_inv[i] = p - mod_inv[p % i] * (p // i) % p
        fac_inv[i] = fac_inv[i - 1] * mod_inv[i] % p
    return fac, fac_inv


def nCk_mod_p(fac, fac_inv, n, k, p):
    return ((fac[n] * fac_inv[n - k]) % p) * fac_inv[k] % p


def main():
    N, K = map(int, input().split())

    R = N - K
    fac, fac_inv = make_fac_tables_mod_p(max(R + 1, K - 1), P)
    for i in range(1, K + 1):
        if i > R + 1:
            print(0)
        else:
            a = nCk_mod_p(fac, fac_inv, R + 1, i, P)
            b = nCk_mod_p(fac, fac_inv, K - 1, K - i, P)
            ans = a * b % P
            print(ans)


if __name__ == "__main__":
    main()
