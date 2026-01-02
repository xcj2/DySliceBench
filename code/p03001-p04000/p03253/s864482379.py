import math
import os
import sys
from collections import Counter
from functools import reduce
from operator import mul

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N, M = list(map(int, sys.stdin.buffer.readline().split()))


def get_factors(n):
    """
    素因数分解
    :param int n:
    :rtype: list of int
    """
    if n <= 1:
        return []

    ret = []
    while n > 2 and n % 2 == 0:
        ret.append(2)
        n //= 2
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            ret.append(i)
            n //= i
        else:
            i += 2
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

    # 何度も呼ぶ場合は combination.py をつかう
    r = min(n - r, r)
    if r == 0:
        return 1
    if mod:
        return reduce(mul, range(n, n - r, -1)) * mod_inv(reduce(mul, range(r, 0, -1)), mod) % mod
    else:
        # math.factorial よりこっちのが速い
        # https://atcoder.jp/contests/abc110/submissions?f.Task=&f.Language=&f.Status=&f.User=nohtaray
        return reduce(mul, range(n, n - r, -1)) // reduce(mul, range(r, 0, -1))


def nhr(n, r, mod=None):
    """
    重複組み合わせの総数 nHr
    :param int n:
    :param int r:
    :param int mod:
    :return:
    """
    return ncr(n + r - 1, r, mod)


counts = Counter(get_factors(M))
ans = 1
for c in counts.values():
    # N 個から c 個選ぶ重複組合せ
    ans = ans * nhr(N, c, MOD) % MOD
print(ans)
