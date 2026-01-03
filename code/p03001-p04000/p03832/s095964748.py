import os
import sys

# import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353


def get_factorials(max, mod=None):
    """
    階乗 0!, 1!, 2!, ..., max!
    :param int max:
    :param int mod:
    :return:
    """
    ret = [1]
    n = 1
    if mod:
        for i in range(1, max + 1):
            n *= i
            n %= mod
            ret.append(n)
    else:
        for i in range(1, max + 1):
            n *= i
            ret.append(n)
    return ret


def mod_invs(max, mod):
    """
    逆元のリスト 0 から max まで
    :param int max:
    :param int mod:
    """
    invs = [1] * (max + 1)
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


def factorial_invs(max, mod):
    """
    階乗 0!, 1!, 2!, ..., max! の逆元
    :param int max:
    :param int mod:
    """
    ret = []
    r = 1
    for inv in mod_invs(max, mod):
        r = r * inv % mod
        ret.append(r)
    return ret


class Combination:
    def __init__(self, max, mod):
        """
        :param int max:
        :param int mod: 3 以上の素数であること
        """
        self._factorials = get_factorials(max, mod)
        self._finvs = factorial_invs(max, mod)
        self._mod = mod

    # @debug
    def ncr(self, n, r):
        """
        :param int n:
        :param int r:
        :rtype: int
        """
        if n < r:
            return 0
        return self._factorials[n] * self._finvs[r] % self._mod * self._finvs[n - r] % self._mod


N, A, B, C, D = list(map(int, sys.stdin.buffer.readline().split()))

comb = Combination(max=N + 1, mod=MOD)
# dp[u][i]: u 人のグループまでみて、合計 i 人のグループ分けをする方法の数
dp = [[0] * (N + 1) for _ in range(N + 1)]
for u in range(N + 1):
    dp[u][0] = 1
for unit in range(A, B + 1):
    for j in reversed(range(N + 1)):
        dp[unit][j] = dp[unit - 1][j]
        for cnt in range(C, D + 1):
            if j + unit * cnt > N:
                break
            # ((N-j)! / (N-j-unit*cnt)! / (unit!)^cnt) / cnt!
            ncr = comb._factorials[N - j] * comb._finvs[N - j - unit * cnt] % MOD * \
                  pow(comb._finvs[unit], cnt, MOD) % MOD * comb._finvs[cnt] % MOD
            dp[unit][j + unit * cnt] += dp[unit - 1][j] * ncr % MOD
            dp[unit][j + unit * cnt] %= MOD
# print(dp)
print(dp[B][N])
