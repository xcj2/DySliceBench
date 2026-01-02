import math
import os
import sys

from functools import lru_cache

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18

N, K = list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


def mod_inv(a, mod):
    """
    a の逆元
    :param int a:
    :param int mod:
    :return:
    """
    return pow(a, mod - 2, mod)


@lru_cache(maxsize=None)
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

    # 何度も呼ぶ場合は最大の n 以下の階乗を事前に計算しておくといい
    if mod:
        return (
                math.factorial(n)
                * mod_inv(math.factorial(r), mod)
                * mod_inv(math.factorial(n - r), mod)
                % mod
        )
    else:
        return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


@lru_cache(maxsize=None)
def nhr(n, r, mod=None):
    """
    重複組み合わせの総数 nHr
    :param int n:
    :param int r:
    :param int mod:
    :return:
    """
    return ncr(n + r - 1, r, mod)


# K を i 個に分割する方法の数
# ncr(K-1,i-1)
# for i in range(1, 10):
#     print(i, ncr(K - 1, i - 1, MOD))

ans = []
for i in range(1, K + 1):
    # K を i 個に分割する方法の数
    ki = ncr(K - 1, i - 1, MOD)
    # i+1 のスペースに残りを入れる
    # 選ばなきゃいけないやつは減らす
    nocori = N - K - (i - 1)
    if nocori >= 0:
        ans.append(ki * nhr(i + 1, nocori, mod=MOD) % MOD)
    else:
        ans.append(0)
print('\n'.join(map(str, ans)))
