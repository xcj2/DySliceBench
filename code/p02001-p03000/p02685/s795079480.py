MOD = 998244353


def modinv(a):
    return pow(a, MOD - 2, MOD)


def make_tables(N):
    fac = [1, 1]
    inv = [1, 1]
    for i in range(2, N + 1):
        fac.append(fac[i - 1] * i % MOD)
        inv.append(modinv(fac[i]))
    return fac, inv


def ncr(n, r):
    return int(fac[n] * inv[r] * inv[n - r]) % MOD


if __name__ == '__main__':

    N, M, K = map(int, input().split())

    fac, inv = make_tables(N)

    ans = 0
    for k in range(K + 1):
        ans += (ncr(N - 1, k) * M * pow(M - 1, N - 1 - k, MOD)) % MOD

    print(ans % MOD)
