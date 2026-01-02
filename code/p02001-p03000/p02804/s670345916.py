import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
A = lr()
A.sort()

MOD = 10 ** 9 + 7
if K == 1:
    print(0)
    exit()


def cmb(n, k):
    # nCkを計算する
    k = min(k, n-k)
    return fac[n] * ifac[k] % MOD * ifac[n-k] % MOD

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

fac, ifac = make_fact(10**6, MOD)
answer = 0
for i in range(K-1, N):
    # 最大値として何回登場するか、A[i] * i C (K-1)
    answer += A[i] * cmb(i, K-1)
    answer %= MOD

for i in range(N-K+1):
    # A[i] * (N-(i+1)) C (k-1)
    answer -= A[i] * cmb(N-(i+1), K-1)
    answer %= MOD

print(answer % MOD)
# 51