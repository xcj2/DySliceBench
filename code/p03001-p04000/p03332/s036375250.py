# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 998244353
N, A, B, K = lr()
answer = 0
# A * x + B * y = K
# nCx * nCy

def F(x, y):
    return comb[x] * comb[y]

def cumprod(arr, MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n-1]; arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n-1, -1]; arr[n] %= MOD
    return arr.ravel()[:L]

def make_fact(U, MOD):
    x = np.arange(U, dtype=np.int64); x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64); x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv

U = N + 1 # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)
fact_N = fact[N]
comb = fact_N * fact_inv % MOD * fact_inv[::-1] % MOD

for x in range(N+1):
    temp = K-A*x
    q, r = divmod(temp, B)
    if r != 0:
        continue
    if q > N:
        continue
    if q < 0:
        break
    answer += F(x, q)
    answer %= MOD

print(answer % MOD)
