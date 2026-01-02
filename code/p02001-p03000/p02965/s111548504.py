import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 998244353

N, M = list(map(int, sys.stdin.readline().split()))


def get_factorials(max, mod=None):
    """
    階乗 0!, 1!, 2!, ..., max!
    :param int max:
    :param int mod:
    :return:
    """
    ret = np.ones(max + 1, dtype=int)
    n = 1
    for i in range(1, max + 1):
        n *= i
        n %= mod
        ret[i] = n
    return ret


def mod_invs(max, mod):
    """
    逆元のリスト 0 から max まで
    :param max:
    :param mod:
    :return:
    """
    invs = [1] * (max + 1)
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


factorials = get_factorials(M * 3 // 2 + N, MOD)
finvs = np.ones(M * 3 // 2 + N + 1, dtype=int)
p = 1
for i, inv in enumerate(mod_invs(M * 3 // 2 + N, MOD)):
    p = p * inv % MOD
    finvs[i] = p


def ncr(n, r, mod=None):
    """
    scipy.misc.comb または scipy.special.comb と同じ
    組み合わせの数 nCr
    """
    ret = factorials[n] * finvs[r] % MOD * finvs[n - r] % mod
    ret[n < r] = 0
    return ret


# (1) 合計が M*3 で、奇数の数が M 以下である数列の数
odds = np.arange(M % 2, M + 1, 2)
halves1 = (M * 3 - odds) // 2
# 合計が halfs の数列を 2 倍して、odds 個選んで 1 を足す
c1 = ncr(halves1 + N - 1, N - 1, MOD) * ncr(N, odds, MOD) % MOD

# (2) max が M*2 より大きく、奇数の数が M 以下である数列の数
# => 合計が M で、1 要素目が 0 より大きい、奇数が M 以下である数列の数 * N
# 1 要素目に M*2 を足せば (2) になる
halves2 = (M - odds) // 2
# a. 合計が M で奇数が M 以下
c2a = ncr(halves2 + N - 1, N - 1, MOD) * ncr(N, odds, MOD) % MOD
# b. 1 要素目が 0 である数列の数
c2b = ncr(halves2 + N - 2, N - 2, MOD) * ncr(N - 1, odds, MOD) % MOD

c2 = (c2a - c2b) * N % MOD

print((c1 - c2).sum() % MOD)
