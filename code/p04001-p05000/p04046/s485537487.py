H, W, A, B = map(int, input().split())
MOD = 10 ** 9 + 7
limit = 2 * 10 ** 5


# modしながらコンビネーションを求める
def mod_cmb(n, r, mod):
    x = fact[n] * fact_inverse[r] % mod
    x = x * fact_inverse[n - r] % mod
    return x


def d_cmb(n, r, mod):
    return mod_cmb(n + r - 1, r, mod)


# modしたa^bを求める
def mod_pow(a, p, mod):
    if p == 0:
        return 1
    elif p % 2 == 1:
        return a * mod_pow(a, p - 1, mod)
    else:
        return (mod_pow(a, p // 2, mod) % mod) ** 2 % mod


fact = [1] * (limit + 1)
fact_inverse = [1] * (limit + 1)

for i in range(1, limit + 1):
    fact[i] = fact[i - 1] * i % MOD

fact_inverse[limit] = mod_pow(fact[limit], MOD - 2, MOD)
for i in reversed(range(1, limit + 1)):
    fact_inverse[i - 1] = fact_inverse[i] * i % MOD

n1 = W
r1 = H - A - 1
n2 = 1
r2 = A - 1
ans = 0
for i in range(W - B):
    ans += d_cmb(n1 - i, r1, MOD) * d_cmb(n2 + i, r2, MOD)
    ans %= MOD

print(ans)