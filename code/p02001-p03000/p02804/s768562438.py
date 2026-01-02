import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7

# 組合せ nCr (MOD) 逆元を使う方法
def perm(n,k):
    if k > n or k < 0: return 0
    return fact[n] * fact_inv[n-k] % MOD

def cmb(n, k):
    if k < 0 or k > n: return 0 
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

U = 10 ** 5 + 100 # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)
N, K = lr()
A = np.array(lr())
A.sort()
if K == 1:
    print(0); exit()
coef = np.zeros(N, np.int64)
coef[K-1:] = [cmb(n, K-1) for n in range(K-1, N)]
answer = (A * coef % MOD).sum() % MOD
coef = np.zeros(N, np.int64)
coef[:-K+1] = [cmb(n, K-1) for n in range(N-1, K-2, -1)]
answer -= (A * coef % MOD).sum() % MOD
print(answer%MOD)
# 53