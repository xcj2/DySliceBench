# coding:utf-8

import sys


input = sys.stdin.readline
INF = float('inf')
MOD = 10 ** 9 + 7


def inpl(): return list(map(int, input().split()))


# aのp乗を求めるアルゴリズム
# MOD版
def pow_mod(a, p):
    if p == 0: return 1

    if p % 2 == 0:
        half_p = p // 2
        half = pow_mod(a, half_p)
        return half * half % MOD
    else:
        return a * pow_mod(a, p - 1) % MOD


def solve(N, A):
    # 1/1 + 1/2 + 1/3 + ... + 1/Nの累積和を求めておく
    inv_sum = [0]
    for i in range(N):
        inv_sum.append((inv_sum[-1] + pow_mod(i + 1, MOD - 2)) % MOD)
    del inv_sum[0]

    # 各iについて、Σ(j=1, N) 1/(|j - i| + 1)を求めて、
    # それらを係数としてA[i]に掛け、加算する
    ans = 0
    for i in range(N):
        ans += + A[i] * (inv_sum[N - 1 - i] + inv_sum[i] - 1)
        ans %= MOD

    # ansにN!を掛ける
    for i in range(N):
        ans *= (i + 1)
        ans %= MOD
    return ans


N = int(input())
A = inpl()
print(solve(N, A))
