from collections import defaultdict
import os
from functools import reduce

import itertools
import sys
from math import gcd

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


N, K = list(map(int, sys.stdin.buffer.readline().split()))


def test(N, K):
    s = 0
    counts = defaultdict(int)
    for nums in itertools.product(range(1, K + 1), repeat=N):
        s += reduce(gcd, nums)
        counts[reduce(gcd, nums)] += 1
    print(counts)
    print(s % MOD)


# test(N, K)


# comb = Combination(max=N + K, mod=MOD)


# @debug
def count_patterns(n):
    # gcd の約数が n となるように選ぶ方法の数
    return pow(K // n, N, MOD)


counts = [0] * (K + 1)
for n in range(1, K + 1):
    cnt = count_patterns(n)
    counts[n] = cnt
for n in reversed(range(1, K + 1)):
    i = n * 2
    while i <= K:
        counts[n] -= counts[i]
        i += n
# print(counts)

ans = 0
for n in range(1, K + 1):
    ans += n * counts[n] % MOD
    ans %= MOD
print(ans)
