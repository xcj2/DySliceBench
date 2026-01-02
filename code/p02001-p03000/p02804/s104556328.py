MOD = 10 ** 9 + 7

def ncr(n, r, mod=MOD):
    return (fct[n] * invf[r] * invf[n - r]) % mod


def make_tables(n, mod=MOD):
    fct = [1 for _ in range(n + 1)]
    invf = [1 for _ in range(n + 1)]

    for i in range(2, n + 1):
        fct[i] = (fct[i - 1] * i) % mod
        invf[i] = divmod(fct[i])
    return fct, invf


def divmod(a, mod=MOD):
    return pow(a, mod - 2, mod)


N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
for i in range(N):
    A[i] %= MOD

fct, invf = make_tables(N, mod=MOD)

ans = 0
for i in range(N - K + 1):
    ans += ((A[-1-i] - A[i]) % MOD * ncr(N - i - 1, K - 1)) % MOD
print(ans % MOD)