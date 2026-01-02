import numpy as np
n, a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
MOD = 10**9 + 7
v = pow(2, n, MOD) - 1


def cumprod(arr, MOD):
    L = len(arr)
    Lsq = int(L**.5 + 1)
    arr = np.resize(arr, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n - 1]
        arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n - 1, -1]
        arr[n] %= MOD
    return arr.ravel()[:L]


def make_fact(U, MOD):
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), MOD - 2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv


# a / b = (a % N * pow(b, N - 2, N)) % N(mod=N)
fact, fact_inv = make_fact(2 * 10**5 + 1, MOD)
# print(fact)
a_fact = fact[a]
b_fact = fact[b]

n_fact = [n % MOD] * (b + 1)
for i in range(1, b + 1):
    n_fact[i] = (n_fact[i - 1] * (n - i)) % MOD
an_fact = n_fact[a - 1]
bn_fact = n_fact[b - 1]


def f(a, b, MOD):
    a, b = int(a), int(b)
    return (a % MOD * pow(b, MOD - 2, MOD)) % MOD


ca = f(an_fact, a_fact, MOD)
cb = f(bn_fact, b_fact, MOD)

print((v - ca - cb) % MOD)
