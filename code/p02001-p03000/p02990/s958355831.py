import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

def cmb(n, k):
    if n < k: return 0
    return fact[n] * fact_inv[k] % MOD * fact_inv[n-k] % MOD

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

N, K = lr()
MOD = 10 ** 9 + 7
U = 2010 # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)
red = N-K
for i in range(1, K+1):
    # (red+1)Ci
    answer = cmb(red+1, i)
    #print(answer)
    remain = K - i
    # remainをiの中に自由にいれる、i-1の壁を用意
    # (remain+(i-1)) C remain
    answer *= cmb(remain+i-1, remain)
    print(answer%MOD)

# 15
