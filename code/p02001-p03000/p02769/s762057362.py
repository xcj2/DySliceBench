import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

# Wrong Answer
# WA


N, K = map(int, input().split())
MOD = 10 ** 9 + 7

# 階乗、Combinationコンビネーション(numpyを使う)


def cumprod(arr, MOD):
    L = len(arr)
    Lsq = int(L**.5+1)
    arr = np.resize(arr, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n-1]
        arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n-1, -1]
        arr[n] %= MOD
    return arr.ravel()[:L]


def make_fact(U, MOD):
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv


U = 10**6
fact, fact_inv = make_fact(U, MOD)


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod


ans = 0
for i in range(N):
    if K < i:
        continue

    if N - 1 <= K:
        ans = mod_comb_k(N + N - 1, N - 1, MOD)
        break

    if i == 0:
        ans += 1
        continue

    '''
    a = mod_comb_k(N - 1, i, MOD)
    b = mod_comb_k(N, i, MOD)
    c = a * b
    c %= MOD
    '''
    a = mod_comb_k(N - 1, i, MOD)
    b = mod_comb_k(N, i, MOD)
    c = a * b % MOD
    ans += c
    ans %= MOD

print(ans)
