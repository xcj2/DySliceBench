import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N, M = list(map(int, sys.stdin.readline().split()))
A = [int(sys.stdin.readline()) for _ in range(M)]

MOD = 10 ** 9 + 7
A = np.array(A)


# https://atcoder.jp/contests/abc066/submissions/5721975
def mod_invs(max, mod):
    """
    逆元のリスト 0 から max まで
    https://atcoder.jp/contests/abc127/submissions/5630531
    ここから。あんまり良くわかってない
    :param max:
    :param mod:
    :return:
    """
    invs = [1] * (max + 1)
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


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


def can_go():
    # 上までいける？
    return len(A) < 2 or min(np.diff(A)) > 1


factorials = get_factorials(N, MOD)


def mod_inv(a, mod):
    """
    a の逆元
    :param int a:
    :param int mod:
    :return:
    """
    return pow(a, mod - 2, mod)


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
    return (
            factorials[n]
            * mod_inv(factorials[r], mod)
            * mod_inv(factorials[n - r], mod)
            % mod
    )


if not can_go():
    print(0)
    exit()


def count(n):
    ans = 0
    for r in range(n):
        if r > n - r:
            break
        ans += ncr(n - r, r, MOD)
    return max(1, ans)


step = 0
ans = 1
for a in A:
    ans = ans * count(a - step - 1) % MOD
    step = a + 1
ans *= count(N - step)
print(ans % MOD)
