N, K = map(int, input().split())
MOD = 10 ** 9 + 7


# modしながらコンビネーションを求める
def mod_cmb(n, r, mod):
    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * mod_inverse(q, mod) % mod


# modしたa^bを求める
def mod_pow(a, p, mod):
    if p == 0:
        return 1
    elif p % 2 == 1:
        return a * mod_pow(a, p - 1, mod)
    else:
        return (mod_pow(a, p // 2, mod) % mod) ** 2 % mod


# aで割りたいときはa^(p-2)をかければよい（pは素数かつmodで使うやつ）
def mod_inverse(a, mod):
    return mod_pow(a, (mod - 2), mod)


def f(x, mod):
    if K - 1 < x - 1:
        return 0
    else:
        return mod_cmb(N - K + 1, x, mod) * mod_cmb(K - 1, x - 1, mod) % mod


for i in range(1, K + 1):
    print(f(i, MOD))