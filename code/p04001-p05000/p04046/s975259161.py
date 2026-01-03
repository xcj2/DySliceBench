import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

H, W, A, B = list(map(int, sys.stdin.readline().split()))


# dp = np.ones(W, dtype=int)
# for h in range(1, H - A):
#     dp = dp.cumsum() % MOD
# for h in range(H - A, H):
#     dp[B:] = dp[B:].cumsum() % MOD
# print(dp[-1])


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

def mod_inv(a, mod):
    """
    a の逆元
    :param int a:
    :param int mod:
    :return:
    """
    return pow(a, mod - 2, mod)


factorials = get_factorials(H + W, MOD)


def ncr(n, r, mod=None):
    """
    scipy.misc.comb または scipy.special.comb と同じ
    組み合わせの数 nCr
    :param int n:
    :param int r:
    :param int mod: 3 以上の素数であること
    :rtype: int
    """
    if n < r:
        return 0

    return factorials[n] * mod_inv(factorials[r], mod) * mod_inv(factorials[n - r], mod) % mod


ans = 0
for i in range(W - B):
    ans += ncr((H - A - 1) + (W - i - 1), W - i - 1, MOD) * ncr((A - 1) + i, i, MOD)
    ans %= MOD
print(ans)
