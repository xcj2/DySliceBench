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

def cmb(n, k):
    if k < 0 or k > n: return 0 
    return fact_N * fact_inv[k] % MOD * fact_inv[n-k] % MOD

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

U = N + 100 # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)
fact_N = fact[N]

for x in range(N+1):
    temp = K-A*x
    if temp%B != 0:
        continue
    y = temp // B
    if y > N:
        continue
    if y < 0:
        break
    answer += cmb(N, x) * cmb(N, y)
    answer %= MOD

print(answer % MOD)
