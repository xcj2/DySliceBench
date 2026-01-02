import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 998244353


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

    def ncr(self, n, r):
        """
        :param int n:
        :param int r:
        :rtype: int
        """
        if n < r:
            return 0
        return self._factorials[n] * self._finvs[r] % self._mod * self._finvs[n - r] % self._mod


N, A, B, K = list(map(int, sys.stdin.readline().split()))
comb = Combination(max=N, mod=MOD)
# ans = 0
# # A の数が決まれば B の数も決まる
# for a in range(N + 1):
#     if (K - a * A) % B != 0:
#         continue
#     b = int((K - a * A) // B)
#     if not (0 <= a <= N and 0 <= b <= N):
#         continue
#
#     s = 0
#     # 緑
#     c = min(a, b)
#     # A
#     a -= c
#     # B
#     b -= c
#     # 無色
#     d = N - a - b - c
#     # ここ高速化したい
#     while c >= 0 and d >= 0:
#         s += comb.ncr(N, a) * comb.ncr(N - a, b) * comb.ncr(N - a - b, c)
#         a += 1
#         b += 1
#         c -= 1
#         d -= 1
#
#     ans += s
#     ans %= MOD
# print(ans)


# # dp[i, a, b]: i番目までで、残り使うべき A が a 個、B が b 個残ってるパターン数
# dp = np.zeros((N + 1, N + 1, N + 1), dtype=int)
#
# # A の数が決まれば B の数も決まる
# for a in range(N + 1):
#     if (K - a * A) % B != 0:
#         continue
#     b = int((K - a * A) // B)
#     if not (0 <= a <= N and 0 <= b <= N):
#         continue
#     dp[0][a][b] += 1
#
# for i in range(1, N + 1):
#     dp[i] += dp[i - 1]
#     dp[i, :-1] += dp[i - 1, 1:]
#     dp[i, :, :-1] += dp[i - 1, :, 1:]
#     dp[i, :-1, :-1] += dp[i - 1, 1:, 1:]
# print(dp)
# print(dp[-1][0][0])


# 未証明、DP テーブル見た
ans = 0
for a in range(N + 1):
    if (K - a * A) % B != 0:
        continue
    b = int((K - a * A) // B)
    if not (0 <= a <= N and 0 <= b <= N):
        continue
    ans += comb.ncr(N, a) * comb.ncr(N, b)
    ans %= MOD
print(ans)
