import math
import sys

sys.setrecursionlimit(10000)
INF = float('inf')


def ncr(n, r, mod=None):
    """
    scipy.misc.comb または scipy.special.comb と同じ
    組み合わせの数 nCr
    :param int n:
    :param int r:
    :param int mod: 3 以上の素数であること
    :rtype: int
    """
    assert n >= r

    def inv(a):
        """
        a の逆元
        :param a:
        :return:
        """
        return pow(a, mod - 2, mod)

    if mod:
        return math.factorial(n) * inv(math.factorial(r)) * inv(math.factorial(n - r)) % mod
    else:
        return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


N, M, K = list(map(int, input().split()))


def pyramid(n):
    return n * (n + 1) * (n + 2) // 6


MOD = 10 ** 9 + 7

# K == 2 の場合
k2 = (pyramid(N - 1) * M ** 2 + pyramid(M - 1) * N ** 2) % MOD
# k2 を何回使うか
c = ncr(N * M - 2, K - 2, mod=MOD)
print(k2 * c % MOD)
