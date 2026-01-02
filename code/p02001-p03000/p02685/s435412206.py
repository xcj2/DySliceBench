import os

import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
# MOD = 10 ** 9 + 7
MOD = 998244353


def get_factorials(max, mod=None):
    """
    階乗 0!, 1!, 2!, ..., max!
    :param int max:
    :param int mod:
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
    逆元 0, 1/1, 1/2, 1/3, ..., 1/max
    :param int max:
    :param int mod:
    """
    invs = [1] * (max + 1)
    invs[0] = 0
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


def factorial_invs(max, mod):
    """
    階乗 0!, 1!, 2!, ..., max! の逆元
    :param int max:
    :param int mod:
    """
    ret = [1]
    r = 1
    for inv in mod_invs(max, mod)[1:]:
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

    def ncr(self, n, r):
        """
        :param int n:
        :param int r:
        :rtype: int
        """
        if n < r:
            return 0
        return self._factorials[n] * self._finvs[r] % self._mod * self._finvs[n - r] % self._mod


N, M, K = list(map(int, sys.stdin.buffer.readline().split()))

# dp[i][k]: i までみて、k 回同じ色になった
# dp = [[0] * (K + 2) for _ in range(N)]
# dp[0][0] = 1
# for i in range(N - 1):
#     for k in reversed(range(K + 1)):
#         # 同じ色
#         dp[i + 1][k + 1] += dp[i][k]
#         # 違う色
#         dp[i + 1][k] += dp[i][k] * (M - 1)
# print(np.array(dp))
# li = dp[-1][:K + 1]
# ans = sum(li) * M % MOD
# print(ans)
# print()

comb = Combination(max=max(N, M, K) + 100, mod=MOD)
ans = 0
for k in range(K + 1):
    ans += pow(M - 1, N - 1 - k, MOD) * comb.ncr(N - 1, k)
    ans %= MOD
print(ans * M % MOD)
