import os
from functools import reduce
from operator import mul

import itertools
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353


def ncr(n, r, mod=None):
    """
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
    """
    return ncr(n + r - 1, r, mod)


def cumsum(it):
    """
    累積和
    :param collections.Iterable it:
    """
    cs = 0
    ret = []
    for v in it:
        cs += v
        ret.append(cs)
    return ret


# a = nhr(10, 10)
N, M, Q = list(map(int, sys.stdin.buffer.readline().split()))
ABCD = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(Q)]

ans = 0
for r in range(M):
    for idx in itertools.combinations_with_replacement(range(1, N + 1), r=r):
        a = [0] * (N + 10)
        a[1] = 1
        for i in idx:
            a[i] += 1
        cum = cumsum(a)
        # print(idx, cum[1: N + 1])
        pt = 0
        for a, b, c, d in ABCD:
            if cum[b] - cum[a] == c:
                pt += d
        ans = max(ans, pt)
print(ans)
