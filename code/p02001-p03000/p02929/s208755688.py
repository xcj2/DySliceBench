# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7

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

U = 10 ** 6  # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)

# 最終形が白一色、逆再生、leftとrightで別に考える
N = ir()
S = sr()
cur = 'W'  # 左端に白があるとする
left = 0
right = 0
dic = {'W': 'B', 'B': 'W'}
answer = fact[N]
X = []
for s in S:
    if s == cur:
        right += 1
        cur = dic[s]
    else:
        left += 1
        remain = N - right
        X.append(remain)
        cur = s
    if right > left:
        print(0); exit()

if right != left:
    print(0); exit()

for i, x in enumerate(X[::-1]):
    answer *= (x - i)
    answer %= MOD

print(answer % MOD)
# 07