MOD = 10 ** 9 + 7


def make_table_mod(n, mod=10 ** 9 + 7):
    fct = [1, 1]
    inv = [1, 1]

    for i in range(2, n + 1):
        fct.append((fct[i-1] * i) % MOD)
        inv.append(divmod(fct[i]))
    return fct, inv


def divmod(n, p=10**9+7):
    return pow(n, p-2, p)


def ncr(n, r, mod=10**9+7):
    return (fct[n] * inv[r] * inv[n-r]) % mod

N, K = map(int, input().split())
fct, inv = make_table_mod(N)
for i in range(1, K + 1):
    if N - K + 1 < i:
        print(0)
    else:
        print((ncr(N - K + 1, i) * ncr(K - 1, i - 1)) % MOD)
